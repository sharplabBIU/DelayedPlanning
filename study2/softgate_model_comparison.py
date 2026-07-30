"""
Model comparison (Fig 3A right) rerun with the SOFT-GATE rule in every model
that uses MB reasoning. Candidate set = the 13 models of the model-recovery
analysis (Supp Fig S4), with the winning model instantiated as the soft-gated
MBMC. Patches applied to mfit_likelihoods.py source:
  * soft gate: second-search counter accrues p1 * b2 per visit (12 sites)
  * state-tailored first-search urns (subtree saturation), as in gated_soft
Fit to Study 2 real data (N=163), hierarchical EM, ss=10000, maxiter=30.
"""
import warnings
warnings.filterwarnings('ignore')
import os
import re
import sys
import time
import types
import numpy as np
import pandas as pd

from recovery_em import em_fit

SSAMP = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
MAXITER = 30
SMOKE = '--smoke' in sys.argv

SRC = open('../model_fitting_revision/mfit_likelihoods.py').read()

LIK_OLD = ('\t\tif num_success2 > 0:\n'
           '\t\t\texp_arr2 += mb_breadth_arr2\n')
LIK_NEW = ('\t\tif num_success2 > 0:\n'
           '\t\t\t_p1n = np.minimum(update_probability_planning_success('
           'num_success1, total1, exp_arr), 1.0)\n'
           '\t\t\texp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2\n')
ngate = SRC.count(LIK_OLD)
assert ngate == 12, f'gate sites: {ngate}'
SRC = SRC.replace(LIK_OLD, LIK_NEW)

URN_PAIRS = [
    (r"\(2,\s*1,\s*'start'\):\s*\[2,\s*8\]", "(2, 1, 'start'): [1,4]"),
    (r"\(1,\s*1,\s*'start'\):\s*\[4,\s*8\]", "(1, 1, 'start'): [2,4]"),
    (r"\(1,\s*2,\s*'images/toothbrush\.png'\):\s*\[2,\s*4\]",
     "(1, 2, 'images/toothbrush.png'): [1,2]"),
    (r"\(1,\s*2,\s*'images/baby\.png'\):\s*\[2,\s*4\]",
     "(1, 2, 'images/baby.png'): [1,2]"),
]
for pat, new in URN_PAIRS:
    SRC, n = re.subn(pat, new, SRC)
    print(f'urn patch {new[:28]}... applied {n}x', flush=True)
    assert n >= 13, f'too few urn sites: {n}'

with open('mfit_softgate_gen.py', 'w') as f:
    f.write(SRC)
import mfit_softgate_gen as LK

G, B, N = 'gamma', 'beta', 'norm'
_MBB = [['MB_B', G, [1, 1]]]
_MB2 = _MBB + [['MB_depth', B, [1, 1]]]
_MBbd = _MBB + [['MB_depth', B, [1, 1]], ['MB_breadth', B, [1, 1]], ['breadth2', B, [1, 1]]]
_MBc = _MBbd + [['mbcache', G, [1, 1]]]
_MBcr = _MBc + [['cache_reward', N, [0, 5]]]
_MBcrf = _MBcr + [['forget', G, [1, 1]]]
_MBcrfcb = _MBbd + [['mbcache', G, [1, 1]], ['CB', N, [0, 5]], ['forgetC', G, [1, 1]],
                    ['cache_reward', N, [0, 5]]]

CANDIDATES = [
    ('CB',            LK.CacheR_CB_1, [['CB', N, [0, 5]]]),
    ('CCRF',          LK.CacheR_CB_3, [['mbcache', G, [1, 1]], ['forgetC', G, [1, 1]],
                                       ['cache_reward', N, [0, 5]]]),
    ('CCRF_CB',       LK.CacheR_CB_4, [['CB', N, [0, 5]], ['mbcache', G, [1, 1]],
                                       ['forgetC', G, [1, 1]], ['cache_reward', N, [0, 5]]]),
    ('MBMC_optimal',  LK.MB_actionSeparation, _MBB),
    ('MBMC_Depth',    LK.MB_Depth_actionSeparation, _MB2),
    ('MBMC_Breadth2', LK.MB_Breadth_actionSeparation,
                      _MBB + [['MB_breadth', B, [1, 1]], ['breadth2', B, [1, 1]]]),
    ('MBMC_Breadth1', LK.MB_oneBreadth_Depth_actionSeparation,
                      _MBB + [['MB_depth', B, [1, 1]], ['MB_breadth', B, [1, 1]]]),
    ('MBMC_BD',       LK.MB_Breadth_Depth_actionSeparation, _MBbd),
    ('MBMC_CC',       LK.MB_Breadth_Depth_actionSeparation_MBcache1_fullmemory, _MBc),
    ('MBMC_CCR',      LK.MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory, _MBcr),
    ('MBMC_CCRF',     LK.MB_Breadth_Depth_actionSeparation_MBcache2_limitedmemory, _MBcrf),
    ('MBMC_CCRF_CB',  LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting, _MBcrfcb),
    ('MBMC_full',     LK.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution,
                      _MBcrfcb + [['cache_plan', G, [1, 1]]]),
]

d = pd.read_csv('lmm_fixed.csv')          # RAW current_state paths (mfit keys)
subs = d['sub'].unique()
dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
print(f'fitting {len(CANDIDATES)} candidates to {len(dfs)} subjects '
      f'(ss={SSAMP}, maxiter={MAXITER}, cores={CORES})', flush=True)

todo = CANDIDATES[-1:] + CANDIDATES[:1] if SMOKE else CANDIDATES
rows = []
for name, lik, pinfo in todo:
    t0 = time.time()
    mi = 2 if SMOKE else MAXITER
    ibic, _r, _f = em_fit(dfs, [list(p) for p in pinfo], lik, sample_size=SSAMP,
                          cores=CORES, max_iter=mi, verbose=SMOKE, seed0=1)
    rows.append(dict(model=name, k=len(pinfo), iBIC=round(ibic, 2)))
    print(f'{name:14s} k={len(pinfo)}  iBIC={ibic:.2f}  ({time.time()-t0:.0f}s)', flush=True)

out = pd.DataFrame(rows)
if not SMOKE:
    out.to_csv('softgate_model_comparison_BICs.csv', index=False)
    best = out.loc[out['iBIC'].idxmin()]
    out['delta_iBIC'] = out['iBIC'] - best['iBIC']
    print('\nbest:', best['model'])
    print(out.sort_values('iBIC').to_string(index=False))
    out.to_csv('softgate_model_comparison_BICs.csv', index=False)
print('DONE', flush=True)
