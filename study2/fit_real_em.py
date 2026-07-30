"""
Best-fitting MBMC parameters for Study 1 and Study 2 on the REAL data, using Path A:
the hierarchical EM / iterative importance sampling (recovery_em.em_fit + recovery_common,
the same estimator as model_fitting.py) with the full winning model
(MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution).

Parameters are fit and reported directly in NATIVE space (group families gamma/beta/norm),
so NO exp/sigmoid back-transform is applied -- the posterior means ARE the native values.

Outputs (per study): em_params_{study}_MBMC.npy (per-subject native posterior means),
em_params_{study}_median_iqr.csv; plus a combined barplot cbm_MBMC_params_EM_barplots.png.
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

import recovery_common as rc
from recovery_common import basename_without_ext
from recovery_em import em_fit, posterior_means
import recovery_parameter as RP

SS = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
MAXITER = 30
SEED0 = 1
LIK = rc.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution
PARAM_INFO = RP.PARAM_INFO
PNAMES = [p[0] for p in PARAM_INFO]
SYMBOLS = RP.SYMBOLS
STUDIES = ['study1', 'study2']
COLOR = {'study1': '#2c7fb8', 'study2': '#d95f0e'}


def fit_study(study):
    d = pd.read_csv(f'../{study}/lmm_fixed.csv')
    d['current_state'] = d['current_state'].map(basename_without_ext)   # images/x.png -> x
    subs = d['sub'].unique()
    dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
    print(f'[{study}] fitting {len(subs)} subjects (EM, ss={SS}, cores={CORES})...',
          flush=True)
    t0 = time.time()
    ibic, results, _ = em_fit(dfs, PARAM_INFO, LIK, sample_size=SS, cores=CORES,
                              max_iter=MAXITER, verbose=True, seed0=SEED0)
    R = posterior_means(results, PARAM_INFO)                     # N x 9 native
    np.save(f'em_params_{study}_MBMC.npy', R)
    print(f'[{study}] done: N={len(subs)}, iBIC={ibic:.1f}, {time.time()-t0:.0f}s', flush=True)
    return R


def summary(R, n):
    return pd.DataFrame({
        'parameter': PNAMES, 'symbol': SYMBOLS, 'n': n,
        'mean': R.mean(0), 'sem': R.std(0, ddof=1) / np.sqrt(n),
        'median': np.median(R, 0),
        'Q1': np.percentile(R, 25, 0), 'Q3': np.percentile(R, 75, 0),
    })


def main():
    fits = {st: fit_study(st) for st in STUDIES}
    stats = {st: summary(fits[st], len(fits[st])) for st in STUDIES}
    x = np.arange(len(PNAMES))

    for st in STUDIES:
        s = stats[st]
        s.to_csv(f'em_params_{st}_median_iqr.csv', index=False)
        print(f'\n=== {st}: MBMC best-fit (EM, native) median [IQR], N={len(fits[st])} ===')
        for p, sym, m, a, b in zip(s['parameter'], s['symbol'], s['median'],
                                   s['Q1'], s['Q3']):
            print(f'  {p:13s} {sym:26s} {m:8.3f}  [{a:.3f}, {b:.3f}]')

    # ---- barplots: mean +/- SEM, one panel per study, shared y ----
    ymax = max(float((s['mean'] + s['sem']).max()) for s in stats.values()) * 1.12
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.2), sharey=True)
    for ax, st in zip(axes, STUDIES):
        s = stats[st]
        ax.bar(x, s['mean'], yerr=s['sem'], capsize=4, color=COLOR[st],
               edgecolor='black', linewidth=0.6, error_kw=dict(lw=1.1))
        ax.set_xticks(x)
        ax.set_xticklabels(SYMBOLS, fontsize=14)
        ax.set_title(f'{st.replace("study", "Study ")}  (N = {len(fits[st])})', fontsize=13)
        ax.set_ylim(0, ymax)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel('Fitted value (native, EM)', fontsize=12)
    fig.suptitle('MBMC best-fitting parameters — EM / iterative importance sampling '
                 '(no back-transform)', fontsize=13, y=1.02)
    fig.tight_layout()
    fig.savefig('cbm_MBMC_params_EM_barplots.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('\nSaved: cbm_MBMC_params_EM_barplots.png, em_params_study{1,2}_MBMC.npy, '
          'em_params_study{1,2}_median_iqr.csv')


if __name__ == '__main__':
    main()
