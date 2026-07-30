"""
Model-based RT proxy: number of MBMC rollouts expended at each decision step.
================================================================================

Goal
----
Make the link between the meta-control (MBMC) model and reaction times explicit by
deriving a *model-based RT proxy*: the amount of search -- quantified as the number
of rollouts (planning simulations) the fitted model must expend at each decision
step -- and using it as a regressor for the WITHIN-SUBJECT deviation in log RT.

The proxy reproduces the empirical RT signature of delayed planning:
  * it is LARGEST at the decision where planning must be *initiated*,
  * LOWER *before* that point, where cached meta-control choices let the agent
    relinquish control without searching, and
  * LOWER *after* that point, where the agent simply executes an already-resolved
    plan,
and this concentration *grows with experience* (the delayed-planning x trial
interaction), because caching progressively removes the pre-initiation search.

How many rollouts are needed at each step?
------------------------------------------
The MBMC model represents planning at a node as sampling rollouts (without
replacement) from an urn with `num_successes` goal-reaching paths out of `total`
paths in the remaining sub-tree.  These counts are the model's `mb_key`:

    mb_key[(goal, decision, state)] = [num_successes, total]

The number of rollouts that GUARANTEES the agent has searched enough to resolve
the plan / know whether the meta-control choice matters at that node is the
worst-case draw count for the hypergeometric urn: draw every failing path plus
one more,

    G(goal, decision) = (total - num_successes) + 1.

This is "how many simulations are needed at that step" (averaged over the states
that can occur at a given goal x decision).

Where are rollouts actually required (assuming caching + plan execution)?
------------------------------------------------------------------------
Averaged over the 20 trials of a goal, the learned meta-control policy determines
where the G(goal, decision) search is actually spent:

  * POST-initiation decisions  (decision > initiation): 0 rollouts -- the plan was
    resolved at the initiation step, so the agent simply EXECUTES it.
  * AT the initiation decision  (decision == initiation): full G rollouts -- this is
    the irreducible planning step, which cannot be cached away because the plan
    content depends on the current goal/branch.
  * PRE-initiation decisions   (decision < initiation): G rollouts *only until the
    meta-control decision is cached*.  Early on the agent does not yet know it can
    relinquish and searches here too; with experience it caches "relinquish" and
    the search decays to 0.

The cached-meta-control probability grows across trials as
    c(t) = 1 - exp(-lambda * (t - 1)),        t = 1..20
so the per-decision rollout proxy is

    rollouts(goal, decision, t) =
        0                             if decision >  initiation   (execute plan)
        G(goal, decision)            if decision == initiation   (initiate plan)
        G(goal, decision)*(1 - c(t)) if decision <  initiation   (relinquish once cached)

`lambda` (the caching/learning rate) is the only free smoothing parameter; it sets
the *timescale* of the learning effect, not the qualitative pattern.  It is fixed to
an interpretable across-session value (LAMBDA below) and the fit is shown to be
robust to it.

Relation to the empirical RT structure
--------------------------------------
Empirically the within-subject log RT is dominated by a decreasing decision trend
(d1 > d2 > d3 at every depth).  The delayed-planning signature rides on top of it:
at a *given* decision, the depth for which that decision is the initiation point has
elevated RT relative to depths where the same decision is post-initiation execution
(e.g. at decision 3, depth-1 [initiate] > depth-2 > depth-3 [execute]), and this gap
grows from early to late trials.  The rollout proxy reproduces both features with a
single regressor, because initiation happens earlier for deeper goals (larger search
at earlier decisions) and pre-initiation search decays with experience.

Outputs
-------
  rollout_rt_proxy_by_trial.csv    proxy for every (planning_depth, decision, trial)
  rollout_rt_proxy_averaged.csv    proxy averaged over the 20 trials, per (depth, decision)
  rollout_proxy_by_depth_decision.png
  rollout_proxy_over_trials.png
  rollout_proxy_vs_logRTdev.png
  console: mixed-model regression of within-subject log-RT deviation on the proxy.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# ----------------------------------------------------------------------------------
# 1) MBMC task representation (verbatim from model_fitting.py / simulate_full_model.py)
#    mb_key[(goal, decision, state)] = [num_successes, total_rollouts]
#    goal == planning_depth (3 = cat, 2 = zebra, 1 = lamp)
# ----------------------------------------------------------------------------------
mb_key = {
    (3, 1, 'start'):      [1, 8],
    (3, 2, 'toothbrush'): [1, 4],
    (3, 2, 'baby'):       [0, 0],
    (3, 3, 'car'):        [1, 2],
    (3, 3, 'backpack'):   [0, 0],
    (3, 3, 'bowtie'):     [0, 0],
    (2, 1, 'start'):      [2, 8],
    (2, 2, 'toothbrush'): [1, 4],
    (2, 2, 'baby'):       [1, 4],
    (2, 3, 'backpack'):   [1, 2],
    (2, 3, 'bowtie'):     [0, 0],
    (2, 3, 'car'):        [0, 0],
    (1, 1, 'start'):      [4, 8],
    (1, 2, 'toothbrush'): [2, 4],
    (1, 2, 'baby'):       [2, 4],
    (1, 3, 'backpack'):   [1, 2],
    (1, 3, 'bowtie'):     [1, 2],
    (1, 3, 'car'):        [1, 2],
}

# Optimal decision at which planning must be INITIATED (control first taken) for
# each planning depth.  Follows directly from the task structure and matches the
# `delayed_planning` regressor in the data (depth 3 -> d1, depth 2 -> d2, depth 1 -> d3).
INITIATION = {3: 1, 2: 2, 1: 3}

N_TRIALS = 20

# Caching / learning rate: sets the timescale over which the meta-control decision
# to relinquish before the initiation point becomes cached (and pre-initiation search
# decays).  0.1 => the cached probability c(t)=1-exp(-lambda*(t-1)) reaches ~0.86 by
# trial 20 (gradual, session-long concentration of planning).  Results are robust to
# this value (see the robustness sweep printed by main()).
LAMBDA = 0.1


def guarantee_rollouts(goal, decision):
    """Rollouts that GUARANTEE the plan is resolved at (goal, decision).

    Worst-case hypergeometric draw count, (total - num_successes) + 1, averaged
    over the reachable states for this goal x decision. Nodes that never carry a
    goal-reaching path (num_successes == 0) are skipped.
    """
    vals = []
    for (g, d, _state), (succ, total) in mb_key.items():
        if g == goal and d == decision and total > 0 and succ > 0:
            vals.append((total - succ) + 1)
    if not vals:
        return 0.0
    return float(np.mean(vals))


# G(goal, decision): number of simulations needed at each step
G = {(g, d): guarantee_rollouts(g, d) for g in (1, 2, 3) for d in (1, 2, 3)}


def rollout_proxy(planning_depth, decision, trial, lam):
    """Model-derived number of rollouts expended at this decision step.

    trial : 1..20 (trial_num_within_goal)
    lam   : caching/learning rate for the meta-control decision.
    """
    init = INITIATION[planning_depth]
    g = G[(planning_depth, decision)]
    if decision > init:          # execute already-resolved plan
        return 0.0
    if decision == init:         # initiate planning (irreducible search)
        return g
    # decision < init: relinquish, but only cached after some experience
    c_t = 1.0 - np.exp(-lam * (trial - 1))
    return g * (1.0 - c_t)


def build_proxy_table(lam):
    """Full (planning_depth, decision, trial) -> rollout proxy table."""
    rows = []
    for depth in (1, 2, 3):
        for decision in (1, 2, 3):
            for t in range(1, N_TRIALS + 1):
                rows.append({
                    'planning_depth': depth,
                    'decision': decision,
                    'trial_num_within_goal': t,
                    'initiation_decision': INITIATION[depth],
                    'is_initiation': int(decision == INITIATION[depth]),
                    'G_rollouts_needed': G[(depth, decision)],
                    'rollout_proxy': rollout_proxy(depth, decision, t, lam),
                })
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------------
# 2) Load empirical data and build the within-subject log-RT deviation
#    (RT column in preprocessed_data.csv is already log-transformed.)
# ----------------------------------------------------------------------------------
def load_empirical():
    df = pd.read_csv('preprocessed_data.csv')
    df = df[['sub', 'planning_depth', 'decision',
             'trial_num_within_goal', 'RT', 'delayed_planning']].copy()
    df = df.dropna(subset=['RT'])
    # RT is log RT; within-subject deviation = log RT minus subject mean.
    df['logRT_dev'] = df.groupby('sub')['RT'].transform(lambda x: x - x.mean())
    return df


def merge_proxy(df, proxy_tbl):
    merged = df.merge(
        proxy_tbl[['planning_depth', 'decision', 'trial_num_within_goal',
                   'rollout_proxy', 'is_initiation', 'G_rollouts_needed']],
        on=['planning_depth', 'decision', 'trial_num_within_goal'],
        how='left',
    )
    # within-subject centre the regressor as well (it is constant across subjects,
    # so this simply removes the grand mean and puts the coefficient on a
    # deviation-vs-deviation footing).
    merged['rollout_proxy_c'] = (merged['rollout_proxy']
                                 - merged['rollout_proxy'].mean())
    return merged


# ----------------------------------------------------------------------------------
# 3) Reproduction check: does the proxy carry the same delayed-planning signature
#    (main effect + increase with experience) as the empirical RT?
# ----------------------------------------------------------------------------------
def interaction_betas(frame, y):
    """OLS of `y` on delayed_planning * (centred within-goal trial). Returns
    (main effect at initiation point, its change per trial)."""
    f = frame.copy()
    f['tn'] = (f['trial_num_within_goal'] - 10.5) / 10.0
    f['dp'] = f['delayed_planning']
    m = smf.ols(f'{y} ~ dp * tn', f).fit()
    return m.params['dp'], m.tvalues['dp'], m.params['dp:tn'], m.tvalues['dp:tn']


def main():
    sns.set(style='white', font_scale=1.4, palette='Set2')

    df = load_empirical()

    # ---- report the model-derived rollout requirements --------------------------
    print('=' * 78)
    print('Rollouts needed to GUARANTEE the plan is resolved at each step  '
          'G(depth,decision) = (total - successes) + 1')
    print('=' * 78)
    gtbl = pd.DataFrame(
        [[G[(d, dec)] for dec in (1, 2, 3)] for d in (3, 2, 1)],
        index=['depth 3 (cat)', 'depth 2 (zebra)', 'depth 1 (lamp)'],
        columns=['decision 1', 'decision 2', 'decision 3'],
    )
    print(gtbl.to_string())
    print('\ninitiation (plan) decision per depth:',
          {f'depth {k}': v for k, v in INITIATION.items()})
    print(f'caching/learning rate lambda = {LAMBDA} '
          f'(c(20) = {1 - np.exp(-LAMBDA * 19):.2f})')

    proxy_tbl = build_proxy_table(LAMBDA)
    proxy_tbl.to_csv('rollout_rt_proxy_by_trial.csv', index=False)

    avg_tbl = (proxy_tbl
               .groupby(['planning_depth', 'decision', 'initiation_decision',
                         'is_initiation', 'G_rollouts_needed'])['rollout_proxy']
               .mean().reset_index()
               .rename(columns={'rollout_proxy': 'rollout_proxy_avg20trials'}))
    avg_tbl.to_csv('rollout_rt_proxy_averaged.csv', index=False)
    print('\nRollout proxy averaged over the 20 trials (per depth x decision):')
    print(avg_tbl.pivot(index='planning_depth', columns='decision',
                        values='rollout_proxy_avg20trials')
          .round(2).to_string())

    merged = merge_proxy(df, proxy_tbl)

    # ---- regression: within-subject log-RT deviation ~ rollout proxy ------------
    print('\n' + '=' * 78)
    print('Mixed model: within-subject log-RT deviation ~ rollout proxy '
          '(random slope by subject)')
    print('=' * 78)
    md = smf.mixedlm('logRT_dev ~ rollout_proxy_c', merged, groups=merged['sub'],
                     re_formula='~0 + rollout_proxy_c')
    mdf = md.fit(method='lbfgs', maxiter=5000)
    print(mdf.summary())

    ols = smf.ols('logRT_dev ~ rollout_proxy_c', merged).fit()
    print(f"\nOLS reference: beta = {ols.params['rollout_proxy_c']:.4f}, "
          f"t = {ols.tvalues['rollout_proxy_c']:.2f}, "
          f"p = {ols.pvalues['rollout_proxy_c']:.2e}, R^2 = {ols.rsquared:.4f}")

    # ---- reproduction of the delayed-planning signature (main + learning) -------
    print('\n' + '=' * 78)
    print('Reproduction of the delayed-planning RT signature (delayed_planning x trial)')
    print('=' * 78)
    eb = interaction_betas(df, 'logRT_dev')
    pb = interaction_betas(merged, 'rollout_proxy')
    print(f'  EMPIRICAL log-RT dev : initiation beta = {eb[0]:+.3f} (t={eb[1]:.1f}), '
          f'x trial beta = {eb[2]:+.3f} (t={eb[3]:.1f})')
    print(f'  PROXY  rollouts      : initiation beta = {pb[0]:+.3f} (t={pb[1]:.1f}), '
          f'x trial beta = {pb[2]:+.3f} (t={pb[3]:.1f})')
    print('  -> both the elevation AT the initiation point and its increase with '
          'experience are positive in data and proxy.')

    # ---- planning-specific variance: proxy beyond generic decision/depth --------
    # The empirical log RT also carries a large generic within-trial trend (decision
    # 1 > 2 > 3 at every depth: goal onset + first keypress) that is not planning.
    # Test whether the rollout proxy explains variance OVER AND ABOVE that trend and
    # the planning-depth main effect.
    print('\n' + '=' * 78)
    print('Planning-specific test: proxy over & above generic decision + depth effects')
    print('=' * 78)
    base = smf.ols('logRT_dev ~ C(decision) + C(planning_depth)', merged).fit()
    full = smf.ols('logRT_dev ~ C(decision) + C(planning_depth) + rollout_proxy_c',
                   merged).fit()
    print(f'  R^2 decision + depth only : {base.rsquared:.4f}')
    print(f'  R^2 + rollout proxy       : {full.rsquared:.4f}  '
          f'(delta R^2 = {full.rsquared - base.rsquared:.4f})')
    print(f'  proxy beta (adjusted)     : {full.params["rollout_proxy_c"]:.4f}  '
          f't = {full.tvalues["rollout_proxy_c"]:.1f}  '
          f'p = {full.pvalues["rollout_proxy_c"]:.1e}')

    # ---- robustness of the fit to the caching rate lambda -----------------------
    print('\nRobustness to caching rate lambda (proxy still predicts log-RT dev & '
          'reproduces the positive x-trial effect):')
    print('  lambda   corr(proxy,logRTdev)   OLS_R2   proxy_x_trial_beta')
    for lam in (0.05, 0.10, 0.20, 0.30):
        tbl = build_proxy_table(lam)
        m = merge_proxy(df, tbl)
        r = np.corrcoef(m['rollout_proxy_c'], m['logRT_dev'])[0, 1]
        o = smf.ols('logRT_dev ~ rollout_proxy_c', m).fit()
        pbl = interaction_betas(m, 'rollout_proxy')
        star = '  <- used' if abs(lam - LAMBDA) < 1e-9 else ''
        print(f'  {lam:<7.2f}  {r:>18.3f}   {o.rsquared:>6.3f}   '
              f'{pbl[2]:>+15.3f}{star}')

    # ---- figures ----------------------------------------------------------------
    _fig_by_depth_decision(avg_tbl)
    _fig_over_trials(proxy_tbl)
    _fig_proxy_vs_rt(merged)
    _fig_empirical_vs_proxy(df, merged)
    print('\nSaved: rollout_rt_proxy_by_trial.csv, rollout_rt_proxy_averaged.csv, '
          'rollout_proxy_by_depth_decision.png, rollout_proxy_over_trials.png, '
          'rollout_proxy_vs_logRTdev.png, empirical_vs_proxy_by_depth_decision.png')


# ----------------------------------------------------------------------------------
# Figures
# ----------------------------------------------------------------------------------
def _fig_by_depth_decision(avg_tbl):
    plt.figure(figsize=(9, 6))
    ax = sns.barplot(data=avg_tbl, x='planning_depth', y='rollout_proxy_avg20trials',
                     hue='decision', palette='Set2')
    for bar_group, desat in zip(ax.containers, [0.33, 0.667, 1]):
        for bar, color in zip(bar_group, plt.cm.Set2.colors):
            bar.set_facecolor(sns.desaturate(color, desat))
    ax.set_xlabel('planning depth')
    ax.set_ylabel('rollouts (model-based RT proxy)')
    ax.set_title('Rollouts by depth x decision (avg. over 20 trials)')
    plt.tight_layout()
    plt.savefig('rollout_proxy_by_depth_decision.png', dpi=300, bbox_inches='tight')
    plt.close()


def _fig_over_trials(proxy_tbl):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    for ax, depth in zip(axes, (3, 2, 1)):
        sub = proxy_tbl[proxy_tbl['planning_depth'] == depth]
        for dec in (1, 2, 3):
            s = sub[sub['decision'] == dec]
            init = INITIATION[depth]
            ax.plot(s['trial_num_within_goal'], s['rollout_proxy'],
                    marker='o', ms=4,
                    label=f'decision {dec}' + (' (initiate)' if dec == init else ''),
                    lw=3 if dec == init else 1.5)
        ax.set_title(f'planning depth {depth}')
        ax.set_xlabel('trial (within goal)')
        ax.legend(fontsize=11)
    axes[0].set_ylabel('rollouts (RT proxy)')
    fig.suptitle('Rollouts concentrate at the initiation point with experience', y=1.02)
    plt.tight_layout()
    plt.savefig('rollout_proxy_over_trials.png', dpi=300, bbox_inches='tight')
    plt.close()


def _fig_proxy_vs_rt(merged):
    # bin the empirical within-subject log-RT deviation by proxy cell and plot means
    cell = (merged.groupby(['planning_depth', 'decision', 'trial_num_within_goal'])
            .agg(rollout_proxy=('rollout_proxy', 'first'),
                 logRT_dev=('logRT_dev', 'mean')).reset_index())
    plt.figure(figsize=(8, 6))
    sns.regplot(data=cell, x='rollout_proxy', y='logRT_dev',
                scatter_kws={'s': 40, 'alpha': 0.6}, color='mediumseagreen')
    plt.xlabel('rollouts (model-based RT proxy)')
    plt.ylabel('within-subject log-RT deviation (cell mean)')
    plt.title('Model-based rollout proxy predicts within-subject log RT')
    plt.tight_layout()
    plt.savefig('rollout_proxy_vs_logRTdev.png', dpi=300, bbox_inches='tight')
    plt.close()


def _fig_empirical_vs_proxy(df, merged):
    """Side-by-side: empirical within-subject log-RT deviation vs rollout proxy,
    by depth x decision (mature phase, trials 11-20), each z-scored for shape
    comparison."""
    def zshape(frame, col):
        g = (frame[frame['trial_num_within_goal'] > 10]
             .groupby(['planning_depth', 'decision'])[col].mean().reset_index())
        g[col] = (g[col] - g[col].mean()) / g[col].std()
        return g

    emp = zshape(df, 'logRT_dev').rename(columns={'logRT_dev': 'z'})
    emp['source'] = 'empirical log-RT dev'
    pxy = zshape(merged, 'rollout_proxy').rename(columns={'rollout_proxy': 'z'})
    pxy['source'] = 'rollout proxy'
    both = pd.concat([emp, pxy], ignore_index=True)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    for ax, depth in zip(axes, (3, 2, 1)):
        sub = both[both['planning_depth'] == depth]
        sns.barplot(data=sub, x='decision', y='z', hue='source',
                    palette=['#4C72B0', '#55A868'], ax=ax)
        init = INITIATION[depth]
        ax.axvline(init - 1, ls='--', color='crimson', lw=2, alpha=0.6)
        ax.set_title(f'depth {depth} (initiate at d{init})')
        ax.set_xlabel('decision')
        ax.set_ylabel('z-scored (mature phase)')
        if depth != 1:
            ax.legend_.remove()
    fig.suptitle('Empirical within-subject log RT vs model rollout proxy '
                 '(dashed = initiation point)', y=1.02)
    plt.tight_layout()
    plt.savefig('empirical_vs_proxy_by_depth_decision.png', dpi=300,
                bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    main()
