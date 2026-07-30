"""
Empirical-range parameter recovery for Fig 3A (left), soft-gated model.
Synthetic data are generated at each subject's BEST-FITTING soft-gated
parameters using the faithful simulator conditioned on that subject's own
dataset — so every random outcome (experienced transitions, goal outcomes
stream) matches their true data. The synthetic choices are then refit with
the same hierarchical EM, and recovery is the Pearson r between generating
and recovered parameters.
"""
import warnings
warnings.filterwarnings('ignore')
import os
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from recovery_common import basename_without_ext
from recovery_em import em_fit, posterior_means
import gated_soft as GB

SSAMP = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
MAXITER = 30

d = pd.read_csv('lmm_fixed.csv')
d['current_state'] = d['current_state'].map(basename_without_ext)
subs = d['sub'].unique()
dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]

R = np.load('em_params_study2_MBMCgatedsoft.npy')   # truth: best-fit, native
assert R.shape == (len(dfs), 9)
sim_params = [R[:, 0], R[:, 1], R[:, 2] * 8, R[:, 3] * 4, R[:, 4], R[:, 5],
              R[:, 6], R[:, 7], R[:, 8]]
print(f'simulating {len(dfs)} subjects at their best-fitting soft-gated '
      f'parameters (faithful: true random outcomes preserved)', flush=True)
sim_df = pd.DataFrame(GB.gatedsoft_simulate(sim_params, dfs))
sim_dfs = [sim_df[sim_df['sub'] == s].reset_index(drop=True)
           for s in sim_df['sub'].unique()]
assert len(sim_dfs) == len(dfs)

t0 = time.time()
ibic, results, _ = em_fit(sim_dfs, GB.PARAM_INFO_GSOFT, GB.gatedsoft_lik,
                          sample_size=SSAMP, cores=CORES, max_iter=MAXITER,
                          verbose=True, seed0=42)
Rrec = posterior_means(results, GB.PARAM_INFO_GSOFT)
print(f'refit iBIC={ibic:.1f} ({time.time()-t0:.0f}s)', flush=True)

SYM = [r'$\beta_{\mathrm{MBMC}}$', r'$\gamma_d$', r'$\tilde b_1$', r'$\tilde b_2$',
       r'$\kappa_C$', r'$\beta_{\mathrm{CB}}$', r'$\gamma_C$', r'$\kappa_R$',
       r'$\omega_P$']
P = 9
C = np.zeros((P, P))
for i in range(P):
    for j in range(P):
        C[i, j] = pearsonr(R[:, i], Rrec[:, j])[0]
pd.DataFrame(C, index=SYM, columns=SYM).to_csv('faithful_recovery_softgate_corr.csv')
diag = np.diag(C)
print('diagonal r:', np.round(diag, 3), flush=True)
print(f'MEAN DIAGONAL r = {diag.mean():.3f}', flush=True)

sns.set(style='white', font_scale=1.2)
plt.figure(figsize=(9.2, 7.8))
ann = np.vectorize(lambda x: ('%.2f' % x).replace('0.', '.'))(C)
ax = sns.heatmap(C, annot=ann, fmt='', cmap='coolwarm', vmin=-1, vmax=1,
                 linewidths=0.5, square=True, xticklabels=SYM, yticklabels=SYM,
                 cbar_kws={'label': r'Pearson $r$', 'shrink': 0.82})
ax.set_xlabel('Recovered parameter')
ax.set_ylabel('Generating parameter (best fit)')
ax.tick_params(axis='x', rotation=25)
plt.setp(ax.get_xticklabels(), ha='right')
plt.title('Parameter recovery at best-fitting parameters, soft-gated model\n'
          '(faithful simulation: true per-subject outcomes preserved)')
plt.tight_layout()
plt.savefig('faithful_recovery_softgate_heatmap.png', dpi=300, bbox_inches='tight')
print('saved faithful_recovery_softgate_heatmap.png', flush=True)
print('RECOVERY DONE', flush=True)
