"""
Fig S6 redo under the SOFT-GATED model: simulate decision times (rollouts) with
the soft-gated + state-tailored-saturation simulator (as mbmc_rollout_rt_softgate),
for 20 synthetic subjects with top-10%-like breadths (b1 in [0.70,0.98],
b2 in [0.05,0.25]), convert rollouts -> RT = 0.70 + 0.30*rollouts (log-scaled),
and fit the SAME hierarchical Bayesian RT LMM as on the empirical data.
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pymc as pm
import arviz as az
from scipy.special import comb, softmax
import warnings
warnings.filterwarnings('ignore')

# soft-gated, state-tailored urns (canonical path), as in mbmc_rollout_rt_softgate
URN1 = {(3, 1): (1, 8), (3, 2): (1, 4), (3, 3): (1, 2),
        (2, 1): (1, 4), (2, 2): (1, 4), (2, 3): (1, 2),
        (1, 1): (2, 4), (1, 2): (1, 2), (1, 3): (1, 2)}
URN2 = {(2, 1): (1, 4), (1, 1): (2, 4), (1, 2): (1, 2)}
INITIATION = {3: 1, 2: 2, 1: 3}

N_SUBJECTS = 20
N_TRIALS = 20
RT_FLOOR = 0.7
RT_PER_ROLLOUT = 0.3
MB_CONTROL = 6.0
DISCOUNT = 0.9
CHOICE_BIAS = 0.0
SEED = 7
B1_RANGE = (0.70, 0.98)
B2_RANGE = (0.05, 0.25)


def p_success(succ, total, draws):
    if succ <= 0 or total <= 0:
        return 0.0
    failures = total - succ
    if draws <= failures:
        return 1.0 - comb(failures, draws, exact=False) / comb(total, draws, exact=False)
    return 1.0


def values(goal, decision, one_ok, two_ok):
    disc = 4 * (DISCOUNT ** (3 - decision))
    v_take, v_rel = 0.0, 0.0
    if goal == 3:
        if one_ok:
            v_take, v_rel = disc, 1.0
        else:
            v_rel = 1.0
    else:
        early = (goal == 2 and decision == 1) or (goal == 1 and decision < 3)
        if early:
            if two_ok:
                v_take, v_rel = disc, 1.0 + disc
            elif one_ok:
                v_take, v_rel = disc, 1.0
            else:
                v_rel = 1.0
        else:
            if one_ok:
                v_take, v_rel = disc, 1.0
            else:
                v_rel = 1.0
    return v_take, v_rel


def simulate_goal(goal, rng, b1, b2):
    """Soft-gated decision-time simulation; yields (trial, decision, rollouts, control)."""
    d1_budget, d2_budget = b1 * 8.0, b2 * 4.0
    exp1 = {d: 0.0 for d in (1, 2, 3)}
    exp2 = {d: 0.0 for d in (1, 2, 3)}
    relinquish_cached = {d: False for d in (1, 2, 3)}
    out = []
    for t in range(N_TRIALS):
        control_taken = False
        goal_alive = True
        relinquished_now = []
        for d in (1, 2, 3):
            succ1, N1 = URN1[(goal, d)]
            succ2, N2 = URN2.get((goal, d), (0, 0))
            safe = succ2 > 0
            if control_taken:                       # executing an already-taken plan
                out.append((t + 1, d, 0.0, 1)); continue
            if relinquish_cached[d]:                # cached relinquish -> no rollouts
                out.append((t + 1, d, 0.0, 0))
                relinquished_now.append(d)
                if not safe and rng.random() < 0.5:
                    goal_alive = False
                continue
            # meta-planning: first search until saturated
            sat1 = exp1[d] > (N1 - succ1)
            m1 = 0.0 if sat1 else min(d1_budget, max(0.0, N1 - exp1[d]))
            exp1[d] += m1
            p1 = p_success(succ1, N1, exp1[d])
            # soft-gated second search, engaged in proportion to p1
            sat2 = succ2 > 0 and exp2[d] > (N2 - succ2)
            m2 = 0.0 if (succ2 <= 0 or sat2) else p1 * min(d2_budget,
                                                           max(0.0, N2 - exp2[d]))
            exp2[d] += m2
            p2 = p_success(succ2, N2, exp2[d])
            plan = min(d1_budget, N1)               # planning proper, active visits
            roll = m1 + m2 + plan
            w_two = p1 * p2
            w_one = p1 * (1.0 - w_two)
            u = rng.random()
            two_ok = u < w_two
            one_ok = (not two_ok) and (u < w_two + w_one)
            v_take, v_rel = values(goal, d, one_ok, two_ok)
            q = np.array([v_take * MB_CONTROL + CHOICE_BIAS, v_rel * MB_CONTROL])
            took = rng.random() < softmax(q)[0]
            out.append((t + 1, d, roll, 1 if took else 0))
            if took:
                control_taken = True
            else:
                relinquished_now.append(d)
                if not safe and rng.random() < 0.5:
                    goal_alive = False
        for d in relinquished_now:
            relinquish_cached[d] = bool(goal_alive)
    return out


def build_data():
    rng = np.random.default_rng(SEED)
    rows = []
    for s in range(N_SUBJECTS):
        b1 = rng.uniform(*B1_RANGE)
        b2 = rng.uniform(*B2_RANGE)
        for goal in (3, 2, 1):
            for (t, d, roll, ctrl) in simulate_goal(goal, rng, b1, b2):
                rows.append({'sub': s, 'planning_depth': goal,
                             'trial_num_within_goal': t, 'decision': d,
                             'rollouts': roll, 'control': ctrl, 'b1': b1, 'b2': b2})
    df = pd.DataFrame(rows)
    df['RT_sec'] = RT_FLOOR + RT_PER_ROLLOUT * df['rollouts']
    df['RT'] = np.log(df['RT_sec'])
    df['delayed_planning'] = (df['decision'] ==
                              df['planning_depth'].map(INITIATION)).astype(int)
    df['goal_switch'] = (df['trial_num_within_goal'] == 1).astype(int)
    df['control_regressor'] = df['control'].astype(float)
    return df


def fit_lmm(df):
    sub_idx, subs = pd.factorize(df['sub'])
    RT = df['RT'].values
    delayed_planning = df['delayed_planning'].values.astype(float)
    trial_num_v = (df['trial_num_within_goal'].values - 21) / 20.0
    goalswitch = df['goal_switch'].values.astype(float)
    decision = df['decision'].values - 2
    planning_depth = df['planning_depth'].values - 2
    control_effect = df['control_regressor'].values
    interaction = delayed_planning * trial_num_v

    with pm.Model():
        intercept = pm.Normal('intercept', mu=0, sigma=2)
        coef_delayed_planning = pm.Normal('coef_delayed_planning', mu=0, sigma=2)
        coef_trial_num = pm.Normal('coef_trial_num', mu=0, sigma=2)
        coef_goalswitch = pm.Normal('coef_goalswitch', mu=0, sigma=2)
        coef_decision = pm.Normal('coef_decision', mu=0, sigma=2)
        coef_planning_depth = pm.Normal('coef_planning_depth', mu=0, sigma=2)
        coef_c = pm.Normal('coef_c', mu=0, sigma=2)
        coef_interaction = pm.Normal('coef_interaction', mu=0, sigma=2)
        sigma_sub = pm.HalfNormal('sigma_sub', 2)
        intercept_sub = pm.Normal('intercept_sub', 0, sigma_sub, shape=len(subs))
        sigma_slope_dp = pm.HalfNormal('sigma_slope_dp', 2)
        slope_sub_dp = pm.Normal('slope_sub_dp', 0, sigma_slope_dp, shape=len(subs))
        sigma_slope_c = pm.HalfNormal('sigma_slope_c', 2)
        slope_sub_c = pm.Normal('slope_sub_c', 0, sigma_slope_c, shape=len(subs))
        sigma_slope_gs = pm.HalfNormal('sigma_slope_gs', 2)
        slope_sub_gs = pm.Normal('slope_sub_gs', 0, sigma_slope_gs, shape=len(subs))
        sigma_slope_d = pm.HalfNormal('sigma_slope_d', 2)
        slope_sub_d = pm.Normal('slope_sub_d', 0, sigma_slope_d, shape=len(subs))
        sigma_slope_pd = pm.HalfNormal('sigma_slope_pd', 2)
        slope_sub_pd = pm.Normal('slope_sub_pd', 0, sigma_slope_pd, shape=len(subs))
        sigma_slope_tn = pm.HalfNormal('sigma_slope_tn', 2)
        slope_sub_tn = pm.Normal('slope_sub_tn', 0, sigma_slope_tn, shape=len(subs))
        sigma_slope_interaction = pm.HalfNormal('sigma_slope_interaction', 2)
        slope_sub_interaction = pm.Normal('slope_sub_interaction', 0,
                                          sigma_slope_interaction, shape=len(subs))
        mu = (intercept + intercept_sub[sub_idx] +
              (coef_delayed_planning + slope_sub_dp[sub_idx]) * delayed_planning +
              (coef_trial_num + slope_sub_tn[sub_idx]) * trial_num_v +
              (coef_goalswitch + slope_sub_gs[sub_idx]) * goalswitch +
              (coef_decision + slope_sub_d[sub_idx]) * decision +
              (coef_c + slope_sub_c[sub_idx]) * control_effect +
              (coef_planning_depth + slope_sub_pd[sub_idx]) * planning_depth +
              (coef_interaction + slope_sub_interaction[sub_idx]) * interaction)
        sigma = pm.HalfNormal('sigma', 2)
        pm.Normal('RT_obs', mu=mu, sigma=sigma, observed=RT)
        trace = pm.sample(draws=2000, tune=2000, target_accept=0.99,
                          chains=4, cores=4, random_seed=SEED, progressbar=False)
    return trace


def posterior_panel(ax, samples, xlabel):
    sns.kdeplot(samples, fill=True, color='gray', ax=ax)
    hdi = np.asarray(az.hdi(samples, prob=0.95)).ravel()
    y0 = ax.get_ylim()[1] * 0.04
    ax.add_patch(plt.Rectangle((hdi[0], y0), hdi[1] - hdi[0], y0 * 1.2,
                               color='gold', zorder=12))
    ax.axvline(0, color='k', lw=1, ls='--')
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Density')


def main():
    df = build_data()
    df.to_csv('rt_lmm_simulated_softgate_data.csv', index=False)
    print('Simulated %d subjects, %d rows; mean RT_sec=%.2f'
          % (df['sub'].nunique(), len(df), df['RT_sec'].mean()), flush=True)
    trace = fit_lmm(df)
    trace.to_netcdf('rt_lmm_simulated_softgate_trace.nc')
    summ = az.summary(trace, var_names=['coef_delayed_planning', 'coef_trial_num',
                                        'coef_interaction'], ci_prob=0.95)
    print(summ.to_string(), flush=True)
    dp = trace.posterior['coef_delayed_planning'].values.flatten()
    inter = trace.posterior['coef_interaction'].values.flatten()
    hlo, hhi = np.asarray(az.hdi(inter, prob=0.95)).ravel()
    print('\ncoef_interaction: mean=%.3f  95%% HDI=[%.3f, %.3f]  P(>0)=%.3f'
          % (inter.mean(), hlo, hhi, float((inter > 0).mean())), flush=True)

    sns.set(font_scale=1.6, style='white')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    posterior_panel(ax1, dp, r'$\beta$ RT (delayed planning)')
    posterior_panel(ax2, inter, r'$\beta$ RT x Time (interaction)')
    fig.suptitle('Simulated RT LMM, soft-gated model (20 subjects)', y=1.01)
    plt.tight_layout()
    plt.savefig('rt_lmm_simulated_softgate_posterior.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('Saved rt_lmm_simulated_softgate_posterior.png', flush=True)
    print('S6 DONE', flush=True)


if __name__ == '__main__':
    main()
