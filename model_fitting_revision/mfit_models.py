"""
Full model registry for CBM/HBI: the 18 models from study2/model_fitting.py plus
the SR and PR meta-controllers from cbm_models.py (20 total).

Each model_fitting.py likelihood has the `f(samples, data, rng_samples)` interface
and is wrapped for CBM exactly like cbm_models.mbmc_loglik. Parameter order follows
each model's group_parameters_info; distribution -> unconstrained type:
gamma->pos, beta->unit, norm->real.
"""
import mfit_likelihoods as LK
import cbm_models as CB
from cbm_models import make_cbm_model, sr_loglik, pr_loglik

_DIST2TYPE = {'gamma': 'pos', 'beta': 'unit', 'norm': 'real'}


def _mk(lik, spec):
    """spec: list of (param_name, distribution). Returns registry entry."""
    params = [p for p, _ in spec]
    types = [_DIST2TYPE[d] for _, d in spec]
    return dict(func=make_cbm_model(lik, types, kind='samples'),
                params=params, types=types, npar=len(params))


# (param, distribution) in model_fitting.py order  ->  samples[i] index
_MB = [('MB_B', 'gamma'), ('MB_depth', 'beta'), ('MB_breadth', 'beta'),
       ('breadth2', 'beta')]
_MB_C = _MB + [('mbcache', 'gamma')]
_MB_CR = _MB_C + [('cache_reward', 'norm')]
_MB_CRF = _MB_CR + [('forget', 'gamma')]
_MB_CRF_CB = _MB + [('mbcache', 'gamma'), ('CB', 'norm'), ('forgetC', 'gamma'),
                    ('cache_reward', 'norm')]

REGISTRY = {
    'MBMC_optimal':        _mk(LK.MB_actionSeparation, [('MB_B', 'gamma')]),
    'MBMC_Depth':          _mk(LK.MB_Depth_actionSeparation,
                               [('MB_B', 'gamma'), ('MB_depth', 'beta')]),
    'MBMC_Breadth2':       _mk(LK.MB_Breadth_actionSeparation,
                               [('MB_B', 'gamma'), ('MB_breadth', 'beta'),
                                ('breadth2', 'beta')]),
    'MBMC_Breadth1':       _mk(LK.MB_oneBreadth_Depth_actionSeparation,
                               [('MB_B', 'gamma'), ('MB_depth', 'beta'),
                                ('MB_breadth', 'beta')]),
    'MBMC_Breadth2_Depth': _mk(LK.MB_Breadth_Depth_actionSeparation, _MB),
    'MBMC_Breadth2_Depth_CC':  _mk(LK.MB_Breadth_Depth_actionSeparation_MBcache1_fullmemory, _MB_C),
    'MBMC_Breadth2_Depth_CCR': _mk(LK.MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory, _MB_CR),
    'MBMC_Breadth2_Depth_CCRF': _mk(LK.MB_Breadth_Depth_actionSeparation_MBcache2_limitedmemory, _MB_CRF),
    'MBMC_Breadth2_Depth_CCRF_CB': _mk(LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting, _MB_CRF_CB),
    'MBMC_Breadth2_Depth_CCRF_CB_PE': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution,
        _MB_CRF_CB + [('cache_plan', 'gamma')]),
    'MBMCF_Breadth2_Depth_CCRF_CB': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgettingRoutesAndCache,
        _MB_CRF_CB + [('forgetR', 'gamma')]),
    'MBMCreplace_Breadth2_Depth_CCRF_CB_PE': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_replacement_execution,
        _MB_CRF_CB + [('cache_plan', 'gamma')]),
    'MBMCsequential_Breadth2_Depth_CCRF_CB': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_sequentialactionsearch,
        _MB_CRF_CB),
    'MBMC_Breadth2_Depth_CB_MF': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_MF,
        _MB + [('CB', 'norm'), ('lr', 'beta'), ('mf_beta', 'gamma')]),
    'MBMC_Breadth2_Depth_MF': _mk(
        LK.MB_Breadth_Depth_actionSeparation_MBcache_forgetting_MF,
        _MB + [('lr', 'beta'), ('mf_beta', 'gamma')]),
    'CCRF_CB': _mk(LK.CacheR_CB_4, [('CB', 'norm'), ('mbcache', 'gamma'),
                                    ('forgetC', 'gamma'), ('cache_reward', 'norm')]),
    'CCRF':    _mk(LK.CacheR_CB_3, [('mbcache', 'gamma'), ('forgetC', 'gamma'),
                                    ('cache_reward', 'norm')]),
    'CB':      _mk(LK.CacheR_CB_1, [('CB', 'norm')]),
    # SR / PR meta-controllers (from cbm_models)
    'SR': dict(func=make_cbm_model(sr_loglik, ['pos', 'real'], kind='scalar'),
               params=['beta', 'CB'], types=['pos', 'real'], npar=2),
    'PR': dict(func=make_cbm_model(pr_loglik, ['pos', 'real'], kind='scalar'),
               params=['beta', 'CB'], types=['pos', 'real'], npar=2),
}

# order for the HBI comparison (nested progression, then variants, then baselines)
MODEL_ORDER = [
    'MBMC_optimal', 'MBMC_Depth', 'MBMC_Breadth2', 'MBMC_Breadth1',
    'MBMC_Breadth2_Depth', 'MBMC_Breadth2_Depth_CC', 'MBMC_Breadth2_Depth_CCR',
    'MBMC_Breadth2_Depth_CCRF', 'MBMC_Breadth2_Depth_CCRF_CB',
    'MBMC_Breadth2_Depth_CCRF_CB_PE', 'MBMCF_Breadth2_Depth_CCRF_CB',
    'MBMCreplace_Breadth2_Depth_CCRF_CB_PE', 'MBMCsequential_Breadth2_Depth_CCRF_CB',
    'MBMC_Breadth2_Depth_CB_MF', 'MBMC_Breadth2_Depth_MF',
    'CCRF_CB', 'CCRF', 'CB', 'SR', 'PR',
]
