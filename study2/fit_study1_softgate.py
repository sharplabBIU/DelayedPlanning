"""
Fit the SOFT-GATED + tailored-saturation model (gated_soft) to Study 1,
mirroring gatedsoft_run_all.stage1. Saves em_params_study1_MBMCgatedsoft.npy,
then checks the parameter-RT correlations reported for Study 2.
"""
import warnings
warnings.filterwarnings('ignore')
import os
import time
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from recovery_common import basename_without_ext
from recovery_em import em_fit, posterior_means
import gated_soft as GB

SSAMP = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
MAXITER = 30

d = pd.read_csv('../study1/lmm_fixed.csv')
d['current_state'] = d['current_state'].map(basename_without_ext)
subs = d['sub'].unique()
dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
print(f'[study1] fitting SOFT-gated (k=9, ss={SSAMP}) to {len(dfs)} subjects', flush=True)
t0 = time.time()
ibic, results, _ = em_fit(dfs, GB.PARAM_INFO_GSOFT, GB.gatedsoft_lik, sample_size=SSAMP,
                          cores=CORES, max_iter=MAXITER, verbose=True, seed0=1)
R = posterior_means(results, GB.PARAM_INFO_GSOFT)
np.save('em_params_study1_MBMCgatedsoft.npy', R)
print(f'[study1] GATED-SOFT iBIC={ibic:.1f} ({time.time()-t0:.0f}s)', flush=True)

PN = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache', 'CB',
      'forgetC', 'cache_reward', 'cache_plan']
for i, p in enumerate(PN):
    print(f'  {p:14s} mean={R[:,i].mean():.3f} median={np.median(R[:,i]):.3f} '
          f'IQR=[{np.percentile(R[:,i],25):.3f},{np.percentile(R[:,i],75):.3f}]', flush=True)

# parameter-RT correlations on Study 1 (spearman, Bonferroni x18 as in the paper)
import arviz as az
df1 = pd.read_csv('../study1/preprocessed_data.csv')
_, subs_pp = pd.factorize(df1['sub'])
assert list(subs_pp) == list(subs), 'sub order mismatch'
tr = az.from_netcdf('../study1/RTdata_model_fitted_withintrial.nc')
post = tr.posterior
bRT = post['coef_delayed_planning'].values.mean() + post['slope_sub_dp'].values.mean(axis=(0, 1))
bINT = post['coef_interaction'].values.mean() + post['slope_sub_interaction'].values.mean(axis=(0, 1))
print('[study1] param-RT correlations (spearman, p x18):', flush=True)
for i, p in enumerate(PN):
    for eff, name in [(bRT, 'bRT'), (bINT, 'bRTxTime')]:
        rho, pv = spearmanr(R[:, i], eff)
        print(f'  {p:12s} vs {name:8s} rho={rho:+.3f} p_bonf={min(1, pv*18):.3g}', flush=True)
print('DONE', flush=True)
