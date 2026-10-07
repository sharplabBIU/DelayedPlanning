"""Supplementary Fig. S7: best-fitting parameters of the winning soft-gated MBMC model (mean +- SEM per study).
Reads em_params_study{1,2}_MBMCgatedsoft.npy; writes cbm_MBMCgatedsoft_params_EM_barplots.png. Run from study2/."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
SYM = [r'$\beta_{\mathrm{MBMC}}$', r'$\gamma_d$', r'$\tilde b_1$', r'$\tilde b_2$', r'$\kappa_C$', r'$\beta_{\mathrm{CB}}$', r'$\gamma_C$', r'$\kappa_R$', r'$\omega_P$']
fig, axes = plt.subplots(1, 2, figsize=(20, 7), sharey=True)
for ax, st, col in zip(axes, ['study1', 'study2'], ['#3776ab', '#f26d21']):
    R = np.load(f'em_params_{st}_MBMCgatedsoft.npy')
    m, se = R.mean(0), R.std(0, ddof=1) / np.sqrt(len(R))
    ax.bar(range(9), m, yerr=se, color=col, edgecolor='k', linewidth=0.6, capsize=4)
    ax.set_xticks(range(9)); ax.set_xticklabels(SYM, fontsize=18); ax.tick_params(axis='y', labelsize=16)
    ax.set_title(f'Study {st[-1]}  (N = {len(R)})', fontsize=20); ax.spines[['top', 'right']].set_visible(False)
axes[0].set_ylabel('Fitted value (native, EM)', fontsize=18)
fig.suptitle('MBMC best-fitting parameters — EM / iterative importance sampling (no back-transform)', fontsize=20)
fig.tight_layout(); fig.savefig('cbm_MBMCgatedsoft_params_EM_barplots.png', dpi=200, bbox_inches='tight'); print('saved cbm_MBMCgatedsoft_params_EM_barplots.png')
