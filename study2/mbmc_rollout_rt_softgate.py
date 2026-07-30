"""
Decision time as planning rollouts under the SOFT-GATED + tailored-saturation model,
at the fitted Study-2 parameters (em_params_study2_MBMCgatedsoft.npy).

Time model (decomposed, as in mbmc_rollout_rt_decomposed.py):
  * META-PLANNING (transient):
      - first search: min(b1*8, unexplored N1) per visit, off once saturated;
        urns are STATE-TAILORED (subtree wherever the goal is reachable via both
        actions): N1 = 8,4,2 by decision except (2,1):4, (1,1):4, (1,2):2.
      - second search: SOFT-GATED -- engages in proportion to p1:
        cost = p1 * min(b2*4, unexplored N2); off at saturation/exhaustion.
  * PLANNING proper (recurrent): min(b1*8, N1) at every actively-engaged decision
    (until the meta-decision to relinquish is cached).
  * Cached relinquish (outcome-gated: consolidated only if the goal was reached)
    and plan execution: 0 rollouts.
  Choices: nested categorical outcome (w2 = p1*p2), model values + softmax.
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import comb, softmax

import mbmc_rollout_rt_median as BASE   # values(), INITIATION, plotting conventions

INITIATION = BASE.INITIATION
N_TRIALS, N_AGENTS = 20, 163
TAG = 'softgate_mean'
PN = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache', 'CB',
      'forgetC', 'cache_reward', 'cache_plan']
TOP_FRAC = 0.10

# state-tailored urns on the canonical path, keyed (goal, decision)
URN1 = {(3, 1): (1, 8), (3, 2): (1, 4), (3, 3): (1, 2),
        (2, 1): (1, 4), (2, 2): (1, 4), (2, 3): (1, 2),
        (1, 1): (2, 4), (1, 2): (1, 2), (1, 3): (1, 2)}
URN2 = {(2, 1): (1, 4), (1, 1): (2, 4), (1, 2): (1, 2)}


def params(study='study2'):
    R = np.load(f'em_params_{study}_MBMCgatedsoft.npy')
    m = dict(zip(PN, np.mean(R, 0)))                 # MEAN across all subjects
    print(f'[{study}] soft-gated fit, all-subject MEANS (n={len(R)}): '
          f'MB_CONTROL={m["MB_B"]:.2f} DISCOUNT={m["MB_depth"]:.2f} '
          f'B1={m["MB_breadth"]:.2f} B2={m["breadth2"]:.2f} CB={m["CB"]:.2f}')
    return dict(MB_CONTROL=m['MB_B'], DISCOUNT=m['MB_depth'],
                B1=m['MB_breadth'], B2=m['breadth2'], CB=m['CB'])


def p_success(succ, total, draws):
    if succ <= 0 or total <= 0:
        return 0.0
    failures = total - succ
    if draws <= failures:
        return 1.0 - comb(failures, draws, exact=False) / comb(total, draws, exact=False)
    return 1.0


def simulate_goal(goal, rng, P):
    d1_budget, d2_budget = P['B1'] * 8.0, P['B2'] * 4.0
    exp1 = {d: 0.0 for d in (1, 2, 3)}
    exp2 = {d: 0.0 for d in (1, 2, 3)}
    relinquish_cached = {d: False for d in (1, 2, 3)}
    meta = np.zeros((N_TRIALS, 3))
    plan = np.zeros((N_TRIALS, 3))
    for t in range(N_TRIALS):
        control_taken = False
        goal_alive = True
        relinquished_now = []
        for d in (1, 2, 3):
            succ1, N1 = URN1[(goal, d)]
            succ2, N2 = URN2.get((goal, d), (0, 0))
            safe = succ2 > 0
            if control_taken:
                continue
            if relinquish_cached[d]:
                relinquished_now.append(d)
                if not safe and rng.random() < 0.5:
                    goal_alive = False
                continue
            # meta-planning: first search (until saturated) ...
            sat1 = exp1[d] > (N1 - succ1)
            m1 = 0.0 if sat1 else min(d1_budget, max(0.0, N1 - exp1[d]))
            exp1[d] += m1
            p1 = p_success(succ1, N1, exp1[d])
            # ... plus SOFT-GATED second search, engaged in proportion to p1
            sat2 = succ2 > 0 and exp2[d] > (N2 - succ2)
            m2 = 0.0 if (succ2 <= 0 or sat2) else p1 * min(d2_budget,
                                                           max(0.0, N2 - exp2[d]))
            exp2[d] += m2
            p2 = p_success(succ2, N2, exp2[d])
            meta[t, d - 1] = m1 + m2
            # planning proper: every actively-engaged visit
            plan[t, d - 1] = min(d1_budget, N1)
            w_two = p1 * p2
            w_one = p1 * (1.0 - w_two)
            u = rng.random()
            two_ok = u < w_two
            one_ok = (not two_ok) and (u < w_two + w_one)
            v_take, v_rel = BASE.values(goal, d, one_ok, two_ok, P['DISCOUNT'])
            q = np.array([v_take * P['MB_CONTROL'] + P['CB'],
                          v_rel * P['MB_CONTROL']])
            if rng.random() < softmax(q)[0]:
                control_taken = True
            else:
                relinquished_now.append(d)
                if not safe and rng.random() < 0.5:
                    goal_alive = False
        for d in relinquished_now:
            relinquish_cached[d] = bool(goal_alive)
    return meta, plan


def main():
    P = params()
    rng = np.random.default_rng(0)
    rows = []
    for agent in range(N_AGENTS):
        for goal in (3, 2, 1):
            meta, plan = simulate_goal(goal, rng, P)
            for t in range(N_TRIALS):
                for d in (1, 2, 3):
                    rows.append({'agent': agent, 'planning_depth': goal,
                                 'trial_num_within_goal': t + 1, 'decision': d,
                                 'meta_rollouts': meta[t, d - 1],
                                 'plan_rollouts': plan[t, d - 1]})
    df = pd.DataFrame(rows)
    df['total_rollouts'] = df['meta_rollouts'] + df['plan_rollouts']
    df.to_csv(f'mbmc_simulated_RT_{TAG}_study2.csv', index=False)

    m = (df.groupby(['planning_depth', 'decision', 'trial_num_within_goal'])
         [['total_rollouts', 'meta_rollouts', 'plan_rollouts']].mean().reset_index())
    sns.set(style='white', font_scale=1.35, palette='Set2')
    fig, axes = plt.subplots(3, 3, figsize=(17, 13.8), sharex=True, sharey=True)
    palette = {1: '#4C72B0', 2: '#DD8452', 3: '#55A868'}
    ROWS = [('total_rollouts', 'Total planning rollouts\n(meta-planning + planning)'),
            ('meta_rollouts', 'Meta-planning rollouts'),
            ('plan_rollouts', 'Planning rollouts')]
    for col, goal in enumerate((3, 2, 1)):
        init = INITIATION[goal]
        for row, (comp, label) in enumerate(ROWS):
            ax = axes[row, col]
            sub = m[m['planning_depth'] == goal]
            for d in (1, 2, 3):
                s = sub[sub['decision'] == d]
                ax.plot(s['trial_num_within_goal'], s[comp], marker='o', ms=4,
                        color=palette[d], lw=3.2 if d == init else 1.6,
                        label=f'decision {d}' + (' (initiate)' if d == init else ''))
            if row == 0:
                ax.set_title(f'planning depth {goal}  (initiate at d{init})')
                ax.legend(fontsize=11)
            if row == len(ROWS) - 1:
                ax.set_xlabel('trial (within goal)')
            if col == 0:
                ax.set_ylabel(label)
            ax.set_xticks([1, 5, 10, 15, 20])
    fig.suptitle('MBMC decision time under the soft-gated model: total (top), '
                 'meta-planning (middle), planning (bottom) — Study 2', y=1.0)
    plt.tight_layout()
    fig.savefig(f'mbmc_simulated_RT_{TAG}_study2.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    for goal in (3, 2, 1):
        g = df[df['planning_depth'] == goal]
        early = g[g['trial_num_within_goal'] <= 5].groupby('decision')['total_rollouts'].mean()
        late = g[g['trial_num_within_goal'] > 15].groupby('decision')['total_rollouts'].mean()
        print('  depth %d (init d%d) TOTAL: early %s -> late %s'
              % (goal, INITIATION[goal], [round(early[d], 2) for d in (1, 2, 3)],
                 [round(late[d], 2) for d in (1, 2, 3)]))
    print(f'saved mbmc_simulated_RT_{TAG}_study2.png')


if __name__ == '__main__':
    main()
