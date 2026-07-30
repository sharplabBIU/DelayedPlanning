"""
SOFT-GATED b1/b2 model with state-tailored saturation.

Like gated_sat, but the gate on the second search is PROBABILISTIC rather than
hard: on every visit, the second search engages with probability p1 (the current
first-search success probability at that state) and stays off with probability
1 - p1. In the likelihood/simulator this is the marginalized (expected) accrual:

    exp2 += p1 * b2*4        per visit   (was: b2*4 only once p1 == 1)

So breadth-2 initiation is graded by breadth-1 success -- e.g. p1 = 0.7 engages
the second search at 70% strength -- and converges to the hard gate as p1 -> 1.
First-search urns keep the state-tailored (subtree) saturation of gated_sat.
"""
import types
import re
import numpy as np

_HDR = ('import numpy as np\n'
        'from random import sample\n'
        'from scipy.special import comb, softmax, expit, logsumexp\n'
        'from recovery_common import basename_without_ext\n')

_LIK_OLD = ('\t\tif num_success2 > 0:\n'
            '\t\t\texp_arr2 += mb_breadth_arr2\n')
_LIK_NEW = ('\t\tif num_success2 > 0:\n'
            '\t\t\t_p1n = np.minimum(update_probability_planning_success('
            'num_success1, total1, exp_arr), 1.0)\n'
            '\t\t\texp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2\n')
_SIM_OLD = ('\t\t\t\tif num_success2 > 0:\n'
            '\t\t\t\t\texp_arr2 += mb_breadth_arr2\n')
_SIM_NEW = ('\t\t\t\tif num_success2 > 0:\n'
            '\t\t\t\t\t_p1n = min(update_probability_planning_success('
            'num_success1, total1, exp_arr), 1.0)\n'
            '\t\t\t\t\texp_arr2 += _p1n * mb_breadth_arr2\n')

_URN_PAIRS = [("(2, 1, 'start'): [2,8]", "(2, 1, 'start'): [1,4]"),
              ("(1, 1, 'start'): [4,8]", "(1, 1, 'start'): [2,4]"),
              ("(1, 2, 'toothbrush'): [2,4]", "(1, 2, 'toothbrush'): [1,2]"),
              ("(1, 2, 'baby'): [2,4]", "(1, 2, 'baby'): [1,2]")]


def _extract(src, name):
    i = src.index(f'def {name}(')
    m = re.search(r'\ndef \w+\(', src[i + 10:])
    return src[i: i + 10 + m.start()] if m else src[i:]


def _patch_urns(src):
    a = src.index('mb_key = {')
    b = src.index('}', a)
    head, block, tail = src[:a], src[a:b], src[b:]
    for old, new in _URN_PAIRS:
        pat = re.escape(old).replace(r'\ ', r'\s*').replace(r'\[', r'\[\s*').replace(
            r',', r'\s*,\s*')
        block, n = re.subn(pat, new, block)
        assert n == 1, f'urn patch failed: {old!r} ({n})'
    return head + block + tail


def _build():
    lik_src = _extract(open('recovery_common.py').read(),
                       'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution')
    assert _LIK_OLD in lik_src
    lik_src = _patch_urns(lik_src.replace(_LIK_OLD, _LIK_NEW))
    sim_src = _extract(open('recovery_faithful.py').read(), 'MF_faithful_simulate')
    assert _SIM_OLD in sim_src
    sim_src = _patch_urns(sim_src.replace(_SIM_OLD, _SIM_NEW))
    mod = types.ModuleType('gatedsoft_generated')
    exec(_HDR + lik_src + '\n\n' + sim_src, mod.__dict__)
    return mod


_M = _build()
_GLIK = getattr(_M, 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution')
_GSIM = getattr(_M, 'MF_faithful_simulate')


def gatedsoft_lik(samples, data, rng_samples):
    return _GLIK(samples, data, rng_samples)


def gatedsoft_simulate(parameters, dfs):
    return _GSIM(parameters, dfs)


G, B, N = 'gamma', 'beta', 'norm'
PARAM_INFO_GSOFT = [
    ['MB_B',        G, [1, 1]],
    ['MB_depth',    B, [1, 1]],
    ['MB_breadth',  B, [1, 1]],
    ['breadth2',    B, [1, 1]],
    ['mbcache',     G, [1, 1]],
    ['CB',          N, [0, 5]],
    ['forgetC',     G, [1, 1]],
    ['cache_reward', N, [0, 5]],
    ['cache_plan',  G, [1, 1]],
]
PN_GSOFT = [p[0] for p in PARAM_INFO_GSOFT]
