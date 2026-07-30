"""
Decision time as the number of MBMC planning rollouts -- EMPIRICAL-MEDIAN version.

Same rollout read-out as mbmc_rollout_rt_simulation.py (RT == number of planning
rollouts the model expends at each decision), but the model parameters are the
across-subject MEDIANS of the hierarchical-EM fit to the real data
(em_params_{study}_MBMC.npy), rather than hand-set values:

    MB_CONTROL = median(beta_MBMC)   DISCOUNT = median(gamma_d)
    BREADTH1   = median(b1)          BREADTH2 = median(b2)      CHOICE_BIAS = median(beta_CB)

Rollouts at a decision are the breadth values read as the PROPORTION of a full
rollout searched (rollouts_action1 = BREADTH1 * total1, etc.), driving the
hypergeometric planning-success probabilities exactly as in the fitting model.
Meta-control: plan at the earliest controlled decision (spend rollouts), execute
later (0 rollouts), re-plan each trial; a relinquished decision is cached (0
rollouts thereafter) -- so planning migrates to the initiation point with
experience and the delayed-planning RT signature emerges.
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import comb, softmax

mb_key = {
    (3, 1, 'start'): [1, 8], (3, 2, 'toothbrush'): [1, 4], (3, 3, 'car'): [1, 2],
    (2, 1, 'start'): [2, 8], (2, 2, 'toothbrush'): [1, 4], (2, 3, 'backpack'): [1, 2],
    (1, 1, 'start'): [4, 8], (1, 2, 'toothbrush'): [2, 4], (1, 3, 'backpack'): [1, 2],
}
mb_key2 = {
    (3, 1, 'start'): [0, 0], (3, 2, 'toothbrush'): [0, 0], (3, 3, 'car'): [0, 0],
    (2, 1, 'start'): [1, 4], (2, 2, 'toothbrush'): [0, 0], (2, 3, 'backpack'): [0, 0],
    (1, 1, 'start'): [2, 4], (1, 2, 'toothbrush'): [1, 2], (1, 3, 'backpack'): [0, 0],
}
PATH = {3: ['start', 'toothbrush', 'car'],
        2: ['start', 'toothbrush', 'backpack'],
        1: ['start', 'toothbrush', 'backpack']}
INITIATION = {3: 1, 2: 2, 1: 3}
N_TRIALS = 20
N_AGENTS = 10000
PNAMES = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache', 'CB',
          'forget', 'cache_reward', 'cache_plan']


TOP_FRAC = 0.10   # use only the top 10% of subjects by fitted breadth2 (b2)


def median_params(study):
    R = np.load(f'em_params_{study}_MBMC.npy')
    b2 = R[:, PNAMES.index('breadth2')]
    b1 = R[:, PNAMES.index('MB_breadth')]
    thr = np.quantile(b2, 1 - TOP_FRAC)         # 90th percentile of b2
    thr2 = np.quantile(b1, 1 - TOP_FRAC)   
    sel = (b2 >= thr) & (b1 >= thr2)                             # top 10% performers by breadth2
    m = dict(zip(PNAMES, np.median(R[sel], 0)))    # MEAN within the selected subjects
    print('[%s] top %d%% performing subjects'
          % (study, int(TOP_FRAC * 100)))
    return dict(MB_CONTROL=m['MB_B'], DISCOUNT=m['MB_depth'],
                BREADTH1=m['MB_breadth'], BREADTH2=m['breadth2'], CHOICE_BIAS=m['CB'])


def p_success(succ, total, draws):
    if succ <= 0 or total <= 0:
        return 0.0
    failures = total - succ
    if draws <= failures:
        return 1.0 - comb(failures, draws, exact=False) / comb(total, draws, exact=False)
    return 1.0


def values(goal, decision, one_ok, two_ok, disc):
    d = 4 * (disc ** (3 - decision))
    v_take, v_rel = 0.0, 0.0
    if goal == 3:
        v_take, v_rel = (d, 1.0) if one_ok else (0.0, 1.0)
    elif goal == 2:
        if decision == 1:
            if two_ok:
                v_take, v_rel = d, 1.0 + d
            elif one_ok:
                v_take, v_rel = d, 1.0
            else:
                v_rel = 1.0
        else:
            v_take, v_rel = (d, 1.0) if one_ok else (0.0, 1.0)
    elif goal == 1:
        if decision < 3:
            if two_ok:
                v_take, v_rel = d, 1.0 + d
            elif one_ok:
                v_take, v_rel = d, 1.0
            else:
                v_rel = 1.0
        else:
            v_take, v_rel = (d, 1.0) if one_ok else (0.0, 1.0)
    return v_take, v_rel


def simulate_goal(goal, rng, P):
    exp1 = {d: 0.0 for d in (1, 2, 3)}
    exp2 = {d: 0.0 for d in (1, 2, 3)}
    relinquish_cached = {d: False for d in (1, 2, 3)}
    out = np.zeros((N_TRIALS, 3))
    for t in range(N_TRIALS):
        control_taken = False
        for d in (1, 2, 3):
            state = PATH[goal][d - 1]
            succ1, total1 = mb_key[(goal, d, state)]
            succ2, total2 = mb_key2[(goal, d, state)]
            if control_taken or relinquish_cached[d]:
                out[t, d - 1] = 0.0
                continue
            r1 = P['BREADTH1'] * total1 if succ1 > 0 else 0.0
            r2 = P['BREADTH2'] * total2 if succ2 > 0 else 0.0
            out[t, d - 1] = r1 + r2
            exp1[d] += r1
            exp2[d] += r2
            p_one = p_success(succ1, total1, exp1[d])
            p_two = p_success(succ2, total2, exp2[d])
            one_ok = rng.random() < p_one * (1 - p_two)
            two_ok = rng.random() < p_one * p_two
            v_take, v_rel = values(goal, d, one_ok, two_ok, P['DISCOUNT'])
            q = np.array([v_take * P['MB_CONTROL'] + P['CHOICE_BIAS'],
                          v_rel * P['MB_CONTROL']])
            if rng.random() < softmax(q)[0]:
                control_taken = True
            else:
                relinquish_cached[d] = True
    return out


def run(P):
    rng = np.random.default_rng(0)
    rows = []
    for agent in range(N_AGENTS):
        for goal in (3, 2, 1):
            roll = simulate_goal(goal, rng, P)
            for t in range(N_TRIALS):
                for d in (1, 2, 3):
                    rows.append({'agent': agent, 'planning_depth': goal,
                                 'trial_num_within_goal': t + 1, 'decision': d,
                                 'RT_rollouts': roll[t, d - 1]})
    return pd.DataFrame(rows)


TAG = 'top10b2_mean'


def make_figure(study):
    P = median_params(study)
    df = run(P)
    df.to_csv(f'mbmc_simulated_RT_over_time_median_{TAG}_{study}.csv', index=False)
    print('[%s] EM-mean params (top group): MB_CONTROL=%.2f DISCOUNT=%.2f BREADTH1=%.2f '
          'BREADTH2=%.2f CHOICE_BIAS=%.2f' % (study, P['MB_CONTROL'], P['DISCOUNT'],
          P['BREADTH1'], P['BREADTH2'], P['CHOICE_BIAS']))
    for goal in (3, 2, 1):
        g = df[df['planning_depth'] == goal]
        early = g[g['trial_num_within_goal'] <= 5].groupby('decision')['RT_rollouts'].mean()
        late = g[g['trial_num_within_goal'] > 15].groupby('decision')['RT_rollouts'].mean()
        print('  depth %d (initiate d%d): early %s -> late %s'
              % (goal, INITIATION[goal], [round(early[d], 2) for d in (1, 2, 3)],
                 [round(late[d], 2) for d in (1, 2, 3)]))

    means = (df.groupby(['planning_depth', 'decision', 'trial_num_within_goal'])
             ['RT_rollouts'].mean().reset_index())
    sns.set(style='white', font_scale=1.4, palette='Set2')
    fig, axes = plt.subplots(1, 3, figsize=(17, 5.2), sharey=True)
    palette = {1: '#4C72B0', 2: '#DD8452', 3: '#55A868'}
    for ax, goal in zip(axes, (3, 2, 1)):
        sub = means[means['planning_depth'] == goal]
        init = INITIATION[goal]
        for d in (1, 2, 3):
            s = sub[sub['decision'] == d]
            ax.plot(s['trial_num_within_goal'], s['RT_rollouts'], marker='o', ms=4,
                    color=palette[d], lw=3.2 if d == init else 1.6,
                    label=f'decision {d}' + (' (initiate)' if d == init else ''))
        ax.set_title(f'planning depth {goal}  (initiate at d{init})')
        ax.set_xlabel('trial (within goal)')
        ax.set_xticks([1, 5, 10, 15, 20])
        ax.legend(fontsize=11)
    axes[0].set_ylabel('Decision Time as Planning Rollouts')
    fig.suptitle('MBMC-simulated Decision Time as planning rollouts for top-performing subjects', y=1.02)
    plt.tight_layout()
    fig.savefig(f'mbmc_simulated_RT_over_time_median_{TAG}_{study}.png', dpi=300,
                bbox_inches='tight')
    plt.close(fig)
    print(f'  saved mbmc_simulated_RT_over_time_median_{TAG}_{study}.png')


if __name__ == '__main__':
    for study in ('study2', 'study1'):
        make_figure(study)
