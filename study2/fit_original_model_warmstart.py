"""Per-subject EM fit of the ORIGINAL MBMC model (MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution)
for one study, written out in the two formats the repository uses:
  * em_params_<study>_MBMC.npy            (N x 9 native posterior means; reference file)
  * ../<study>/<param>_exec.npy            (one file per parameter; the warm start used by
                                            model_fitting_revision/run_map.py and by legacy notebook cells)
This is the fit_study() step of fit_real_em.py made standalone so that it can be re-run for a single study
without touching the soft-gated parameter summaries (Supp. Tables S3-S4).   Usage: python fit_original_model_warmstart.py study1
"""
import os, sys, time, warnings
warnings.filterwarnings('ignore')
import numpy as np, pandas as pd
import recovery_common as rc
from recovery_common import basename_without_ext
from recovery_em import em_fit, posterior_means
import recovery_parameter as RP
study = sys.argv[1] if len(sys.argv) > 1 else 'study1'
SS, CORES, MAXITER, SEED0 = 10000, max(1, (os.cpu_count() or 8) - 2), 30, 1
LIK = rc.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution
PARAM_INFO = RP.PARAM_INFO; PNAMES = [p[0] for p in PARAM_INFO]
d = pd.read_csv(f'../{study}/lmm_fixed.csv'); d['current_state'] = d['current_state'].map(basename_without_ext)
subs = d['sub'].unique(); dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
print(f'[{study}] original MBMC model: EM fit of {len(subs)} subjects (ss={SS}, cores={CORES})', flush=True)
t0 = time.time()
ibic, results, _ = em_fit(dfs, PARAM_INFO, LIK, sample_size=SS, cores=CORES, max_iter=MAXITER, verbose=True, seed0=SEED0)
R = posterior_means(results, PARAM_INFO)
np.save(f'em_params_{study}_MBMC.npy', R)
for j, name in enumerate(PNAMES):
    np.save(os.path.join('..', study, f'{name}_exec.npy'), R[:, j])
print(f'[{study}] done: N={len(subs)}, iBIC={ibic:.1f}, {time.time()-t0:.0f}s; wrote em_params_{study}_MBMC.npy and {len(PNAMES)} ../{study}/*_exec.npy files', flush=True)
