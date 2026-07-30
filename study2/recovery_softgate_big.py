"""
Parameter recovery for the SOFT-GATED + tailored-saturation model.

Ground truth drawn from recovery_parameter.GROUND_TRUTH (full prior shapes);
simulate with the soft-gated faithful simulator (template-conditioned transitions);
fit back with the soft-gated likelihood via hierarchical EM. Config as
recovery_parameter_iterative.py: N_SUB=1000, ss=10000, N_ITER=1, BASE_SEED=200,
MAX_EM_ITER=50. Pearson correlation matrix (truth x recovered).
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

from recovery_em import em_fit, posterior_means
import recovery_parameter as RP
import gated_soft as GF

N_SUB = 1000
SAMPLE_SIZE = 10000
N_ITER = 1
CORES = max(1, (os.cpu_count() or 8) - 2)
BASE_SEED = 200
MAX_EM_ITER = 50

GT_KEYS = ['mb_control', 'discount', 'breadth1', 'breadth2', 'mb_cache',
           'choice_bias', 'forget', 'cache_reward', 'cache_plan']
SYMBOLS = [r'$\beta_{\mathrm{MBMC}}$', r'$\gamma_d$', r'$\tilde b_1$',
           r'$\tilde b_2$', r'$\kappa_C$', r'$\beta_{\mathrm{CB}}$', r'$\gamma_C$',
           r'$\kappa_R$', r'$\omega_P$']
P = len(GF.PARAM_INFO_GSOFT)


def one_iteration(it):
    rng = np.random.default_rng(BASE_SEED + it)
    templates = [RP.make_template(rng) for _ in range(N_SUB)]
    gt = {k: RP.sample_truth(rng, k, N_SUB) for k in RP.GROUND_TRUTH}
    T = np.column_stack([gt[k] for k in GT_KEYS])
    sim_params = [gt['mb_control'], gt['discount'], gt['breadth1'] * 8,
                  gt['breadth2'] * 4, gt['mb_cache'], gt['choice_bias'],
                  gt['forget'], gt['cache_reward'], gt['cache_plan']]
    sim_df = pd.DataFrame(GF.gatedsoft_simulate(sim_params, templates))
    dfs = [sim_df[sim_df['sub'] == s].reset_index(drop=True)
           for s in sim_df['sub'].unique()]
    t0 = time.time()
    ibic, results, _ = em_fit(dfs, GF.PARAM_INFO_GSOFT, GF.gatedsoft_lik,
                              sample_size=SAMPLE_SIZE, cores=CORES,
                              max_iter=MAX_EM_ITER, verbose=True,
                              seed0=(BASE_SEED + it) * 1000)
    R = posterior_means(results, GF.PARAM_INFO_GSOFT)
    C = np.zeros((P, P))
    for i in range(P):
        for j in range(P):
            C[i, j] = pearsonr(T[:, i], R[:, j])[0]
    print(f'iter {it+1}/{N_ITER}  iBIC={ibic:.1f}  ({time.time()-t0:.0f}s)', flush=True)
    return C


def main():
    print(f'Soft-gated recovery: N_SUB={N_SUB}, ss={SAMPLE_SIZE}, iters={N_ITER}, '
          f'seed={BASE_SEED}, max_em={MAX_EM_ITER}', flush=True)
    mats = np.stack([one_iteration(it) for it in range(N_ITER)])
    Cmean = np.nanmean(mats, 0)
    pd.DataFrame(Cmean, index=SYMBOLS, columns=SYMBOLS).to_csv(
        'recovery_softgate_big_corr.csv')
    print('\ndiagonal (self-recovery) Pearson r:', flush=True)
    for s, dg in zip(SYMBOLS, np.diag(Cmean)):
        print('  %-26s %.3f' % (s, dg), flush=True)

    sns.set(style='white', font_scale=1.2)
    plt.figure(figsize=(9.2, 7.8))
    ann = np.vectorize(lambda x: ('%.2f' % x).replace('0.', '.'))(Cmean)
    ax = sns.heatmap(Cmean, annot=ann, fmt='', cmap='coolwarm', vmin=-1, vmax=1,
                     linewidths=0.5, square=True, xticklabels=SYMBOLS,
                     yticklabels=SYMBOLS,
                     cbar_kws={'label': r'Pearson $r$ (N=%d)' % N_SUB, 'shrink': 0.82})
    ax.set_xlabel('Recovered parameter')
    ax.set_ylabel('Ground-truth parameter')
    ax.tick_params(axis='x', rotation=25)
    plt.setp(ax.get_xticklabels(), ha='right')
    ax.tick_params(axis='y', rotation=0)
    plt.title('Parameter recovery, soft-gated model\n(N=%d synthetic subjects, '
              '%d IS samples)' % (N_SUB, SAMPLE_SIZE))
    plt.tight_layout()
    plt.savefig('recovery_softgate_big_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('saved recovery_softgate_big_heatmap.png, recovery_softgate_big_corr.csv',
          flush=True)
    print('RECOVERY DONE', flush=True)


if __name__ == '__main__':
    main()
