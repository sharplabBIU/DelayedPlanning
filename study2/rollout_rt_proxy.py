"""
Model-based RT proxy for Study 2: number of MBMC rollouts per decision step.
================================================================================

Companion to study1/rollout_rt_proxy.py.  Derives the model-based RT proxy -- the
number of rollouts (planning simulations) the fitted MBMC model must expend at each
decision step -- and uses it as a regressor for the WITHIN-SUBJECT deviation in
log RT, then compares the TRUE (empirical) effects to the SIMULATED (proxy) effects.

Decision-1 orientation control
------------------------------
Decision 1 is the trial-orientation stage: participants must first see WHICH goal
they are planning for.  Its RT therefore carries a goal-identification / orientation
cost that is common to every planning depth and is not planning search.  We remove
this variance by residualising BOTH the empirical log-RT deviation and the rollout
proxy on an `is_decision1` indicator.  This subtracts the common orientation offset
while preserving depth-specific structure within decision 1 (e.g. depth-3's
planning-initiation elevation at d1 relative to other depths survives as a within-d1
deviation), so all three depths remain interpretable.

Rollout requirement (see study1 script for full derivation)
-----------------------------------------------------------
mb_key[(goal, decision, state)] = [num_successes, total] is the model's urn at each
node.  Rollouts that GUARANTEE the plan is resolved = worst-case hypergeometric draw
    G(goal, decision) = (total - num_successes) + 1     (averaged over states).
Given caching + plan execution, the per-decision proxy over 20 trials is
    0                               decision >  initiation   (execute plan)
    G(goal, decision)               decision == initiation   (initiate plan)
    G(goal, decision) * (1 - c(t))  decision <  initiation   (relinquish once cached)
with c(t) = 1 - exp(-lambda*(t-1)) the cached-meta-control probability.

Outputs
-------
  rollout_rt_proxy_by_trial.csv, rollout_rt_proxy_averaged.csv
  true_vs_simulated_effects.png          <- true vs simulated effect per depth x decision
  rollout_proxy_over_trials.png
  console: regression of orientation-removed within-subject log-RT deviation on the
           orientation-removed proxy, reproduction of the delayed-planning signature,
           and robustness to lambda.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# ----------------------------------------------------------------------------------
# MBMC task representation (verbatim from model_fitting.py / simulate_full_model.py)
# goal == planning_depth (3 = cat, 2 = zebra, 1 = lamp)
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

# Decision at which planning must be INITIATED for each depth (matches delayed_planning).
INITIATION = {3: 1, 2: 2, 1: 3}
N_TRIALS = 20
# Caching / learning rate (timescale only; results robust -- see sweep in main()).
LAMBDA = 0.1


def guarantee_rollouts(goal, decision):
    """Worst-case hypergeometric draw count (total - successes) + 1, averaged over
    the reachable states for a goal x decision. Skips nodes with no goal path."""
    vals = [(total - succ) + 1
            for (g, d, _s), (succ, total) in mb_key.items()
            if g == goal and d == decision and total > 0 and succ > 0]
    return float(np.mean(vals)) if vals else 0.0


G = {(g, d): guarantee_rollouts(g, d) for g in (1, 2, 3) for d in (1, 2, 3)}


def rollout_proxy(planning_depth, decision, trial, lam):
    init = INITIATION[planning_depth]
    g = G[(planning_depth, decision)]
    if decision > init:               # execute already-resolved plan
        return 0.0
    if decision == init:              # initiate planning (irreducible)
        return g
    c_t = 1.0 - np.exp(-lam * (trial - 1))   # relinquish once meta-control cached
    return g * (1.0 - c_t)


def build_proxy_table(lam):
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
# Data + orientation control
# ----------------------------------------------------------------------------------
def residualise_on_orientation(frame, col):
    """Remove the decision-1 (orientation) component from `col`: subtract the fitted
    value of an OLS on the is_decision1 indicator. Keeps within-d1 depth structure."""
    f = frame.copy()
    f['is_d1'] = (f['decision'] == 1).astype(float)
    fit = smf.ols(f'{col} ~ is_d1', f).fit()
    return (f[col] - fit.predict(f)).values


def load_empirical():
    df = pd.read_csv('preprocessed_data.csv')
    df = df[['sub', 'planning_depth', 'decision',
             'trial_num_within_goal', 'RT', 'delayed_planning']].copy()
    df = df.dropna(subset=['RT'])
    # RT is log RT; within-subject deviation = log RT minus subject mean.
    df['logRT_dev'] = df.groupby('sub')['RT'].transform(lambda x: x - x.mean())
    # remove decision-1 orientation variance.
    df['logRT_dev_orient'] = residualise_on_orientation(df, 'logRT_dev')
    return df


def merge_proxy(df, proxy_tbl):
    m = df.merge(
        proxy_tbl[['planning_depth', 'decision', 'trial_num_within_goal',
                   'rollout_proxy', 'is_initiation', 'G_rollouts_needed']],
        on=['planning_depth', 'decision', 'trial_num_within_goal'], how='left')
    # remove decision-1 orientation variance from the proxy too (symmetric treatment).
    m['rollout_proxy_orient'] = residualise_on_orientation(m, 'rollout_proxy')
    m['rollout_proxy_orient_c'] = (m['rollout_proxy_orient']
                                   - m['rollout_proxy_orient'].mean())
    return m


def interaction_betas(frame, y):
    """OLS of `y` on delayed_planning * centred within-goal trial."""
    f = frame.copy()
    f['tn'] = (f['trial_num_within_goal'] - 10.5) / 10.0
    f['dp'] = f['delayed_planning']
    m = smf.ols(f'{y} ~ dp * tn', f).fit()
    return m.params['dp'], m.tvalues['dp'], m.params['dp:tn'], m.tvalues['dp:tn']


def main():
    sns.set(style='white', font_scale=1.4, palette='Set2')
    df = load_empirical()

    print('=' * 78)
    print('STUDY 2 -- rollouts needed to GUARANTEE plan resolution at each step')
    print('G(depth,decision) = (total - successes) + 1')
    print('=' * 78)
    print(pd.DataFrame(
        [[G[(d, dec)] for dec in (1, 2, 3)] for d in (3, 2, 1)],
        index=['depth 3 (cat)', 'depth 2 (zebra)', 'depth 1 (lamp)'],
        columns=['decision 1', 'decision 2', 'decision 3']).to_string())
    print('\ninitiation (plan) decision per depth:',
          {f'depth {k}': v for k, v in INITIATION.items()})
    print('decision-1 variance removed as trial-orientation (goal identification).')
    print(f'caching/learning rate lambda = {LAMBDA} (c(20) = {1 - np.exp(-LAMBDA*19):.2f})')

    proxy_tbl = build_proxy_table(LAMBDA)
    proxy_tbl.to_csv('rollout_rt_proxy_by_trial.csv', index=False)
    avg_tbl = (proxy_tbl.groupby(
        ['planning_depth', 'decision', 'initiation_decision', 'is_initiation',
         'G_rollouts_needed'])['rollout_proxy'].mean().reset_index()
        .rename(columns={'rollout_proxy': 'rollout_proxy_avg20trials'}))
    avg_tbl.to_csv('rollout_rt_proxy_averaged.csv', index=False)

    merged = merge_proxy(df, proxy_tbl)

    # ---- regression: orientation-removed log-RT deviation ~ orientation-removed proxy
    print('\n' + '=' * 78)
    print('Mixed model: (log-RT dev, orientation-removed) ~ (rollout proxy, '
          'orientation-removed)   [random slope by subject]')
    print('=' * 78)
    md = smf.mixedlm('logRT_dev_orient ~ rollout_proxy_orient_c', merged,
                     groups=merged['sub'], re_formula='~0 + rollout_proxy_orient_c')
    mdf = md.fit(method='lbfgs', maxiter=5000)
    print(mdf.summary())
    ols = smf.ols('logRT_dev_orient ~ rollout_proxy_orient_c', merged).fit()
    print(f"\nOLS reference: beta = {ols.params['rollout_proxy_orient_c']:.4f}, "
          f"t = {ols.tvalues['rollout_proxy_orient_c']:.2f}, "
          f"p = {ols.pvalues['rollout_proxy_orient_c']:.2e}, R^2 = {ols.rsquared:.4f}")

    # ---- planning-identifiable subset: drop decision-1 rows entirely ------------
    # At decision 1 planning is collinear with goal orientation (esp. depth 3, whose
    # initiation IS decision 1), so planning is only cleanly identifiable at
    # decisions 2-3. Refit the proxy there.
    sub = merged[merged['decision'] != 1].copy()
    sub['rp_c'] = sub['rollout_proxy'] - sub['rollout_proxy'].mean()
    print('\nPlanning-identifiable subset (decisions 2-3 only, orientation excluded):')
    o2 = smf.ols('logRT_dev ~ rp_c', sub).fit()
    m2 = smf.mixedlm('logRT_dev ~ rp_c', sub, groups=sub['sub'],
                     re_formula='~0 + rp_c').fit(method='lbfgs', maxiter=5000)
    print(f"  OLS   : beta = {o2.params['rp_c']:.4f}, t = {o2.tvalues['rp_c']:.1f}, "
          f"p = {o2.pvalues['rp_c']:.1e}, R^2 = {o2.rsquared:.4f}")
    print(f"  mixed : beta = {m2.params['rp_c']:.4f}, z = {m2.tvalues['rp_c']:.1f} "
          f"(random slope by subject)")

    # ---- reproduction of the delayed-planning signature (main + learning) -------
    print('\n' + '=' * 78)
    print('Reproduction of the delayed-planning RT signature (delayed_planning x '
          'trial), orientation-removed')
    print('=' * 78)
    eb = interaction_betas(df.assign(logRT_dev_orient=df['logRT_dev_orient']),
                           'logRT_dev_orient')
    pb = interaction_betas(merged, 'rollout_proxy_orient')
    print(f'  TRUE  log-RT dev : initiation beta = {eb[0]:+.3f} (t={eb[1]:.1f}), '
          f'x trial beta = {eb[2]:+.3f} (t={eb[3]:.1f})')
    print(f'  SIM   rollouts   : initiation beta = {pb[0]:+.3f} (t={pb[1]:.1f}), '
          f'x trial beta = {pb[2]:+.3f} (t={pb[3]:.1f})')

    # ---- robustness to lambda ---------------------------------------------------
    print('\nRobustness to caching rate lambda:')
    print('  lambda   corr(proxy,logRTdev_orient)   OLS_R2')
    for lam in (0.05, 0.10, 0.20, 0.30):
        m = merge_proxy(df, build_proxy_table(lam))
        r = np.corrcoef(m['rollout_proxy_orient_c'], m['logRT_dev_orient'])[0, 1]
        o = smf.ols('logRT_dev_orient ~ rollout_proxy_orient_c', m).fit()
        star = '  <- used' if abs(lam - LAMBDA) < 1e-9 else ''
        print(f'  {lam:<7.2f}  {r:>24.3f}   {o.rsquared:>6.3f}{star}')

    # ---- figures ----------------------------------------------------------------
    r_dis, r_all = _fig_true_vs_sim(merged)
    _fig_over_trials(proxy_tbl)
    print(f'\nTrue-vs-simulated per-cell effect correlation: '
          f'r = {r_dis:.3f} (planning-identifiable decisions 2-3), '
          f'r = {r_all:.3f} (all 9 cells incl. orientation-confounded decision 1)')
    print('Saved: true_vs_simulated_effects.png, rollout_proxy_over_trials.png, '
          'rollout_rt_proxy_by_trial.csv, rollout_rt_proxy_averaged.csv')


# ----------------------------------------------------------------------------------
# Figures
# ----------------------------------------------------------------------------------
def _cell_effects(merged, mature_only=True):
    """Per (depth, decision) mean of orientation-removed TRUE and SIM effects,
    each z-scored across cells for shape comparison."""
    f = merged[merged['trial_num_within_goal'] > 10] if mature_only else merged
    g = (f.groupby(['planning_depth', 'decision'])
         .agg(true=('logRT_dev_orient', 'mean'),
              sim=('rollout_proxy_orient', 'mean')).reset_index())
    for c in ('true', 'sim'):
        g[c + '_z'] = (g[c] - g[c].mean()) / g[c].std()
    return g


def _fig_true_vs_sim(merged):
    g = _cell_effects(merged, mature_only=True)
    g['is_d1'] = g['decision'] == 1
    r_all = np.corrcoef(g['true_z'], g['sim_z'])[0, 1]
    gd = g[~g['is_d1']]                       # planning-identifiable cells (dec 2-3)
    r_dis = np.corrcoef(gd['true_z'], gd['sim_z'])[0, 1]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(16, 6),
                                   gridspec_kw={'width_ratios': [1.5, 1]})

    # left: grouped bars per depth x decision, true vs simulated
    long = pd.concat([
        g.assign(effect=g['true_z'], source='true (empirical log RT)'),
        g.assign(effect=g['sim_z'], source='simulated (rollout proxy)'),
    ], ignore_index=True)
    long['depth x decision'] = ('d' + long['planning_depth'].astype(str)
                                + ' / dec' + long['decision'].astype(str))
    order = [f'd{dep} / dec{dec}' for dep in (3, 2, 1) for dec in (1, 2, 3)]
    sns.barplot(data=long, x='depth x decision', y='effect', hue='source',
                order=order, palette=['#4C72B0', '#55A868'], ax=axL)
    axL.axhline(0, color='k', lw=0.8)
    axL.set_ylabel('effect on RT (z-scored, orientation-removed)')
    axL.set_xlabel('planning depth / decision')
    axL.tick_params(axis='x', rotation=45)
    axL.set_title('True vs simulated delayed-planning effects (mature phase)')
    ymax = axL.get_ylim()[1]
    for i, lab in enumerate(order):
        dep = int(lab[1]); dec = int(lab.split('dec')[1])
        if INITIATION[dep] == dec:
            axL.scatter(i, ymax * 0.93, marker='*', s=260, color='crimson',
                        zorder=5, clip_on=False)
        if dec == 1:                          # shade orientation-confounded cells
            axL.axvspan(i - 0.5, i + 0.5, color='grey', alpha=0.10, zorder=0)

    # right: scatter true vs simulated; decision-1 (orientation) cells greyed out,
    # regression fit on the planning-identifiable decision 2-3 cells only.
    sns.regplot(data=gd, x='sim_z', y='true_z', ax=axR, color='mediumseagreen',
                scatter_kws={'s': 90}, label='decisions 2-3 (planning)')
    axR.scatter(g.loc[g['is_d1'], 'sim_z'], g.loc[g['is_d1'], 'true_z'],
                s=90, facecolors='none', edgecolors='grey',
                label='decision 1 (orientation)')
    for _, row in g.iterrows():
        axR.annotate(f"d{int(row.planning_depth)}/dec{int(row.decision)}",
                     (row.sim_z, row.true_z), fontsize=10,
                     xytext=(4, 4), textcoords='offset points')
    axR.set_xlabel('simulated (rollout proxy), z')
    axR.set_ylabel('true (empirical log RT), z')
    axR.set_ylim(g['true_z'].min() - 0.6, g['true_z'].max() + 0.6)
    axR.set_title(f'per-cell correspondence\nr = {r_dis:.2f} (planning), '
                  f'{r_all:.2f} (all cells)')
    axR.legend(fontsize=11, loc='best')

    fig.suptitle('Study 2: model rollout proxy reproduces empirical delayed-planning '
                 'RT effects (red star = initiation point; decision-1 = orientation)',
                 y=1.03)
    plt.tight_layout()
    plt.savefig('true_vs_simulated_effects.png', dpi=300, bbox_inches='tight')
    plt.close()
    return r_dis, r_all


def _fig_over_trials(proxy_tbl):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    for ax, depth in zip(axes, (3, 2, 1)):
        sub = proxy_tbl[proxy_tbl['planning_depth'] == depth]
        for dec in (1, 2, 3):
            s = sub[sub['decision'] == dec]
            init = INITIATION[depth]
            ax.plot(s['trial_num_within_goal'], s['rollout_proxy'], marker='o', ms=4,
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


if __name__ == '__main__':
    main()
