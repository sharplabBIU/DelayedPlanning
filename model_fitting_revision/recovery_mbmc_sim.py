"""
Generative MBMC simulator for parameter recovery, matched EXACTLY to the CBM
likelihood `cbm_models.mbmc_loglik` (same task graph, value logic, caching,
cache-plan bonus, and recency forgetting; path-format states).

Common random numbers (per subject)
-----------------------------------
Every stochastic event of a subject -- the planning-search outcome (two-step /
one-step / fail), the take-vs-relinquish choice, and the state transition that
follows a relinquish -- is drawn from a single fixed per-subject random stream.
Because the generative model draws the planning outcome from exactly the 3-way
mixture that the CBM likelihood marginalises, and the realised trajectory (the
states that follow each relinquish) is recorded and conditioned on at fit time,
the randomness a subject "experiences" during generation is the same randomness
their data carries when it is fit: given the same relinquish choice, the same
transition was realised. Fixing the per-subject seed makes generation a
deterministic function of (parameters, seed).
"""
import numpy as np
from scipy.special import comb, logsumexp

# ---- task graph (path-format states, matching mbmc_loglik) ---------------------
mb_key = {
    (3, 1, 'start'): [1, 8], (3, 2, 'images/toothbrush.png'): [1, 4],
    (3, 2, 'images/baby.png'): [0, 0], (3, 3, 'images/car.png'): [1, 2],
    (3, 3, 'images/backpack.png'): [0, 0], (3, 3, 'images/bowtie.png'): [0, 0],
    (2, 1, 'start'): [2, 8], (2, 2, 'images/toothbrush.png'): [1, 4],
    (2, 2, 'images/baby.png'): [1, 4], (2, 3, 'images/backpack.png'): [1, 2],
    (2, 3, 'images/bowtie.png'): [0, 0], (2, 3, 'images/car.png'): [0, 0],
    (1, 1, 'start'): [4, 8], (1, 2, 'images/toothbrush.png'): [2, 4],
    (1, 2, 'images/baby.png'): [2, 4], (1, 3, 'images/backpack.png'): [1, 2],
    (1, 3, 'images/bowtie.png'): [1, 2], (1, 3, 'images/car.png'): [1, 2],
}
mb_key2 = {
    (3, 1, 'start'): [0, 0], (2, 1, 'start'): [1, 4], (1, 1, 'start'): [2, 4],
    (1, 2, 'images/toothbrush.png'): [1, 2], (1, 2, 'images/baby.png'): [1, 2],
}
transitions = {   # state -> [child0, child1]
    'start': ['images/toothbrush.png', 'images/baby.png'],
    'images/toothbrush.png': ['images/backpack.png', 'images/car.png'],
    'images/baby.png': ['images/bowtie.png', 'images/backpack.png'],
    'images/backpack.png': ['images/lamp.png', 'images/zebra.png'],
    'images/bowtie.png': ['images/knight.png', 'images/lamp.png'],
    'images/car.png': ['images/lamp.png', 'images/cat.png'],
}
# child indices that keep the goal reachable (for take-control + successful plan)
goalward = {
    (3, 'start'): [0], (3, 'images/toothbrush.png'): [1], (3, 'images/car.png'): [1],
    (2, 'start'): [0, 1], (2, 'images/toothbrush.png'): [0], (2, 'images/baby.png'): [1],
    (2, 'images/backpack.png'): [1],
    (1, 'start'): [0, 1], (1, 'images/toothbrush.png'): [0, 1],
    (1, 'images/baby.png'): [0, 1], (1, 'images/backpack.png'): [0],
    (1, 'images/bowtie.png'): [1], (1, 'images/car.png'): [0],
}
GOAL_LANDMARK = {3: 'images/cat.png', 2: 'images/zebra.png', 1: 'images/lamp.png'}
MBMC_PARAMS = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache',
               'CB', 'forgetC', 'cache_reward', 'cache_plan']


def _p_success(succ, total, draws):
    if succ <= 0 or total <= 0:
        return 0.0
    failures = total - succ
    if draws <= failures:
        return 1.0 - comb(failures, draws, exact=False) / comb(total, draws, exact=False)
    return 1.0


def _values(goal, decision, one_ok, two_ok, disc):
    R = 4 * (disc ** (3 - decision))
    vt = vr = 0.0
    if two_ok and ((goal == 2 and decision == 1) or (goal == 1 and decision < 3)):
        vt, vr = R, 1 + R          # two-step relinquish beats take
    elif one_ok or two_ok:
        vt, vr = R, 1.0            # one-step plan -> take
    else:
        vt, vr = 0.0, 1.0          # fail -> relinquish
    return np.array([vt, vr])


def simulate_subject(native, depth_scaffold, seed):
    """native: 9 params in MBMC_PARAMS order. Returns list-of-dict rows (CBM format)."""
    rng = np.random.default_rng(seed)
    (mb_control, discount, b1, b2, mb_cache, choice_bias,
     forgetC, cache_reward, cache_plan) = native
    mb_breadth, mb_breadth2 = b1 * 8, b2 * 4

    keys = list(mb_key.keys())
    cached = {k: np.zeros(2) for k in keys}
    exp1 = {k: 0.0 for k in keys}
    exp2 = {k: 0.0 for k in keys}
    cache_plans = {(g, d): np.zeros(2) for g in (1, 2, 3) for d in (1, 2, 3)}
    recent = {1: [], 2: [], 3: []}

    rows = []
    for t, goal in enumerate(depth_scaffold):
        goal = int(goal)
        state = 'start'
        trial_keys = []
        trial_rows = []
        for decision in (1, 2, 3):
            key = (goal, decision, state)
            s1, tot1 = mb_key[key]
            s2, tot2 = mb_key2.get(key, [0, 0])
            if s1 > 0:
                exp1[key] += mb_breadth
            if s2 > 0:
                exp2[key] += mb_breadth2
            p_one = _p_success(s1, tot1, exp1[key])
            p_two = _p_success(s2, tot2, exp2[key])
            w_two = p_one * p_two
            w_one = p_one * (1 - w_two)
            w_fail = max(0.0, 1 - w_one - w_two)
            # planning-search outcome (CRN)
            u = rng.random() * (w_two + w_one + w_fail)
            if u < w_two:
                one_ok, two_ok, success = False, True, True
            elif u < w_two + w_one:
                one_ok, two_ok, success = True, False, True
            else:
                one_ok, two_ok, success = False, False, False
            val = _values(goal, decision, one_ok, two_ok, discount)

            Q = val * mb_control + cached[key] + np.array([choice_bias, 0.0]) \
                + cache_plans[(goal, decision)]
            p_rel = np.exp(Q[1] - logsumexp(Q))         # P(act==1, relinquish)
            act = 1 if rng.random() < p_rel else 0      # 0=take control, 1=relinquish

            if decision < 3:
                cache_plans[(goal, decision + 1)] = np.array(
                    [cache_plan if act == 0 else 0.0, 0.0])

            trial_rows.append(dict(trial_num=t, planning_depth=goal,
                                   decision=decision, current_state=state,
                                   choice_numeric=act))
            trial_keys.append((key, act))

            # Transition with common random numbers that hold ONLY when the control
            # decision is equivalent: draw a node-fixed environment uniform u_env
            # (independent of the take/relinquish choice). Relinquishing (or a failed
            # plan) lands on the child selected by u_env -- so any model that also
            # relinquishes here lands identically. Taking control lands on the planned
            # (goal-ward) child -- a different branch, i.e. the outcome is not shared
            # with the relinquish case. u_env is stored so the environment realisation
            # is a fixed property of the (subject, trial, decision).
            u_env = rng.random()
            children = transitions[state]
            if act == 0 and success:
                gw = goalward.get((goal, state), [0, 1])
                nxt = children[gw[int(u_env * len(gw)) % len(gw)]]
            else:
                nxt = children[0 if u_env < 0.5 else 1]
            state = nxt

        got = int(state == GOAL_LANDMARK[goal])
        for r in trial_rows:
            r['got_to_goal'] = got
        rows.extend(trial_rows)

        # cache updates (after outcome known; different keys -> no within-trial leak)
        signed = got if got == 1 else -1
        for (key, act) in trial_keys:
            cached[key][act] = mb_cache + cache_reward * signed
            tup = (*key, act)
            lvl = key[1]
            recent[lvl] = [k for k in recent[lvl] if k != tup] + [tup]
        # recency forgetting over ALL cache entries (match mbmc_loglik exactly)
        for lvl in (1, 2, 3):
            rec_idx = {k: r for r, k in enumerate(reversed(recent[lvl]))}
            far = len(recent[lvl]) + 1
            for key in keys:
                if key[1] != lvl:
                    continue
                for act in (0, 1):
                    rec = rec_idx.get((*key, act), far)
                    cached[key][act] *= np.exp(-forgetC * rec)
    return rows
