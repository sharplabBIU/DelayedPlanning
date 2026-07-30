#!/usr/bin/env python
# coding: utf-8
"""
cbm_models.py  --  Revision-1 model set, fit with Piray's CBM (cbm_python)
==========================================================================

This module re-implements the model space of `model_fitting.py` for the
*delayed-planning / meta-control* task using the Computational and Behavioural
Modelling toolbox (CBM, Payam Piray; python port `cbm`), in place of the
in-house hierarchical Expectation-Maximisation (iterative importance sampling)
procedure.

It contains:

  1. `mbmc_loglik`   -- the winning Cache-MC + Replan model (MBMC), ported
                        verbatim from `model_fitting.py`
                        (`MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution`).
                        9 parameters. Has *in-trial sampling* and *caching/forgetting*,
                        which is what produces the learning dynamics.

  2. `sr_loglik`     -- NEW. A successor-representation (SR) meta-controller.
  3. `pr_loglik`     -- NEW. A predecessor-representation (PR) meta-controller
                        (Sharp & Eldar, 2024).

     Both the SR and PR controllers form their map *offline, before the planning
     phase*: goal reachability is read off a representation computed once over
     the task graph under a random policy.  SR = forward goal reachability
     rho^SR(a) = P(reach goal | heading to a); PR = its Bayes inverse, the
     retrospective posterior P(originated via a | goal reached) = rho^SR(a)/sum.
     They take or relinquish control by the heuristic the reviewer proposed:
     "if the likelihood of reaching the goal state is (nearly) equal for both
      actions, relinquish / don't plan".
     Crucially they are *static* across trials (no in-trial sampling, no
     learning), so they cannot reproduce the trial-by-trial learning dynamics.

  4. `cb_loglik`     -- a control-bias-only baseline (1 parameter), to anchor the
                        evidence scale (this is the `CB` model of the paper).

All likelihood functions follow the SAME observation model as the EM code: at
each of the 3 decisions per trial the agent makes a binary meta-control choice
`choice_numeric` (0 = take control [left/right], 1 = relinquish [space]); the
log-likelihood is the summed log-probability of the observed choices.

------------------------------------------------------------------------------
CBM interface
------------------------------------------------------------------------------
CBM calls `model(parameters, subject_data) -> scalar log-likelihood`, where
`parameters` is an *unconstrained* real vector.  Each `*_cbm` wrapper below
transforms the unconstrained parameters into the native (constrained) parameter
space used by the likelihood:

    'pos'  : positive   (EM `gamma`)  -> exp(x)
    'unit' : in (0,1)   (EM `beta`)   -> sigmoid(x)
    'real' : real       (EM `norm`)   -> x

and returns the summed log-likelihood for that subject.
"""

import numpy as np
import pandas as pd
from scipy.special import logsumexp, comb, expit


# ============================================================================
#  Task graph (shared by SR / PR controllers)
# ============================================================================
# Real (non-"space") transitions of the task.  At every state the participant
# can take control (choose one of the two children = left/right) or relinquish
# control ("space").  Terminal landmarks live at depth 3.
REAL_TRANSITIONS = {
    'start':      ['toothbrush', 'baby'],
    'toothbrush': ['backpack', 'car'],
    'baby':       ['bowtie', 'backpack'],
    'backpack':   ['lamp', 'zebra'],
    'bowtie':     ['knight', 'lamp'],
    'car':        ['lamp', 'cat'],
}
TERMINALS = ['lamp', 'zebra', 'knight', 'cat']
ALL_NODES = ['start', 'toothbrush', 'baby', 'backpack', 'car', 'bowtie',
             'lamp', 'zebra', 'knight', 'cat']

# `current_state` in the data is stored as an image path for non-start states.
STATE_TO_NODE = {
    'start': 'start',
    'images/toothbrush.png': 'toothbrush',
    'images/baby.png': 'baby',
    'images/backpack.png': 'backpack',
    'images/car.png': 'car',
    'images/bowtie.png': 'bowtie',
}

# Required-planning-depth -> instructed goal landmark.
# Verified against the EM `mb_key` reachability counts:
#   from `start`, P(random path reaches cat)=1/8 (depth 3),
#                 P(reaches zebra)=2/8 (depth 2), P(reaches lamp)=4/8 (depth 1).
DEPTH_TO_GOAL = {3: 'cat', 2: 'zebra', 1: 'lamp'}

# pre-compute parents (for the PR / backward representation)
PARENTS = {n: [] for n in ALL_NODES}
for _s, _ch in REAL_TRANSITIONS.items():
    for _c in _ch:
        PARENTS[_c].append(_s)


def _forward_reach(goal, gamma):
    """Successor-representation goal reachability.

    reach[s] = E[ gamma^(steps) * 1(absorbed at goal) | start at s, random policy ]
    i.e. the discounted probability that a random forward walk from state `s`
    reaches the goal landmark.  With gamma=1 this equals num_success/total
    (the EM `mb_key` counts).  This is the quantity an SR formed by forward
    replay under a random policy makes available offline.
    """
    reach = {n: 0.0 for n in ALL_NODES}
    reach[goal] = 1.0
    # solve by recursion over the (acyclic) graph, deepest states first
    order = ['backpack', 'car', 'bowtie',          # depth-2 states
             'toothbrush', 'baby',                  # depth-1 states
             'start']                               # depth-0 state
    for s in order:
        ch = REAL_TRANSITIONS[s]
        reach[s] = gamma * 0.5 * (reach[ch[0]] + reach[ch[1]])
    return reach


def _reach_table(gamma):
    """Forward SR goal-reachability rho^SR_g(s) for every goal g and state s.

    rho^SR_g(s) = P(a random-policy walk from s reaches goal landmark g)
                = (I - gamma P)^{-1}[s, g]  (terminals absorbing).
    Both controllers are built from this single offline forward representation;
    the PR controller reads it retrospectively (see `_child_readout`).
    """
    return {g: _forward_reach(g, gamma) for g in TERMINALS}


def _child_readout(kind, r1, r2):
    """Per-action decision quantity from the two children's forward reachability.

    SR : forward goal reachability of each child,
            rho^SR(a_k) = P(reach goal | heading to a_k).
    PR : the *predecessor / retrospective* representation -- the Bayes inverse of
         the SR -- i.e. the probability of having originated via child a_k given
         that the trajectory ends at the goal landmark g,
            P(a_k | reach g) = rho^SR(a_k) / (rho^SR(a1) + rho^SR(a2))
         (Sharp & Eldar, 2024).  Off-path states (neither child reaches g) give
         1/2 each.  On this task graph this coincides numerically with the
         reverse-random-walk occupancy, but is computed here as the posterior by
         definition.
    """
    if kind == 'SR':
        return r1, r2
    tot = r1 + r2
    if tot <= 0.0:
        return 0.5, 0.5
    return r1 / tot, r2 / tot


# ============================================================================
#  Parameter transforms  +  CBM wrapper factory
# ============================================================================
def _transform(raw, types):
    """unconstrained real vector -> native parameter list."""
    out = []
    for x, t in zip(raw, types):
        if t == 'pos':
            out.append(float(np.exp(np.clip(x, -20.0, 20.0))))
        elif t == 'unit':
            out.append(float(expit(x)))
        else:  # 'real'
            out.append(float(x))
    return out


class CBMModel:
    """A *picklable* CBM-compatible model: `model(parameters, data) -> scalar`.

    (Picklability matters because CBM stores the model functions inside the
    saved HBIResult; closures would break the pickle.)

    `native_loglik` is either
      * a `samples`-interface likelihood (kind='samples'): signature
        `f(samples, data, rng_samples)` returning a vector (evaluated with a
        single parameter sample), or
      * a native scalar likelihood (kind='scalar'): signature
        `f(params_list, data)` returning a scalar.
    """

    def __init__(self, native_loglik, types, kind='samples'):
        self.native_loglik = native_loglik
        self.types = types
        self.kind = kind

    def __call__(self, parameters, data):
        params = _transform(np.asarray(parameters, dtype=float).ravel(), self.types)
        try:
            if self.kind == 'samples':
                samples = [np.array([p], dtype=float) for p in params]
                ll = self.native_loglik(samples, data, np.array([0]))
                ll = float(np.asarray(ll).ravel()[0])
            else:
                ll = float(self.native_loglik(params, data))
        except Exception:
            return -1.0e6
        if not np.isfinite(ll):
            return -1.0e6
        return ll


def make_cbm_model(native_loglik, types, kind='samples'):
    return CBMModel(native_loglik, types, kind)


# ============================================================================
#  Model 1 -- MBMC (winning model), ported verbatim from model_fitting.py
#  9 params: MB_B, MB_depth, MB_breadth, breadth2, mbcache, CB, forgetC,
#            cache_reward, cache_plan
# ============================================================================
MBMC_PARAMS = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache',
               'CB', 'forgetC', 'cache_reward', 'cache_plan']
MBMC_TYPES = ['pos', 'unit', 'unit', 'unit', 'pos', 'real', 'pos', 'real', 'pos']


def mbmc_loglik(samples, data, rng_samples):
    np.seterr(divide='ignore')
    sample_size = len(rng_samples)

    # extract parameters
    mb_control = samples[0][rng_samples]
    discount_rate = samples[1][rng_samples]
    mb_breadth = samples[2][rng_samples] * 8
    mb_breadth2 = samples[3][rng_samples] * 4
    mb_cache = samples[4][rng_samples]
    choice_bias = samples[5][rng_samples]
    forgetting_cache = samples[6][rng_samples]
    cache_reward = samples[7][rng_samples]
    cache_plan = samples[8][rng_samples]

    lik = np.zeros(sample_size)

    mb_key = {
        (3, 1, 'start'): [1, 8],
        (3, 2, 'images/toothbrush.png'): [1, 4],
        (3, 2, 'images/baby.png'): [0, 0],
        (3, 3, 'images/car.png'): [1, 2],
        (3, 3, 'images/backpack.png'): [0, 0],
        (3, 3, 'images/bowtie.png'): [0, 0],
        (2, 1, 'start'): [2, 8],
        (2, 2, 'images/toothbrush.png'): [1, 4],
        (2, 2, 'images/baby.png'): [1, 4],
        (2, 3, 'images/backpack.png'): [1, 2],
        (2, 3, 'images/bowtie.png'): [0, 0],
        (2, 3, 'images/car.png'): [0, 0],
        (1, 1, 'start'): [4, 8],
        (1, 2, 'images/toothbrush.png'): [2, 4],
        (1, 2, 'images/baby.png'): [2, 4],
        (1, 3, 'images/backpack.png'): [1, 2],
        (1, 3, 'images/bowtie.png'): [1, 2],
        (1, 3, 'images/car.png'): [1, 2],
    }
    mb_key2 = {
        (3, 1, 'start'): [0, 0],
        (3, 2, 'images/toothbrush.png'): [0.0, 0],
        (3, 2, 'images/baby.png'): [0.0, 0],
        (3, 3, 'images/car.png'): [0.0, 0],
        (3, 3, 'images/backpack.png'): [0, 0],
        (3, 3, 'images/bowtie.png'): [0, 0],
        (2, 1, 'start'): [1, 4],
        (2, 2, 'images/toothbrush.png'): [0.0, 0],
        (2, 2, 'images/baby.png'): [0.0, 0],
        (2, 3, 'images/backpack.png'): [0.0, 0],
        (2, 3, 'images/bowtie.png'): [0, 0],
        (2, 3, 'images/car.png'): [0, 0],
        (1, 1, 'start'): [2, 4],
        (1, 2, 'images/toothbrush.png'): [1, 2],
        (1, 2, 'images/baby.png'): [1, 2],
        (1, 3, 'images/backpack.png'): [0, 0],
        (1, 3, 'images/bowtie.png'): [0, 0],
        (1, 3, 'images/car.png'): [0, 0],
    }

    cache_plans = {(g, d): np.zeros((sample_size, 2))
                   for g in (1, 2, 3) for d in (1, 2, 3)}

    keys = list(mb_key.keys())
    cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
    keys_caching = {(*k, s): np.zeros((sample_size, 2)) for k in keys for s in (0, 1)}

    choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
    for key in keys:
        choice_biases[key][:, 0] = choice_bias

    experiences_action1 = {key: np.zeros(sample_size) for key in keys}
    experiences_action2 = {key: np.zeros(sample_size) for key in keys}

    probability_mb1 = {key: np.zeros(sample_size) for key in keys}
    optimal_policy_1 = {key: np.zeros((sample_size, 2)) for key in keys}
    probability_mb2 = {key: np.zeros(sample_size) for key in keys}
    optimal_policy_2 = {key: np.zeros((sample_size, 2)) for key in keys}
    probability_mb_none = {key: np.zeros(sample_size) for key in keys}
    optimal_policy_3 = {key: np.zeros((sample_size, 2)) for key in keys}

    def update_probability_planning_success(num_successes, total, draws):
        failures = total - num_successes
        p_no_success = np.zeros_like(draws, dtype=float)
        mask = draws <= failures
        if np.any(mask):
            p_no_success[mask] = (comb(failures, draws[mask], exact=False) /
                                  comb(total, draws[mask], exact=False))
        return 1.0 - p_no_success

    def compute_mbmc_values_vectorized(key, mb_depth_array, mb_breadth_arr,
                                       mb_breadth_arr2, exp_arr, exp_arr2):
        num_success1, total1 = mb_key[key]
        num_success2, total2 = mb_key2[key]
        goal, decision, _ = key
        if num_success1 > 0:
            exp_arr = exp_arr + mb_breadth_arr
        if num_success2 > 0:
            exp_arr2 = exp_arr2 + mb_breadth_arr2

        if total1 > 0 and num_success1 > 0:
            p_one = update_probability_planning_success(num_success1, total1, exp_arr)
        else:
            p_one = np.zeros_like(exp_arr)
        if total2 > 0 and num_success2 > 0:
            p_two = update_probability_planning_success(num_success2, total2, exp_arr2)
        else:
            p_two = np.zeros_like(exp_arr2)

        p_one = np.minimum(p_one, 1)
        p_two = np.minimum(p_two, 1)
        p_two = p_one * p_two
        p_one = p_one * (1 - p_two)
        p_fail = 1 - (p_one + p_two)

        v2_take = np.zeros_like(p_one); v2_rel = np.zeros_like(p_one)
        v1_take = np.zeros_like(p_one); v1_rel = np.zeros_like(p_one)
        v0_take = np.zeros_like(p_one); v0_rel = np.zeros_like(p_one)

        if goal == 3:
            v2_take = 4 * (discount_rate ** (3 - decision)); v2_rel += 1
            v1_take = 4 * (discount_rate ** (3 - decision)); v1_rel += 1
            v0_rel += 1
        elif goal == 2:
            if decision == 1:
                v2_take = 4 * (discount_rate ** (3 - decision)); v2_rel = 1 + 4 * (discount_rate ** (3 - decision))
                v1_take = 4 * (discount_rate ** (3 - decision)); v1_rel += 1
                v0_rel += 1
            else:
                v2_take = 4 * (discount_rate ** (3 - decision)); v2_rel += 1
                v1_take = 4 * (discount_rate ** (3 - decision)); v1_rel += 1
                v0_rel += 1
        elif goal == 1:
            if decision < 3:
                v2_take = 4 * (discount_rate ** (3 - decision)); v2_rel = 1 + 4 * (discount_rate ** (3 - decision))
                v1_take = 4 * (discount_rate ** (3 - decision)); v1_rel += 1
                v0_rel += 1
            elif decision == 3:
                v2_take = 4 * (discount_rate ** (3 - decision)); v2_rel += 1
                v1_take = 4 * (discount_rate ** (3 - decision)); v1_rel += 1
                v0_rel += 1

        return (p_two, v2_take, v2_rel, p_one, v1_take, v1_rel, p_fail,
                v0_take, v0_rel, exp_arr, exp_arr2)

    def push_recent_key(recent_keys, key):
        try:
            recent_keys.remove(key)
        except ValueError:
            pass
        recent_keys.append(key)
        return recent_keys

    trials = np.sort(data['trial_num'].unique())
    recent_keys1 = []; recent_keys2 = []; recent_keys3 = []
    for trial in trials:
        df_temp = data[data['trial_num'] == trial].reset_index(drop=True)
        actions = df_temp['choice_numeric'].values
        goal_outcome = df_temp['got_to_goal'].values[0]
        planning_depth_val = int(df_temp['planning_depth'].values[0])
        current_states = df_temp['current_state'].values

        recent_acts = []; recent_other_acts = []
        for decision in (1, 2, 3):
            key = (planning_depth_val, decision, current_states[decision - 1])
            key_plan = (planning_depth_val, decision)

            (p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r,
             experiences_action1[key], experiences_action2[key]) = \
                compute_mbmc_values_vectorized(key, 5, mb_breadth, mb_breadth2,
                                               experiences_action1[key],
                                               experiences_action2[key])

            optimal_policy_1[key] = np.stack([v2t, v2r], axis=1)
            optimal_policy_2[key] = np.stack([v1t, v1r], axis=1)
            optimal_policy_3[key] = np.stack([v0t, v0r], axis=1)

            Q_both = (optimal_policy_1[key] * mb_control.reshape(sample_size, 1)
                      + cached_policy[key] + choice_biases[key] + cache_plans[key_plan])
            logp_both = (Q_both[np.arange(sample_size), actions[decision - 1]]
                         - logsumexp(Q_both, axis=1))

            Q_one = (optimal_policy_2[key] * mb_control.reshape(sample_size, 1)
                     + cached_policy[key] + choice_biases[key] + cache_plans[key_plan])
            logp_one = (Q_one[np.arange(sample_size), actions[decision - 1]]
                        - logsumexp(Q_one, axis=1))

            Q_none = (optimal_policy_3[key] * mb_control.reshape(sample_size, 1)
                      + cached_policy[key] + choice_biases[key] + cache_plans[key_plan])
            logp_none = (Q_none[np.arange(sample_size), actions[decision - 1]]
                         - logsumexp(Q_none, axis=1))

            eps2 = 1e-20
            p2 = np.where(p2 <= 0, eps2, p2)
            p1 = np.where(p1 <= 0, eps2, p1)
            p0 = np.where(p0 <= 0, eps2, p0)

            log_succ1 = np.log(p2) + logp_both
            log_succ2 = np.log(p1) + logp_one
            log_fail = np.log(p0) + logp_none

            log_mix = np.logaddexp(np.logaddexp(log_succ1, log_succ2), log_fail)
            lik += log_mix

            idx = np.arange(sample_size)
            act = actions[decision - 1]
            recent_acts.append(act)
            other_act = int((act - 1) * -1)
            recent_other_acts.append(other_act)

            if goal_outcome == 0:
                goal_outcome = -1
            cache_effect = mb_cache + (cache_reward * goal_outcome)
            cached_policy[key][idx, act] = cache_effect
            if decision < 3:
                key_plan_next = (planning_depth_val, decision + 1)
                if act == 0:
                    cache_plans[key_plan_next][:, 0] = cache_plan
                else:
                    cache_plans[key_plan_next][:, 0] = 0

            key = (planning_depth_val, decision, current_states[decision - 1], act)
            if decision == 1:
                recent_keys1 = push_recent_key(recent_keys1, key)
            elif decision == 2:
                recent_keys2 = push_recent_key(recent_keys2, key)
            elif decision == 3:
                recent_keys3 = push_recent_key(recent_keys3, key)

        rec_idx = {k: r for r, k in enumerate(reversed(recent_keys1))}
        far = len(recent_keys1) + 1
        rec_idx2 = {k: r for r, k in enumerate(reversed(recent_keys2))}
        far2 = len(recent_keys2) + 1
        rec_idx3 = {k: r for r, k in enumerate(reversed(recent_keys3))}
        far3 = len(recent_keys3) + 1

        for key in keys_caching.keys():
            reduced_key = key[:-1]
            action = key[3]
            if key[1] == 1:
                rec = rec_idx.get(key, far)
                cached_policy[reduced_key][:, action] *= np.exp(-forgetting_cache * rec)
            elif key[1] == 2:
                rec = rec_idx2.get(key, far2)
                cached_policy[reduced_key][:, action] *= np.exp(-forgetting_cache * rec)
            elif key[1] == 3:
                rec = rec_idx3.get(key, far3)
                cached_policy[reduced_key][:, action] *= np.exp(-forgetting_cache * rec)

    return lik


# ============================================================================
#  Model 2 / 3 -- SR & PR meta-controllers (NEW, offline, static)
# ============================================================================
# At each decision the controller reads the goal-reachability of the two real
# children off an *offline* successor (SR) / predecessor (PR) representation and
# decides take-vs-relinquish by the reviewer's heuristic:
#   "relinquish when both actions reach the goal about equally".
# Operationally, the log-odds of *taking* control is driven by the reachability
# GAP between the two children (how diagnostic the step is), plus a control bias:
#       logit P(take) = beta * GAP  +  CB
#       GAP = R_GOAL * ( max(reach1, reach2) - mean(reach1, reach2) )
#           = R_GOAL * |reach1 - reach2| / 2
# This is the fully-identified 2-parameter form (a richer parameterisation that
# also weights the relinquish reward / SR discount collapses to these two
# directions, leaving flat ridges).  GAMMA is fixed at 1, so "reachability" is
# exactly the probability of reaching the goal under a random policy -- the
# quantity the reviewer named.  The map is FIXED across the whole session
# (offline, no learning), which is the point: it cannot track learning.
#   beta (pos) : sensitivity to the reachability gap (the heuristic slope)
#   CB   (real): control bias (net take-vs-relinquish baseline)
SRPR_PARAMS = ['beta', 'CB']
SRPR_TYPES = ['pos', 'real']

R_GOAL = 4.0       # normalised goal reward (= 400 task points; matches MBMC)
SRPR_GAMMA = 1.0   # fixed SR/PR discount -> reachability = P(reach goal)


def _srpr_loglik(params, data, kind):
    """Shared SR/PR meta-controller log-likelihood for one subject."""
    beta, CB = params
    reach = _reach_table(SRPR_GAMMA)         # forward reachability rho^SR

    ll = 0.0
    trials = np.sort(data['trial_num'].unique())
    for trial in trials:
        df_temp = data[data['trial_num'] == trial]
        actions = df_temp['choice_numeric'].values
        depth = int(df_temp['planning_depth'].values[0])
        goal_node = DEPTH_TO_GOAL[depth]
        states = df_temp['current_state'].values
        rg = reach[goal_node]
        for decision in (1, 2, 3):
            node = STATE_TO_NODE.get(states[decision - 1], None)
            if node is None or node not in REAL_TRANSITIONS:
                continue
            c1, c2 = REAL_TRANSITIONS[node]
            v1, v2 = _child_readout(kind, rg[c1], rg[c2])    # SR reach or PR posterior
            gap = R_GOAL * (max(v1, v2) - 0.5 * (v1 + v2))   # = R_GOAL*|v1-v2|/2
            q = np.array([beta * gap + CB, 0.0])             # take vs relinquish
            a = int(actions[decision - 1])                   # 0 = take, 1 = relinquish
            ll += q[a] - logsumexp(q)
    return ll


def sr_loglik(params, data):
    return _srpr_loglik(params, data, 'SR')


def pr_loglik(params, data):
    return _srpr_loglik(params, data, 'PR')


# ============================================================================
#  Model 4 -- Control-bias-only baseline (1 param), the paper's `CB` model
# ============================================================================
CB_PARAMS = ['CB']
CB_TYPES = ['real']


def cb_loglik(params, data):
    """Static control bias only: P(take) = sigmoid(CB) at every decision.

    Q = [CB, 0] (take vs relinquish), no value, no representation, no learning.
    Anchors the model-evidence scale.
    """
    CB = params[0]
    ll = 0.0
    trials = np.sort(data['trial_num'].unique())
    for trial in trials:
        df_temp = data[data['trial_num'] == trial]
        actions = df_temp['choice_numeric'].values
        q = np.array([CB, 0.0])
        for decision in (1, 2, 3):
            a = int(actions[decision - 1])
            ll += q[a] - logsumexp(q)
    return ll


# ============================================================================
#  Model registry  +  data loader
# ============================================================================
def build_models():
    """Return an ordered dict {name: dict(func, params, types, npar)} of
    CBM-ready models for the revision-1 comparison."""
    models = {}
    models['MBMC'] = dict(
        func=make_cbm_model(mbmc_loglik, MBMC_TYPES, kind='samples'),
        params=MBMC_PARAMS, types=MBMC_TYPES, npar=len(MBMC_PARAMS),
        label='MBMC (Cache-MC + Replan)')
    models['SR'] = dict(
        func=make_cbm_model(sr_loglik, SRPR_TYPES, kind='scalar'),
        params=SRPR_PARAMS, types=SRPR_TYPES, npar=len(SRPR_PARAMS),
        label='SR meta-controller (offline)')
    models['PR'] = dict(
        func=make_cbm_model(pr_loglik, SRPR_TYPES, kind='scalar'),
        params=SRPR_PARAMS, types=SRPR_TYPES, npar=len(SRPR_PARAMS),
        label='PR meta-controller (offline)')
    models['CB'] = dict(
        func=make_cbm_model(cb_loglik, CB_TYPES, kind='scalar'),
        params=CB_PARAMS, types=CB_TYPES, npar=len(CB_PARAMS),
        label='Control-bias only')
    return models


# raw-loglik (no transform-wrapping safety net) for BIC computation at the MAP
RAW_LOGLIK = {
    'MBMC': (mbmc_loglik, MBMC_TYPES, 'samples'),
    'SR':   (sr_loglik,   SRPR_TYPES, 'scalar'),
    'PR':   (pr_loglik,   SRPR_TYPES, 'scalar'),
    'CB':   (cb_loglik,   CB_TYPES,   'scalar'),
}


def raw_loglik_at(name, raw_params, data):
    """Pure log-likelihood (not log-posterior) at unconstrained `raw_params`."""
    fn, types, kind = RAW_LOGLIK[name]
    params = _transform(np.asarray(raw_params, dtype=float).ravel(), types)
    if kind == 'samples':
        samples = [np.array([p], dtype=float) for p in params]
        return float(np.asarray(fn(samples, data, np.array([0]))).ravel()[0])
    return float(fn(params, data))


def load_subject_data(study_dir):
    """Load a study's `lmm_fixed.csv` and split into a list of per-subject
    DataFrames (the CBM `data` list).  Returns (data_list, subject_ids)."""
    import os
    df = pd.read_csv(os.path.join(study_dir, 'lmm_fixed.csv'))
    subs = list(pd.unique(df['sub']))
    data_list = [df[df['sub'] == s].reset_index(drop=True) for s in subs]
    return data_list, subs
