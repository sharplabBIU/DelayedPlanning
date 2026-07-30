"""
Regenerate the Fig 3C panels using the SOFT-GATED model fits
(em_params_study2_MBMCgatedsoft.npy), mirroring the notebook's approach:
z-scored per-subject LMM random effects vs z-scored model parameters,
auto Pearson/Spearman by Shapiro, Bonferroni x18.
Panels saved with _softgate suffix.
"""
import numpy as np
import pandas as pd
import arviz as az
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, shapiro

sns.set(font_scale=2.6, style='white')

def normalize_array(x):
    return (x - x.mean()) / x.std()

def auto_corr(x, y, alpha=0.05, label=''):
    sx, px = shapiro(x)
    sy, py = shapiro(y)
    method = 'Pearson' if (px > alpha and py > alpha) else 'Spearman'
    r, p = (pearsonr(x, y) if method == 'Pearson' else spearmanr(x, y))
    p = float(np.clip(p * 18, 0, 1))
    print(f'{label} ({method}): r = {r:.4f}, p_bonf = {p:.4g}')
    return r, p

df = pd.read_csv('preprocessed_data.csv')
sub_idx, subs = pd.factorize(df['sub'])
tr = az.from_netcdf('RTdata_model_fitted_withintrial2.nc')
pm = tr.posterior.mean(dim=['chain', 'draw'])
eff_dp = normalize_array(pm['slope_sub_dp'].values)
eff_int = normalize_array(pm['slope_sub_interaction'].values)

PN = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache', 'CB',
      'forgetC', 'cache_reward', 'cache_plan']
R = np.load('em_params_study2_MBMCgatedsoft.npy')
lf = pd.read_csv('lmm_fixed.csv')
assert list(lf['sub'].unique()) == list(subs)
P = {p: normalize_array(R[:, i]) for i, p in enumerate(PN)}

panels = [
    ('breadth2', eff_dp,  r'$\tilde b_2$',        r'$\beta$ RT',          'black',
     'MB_BothAction_RTMAIN_softgate.png'),
    ('breadth2', eff_int, r'$\tilde b_2$',        r'$\beta$ RT x Time',   'black',
     'MB_BothAction_RTinteraction_softgate.png'),
    ('MB_B',     eff_dp,  r'$\beta_{MBMC}$',      r'$\beta$ RT',          'blue',
     'MBBeta_RTMAIN_softgate.png'),
    ('CB',       eff_dp,  r'$\beta_{CB}$',        r'$\beta$ RT',          'green',
     'CB_RTMAIN_softgate.png'),
]
for par, eff, xlab, ylab, color, fname in panels:
    r, p = auto_corr(P[par], eff, label=f'{par} vs {ylab}')
    plt.figure(figsize=(8, 7))
    sns.regplot(x=P[par], y=eff, color=color)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    ax = plt.gca()
    plt.text(0.62, 0.92, r'$\rho = {}$'.format(round(r, 2)),
             transform=ax.transAxes, fontsize=26)
    plt.tight_layout()
    plt.savefig(fname, dpi=300, bbox_inches='tight')
    plt.close()
    print(f'saved {fname}')

# extra checks reported in the text
auto_corr(P['cache_reward'], eff_int, label='kappa_R vs bRTxTime')
auto_corr(P['mbcache'], eff_dp, label='kappa_C vs bRT')
auto_corr(P['forgetC'], eff_dp, label='gamma_C vs bRT')
auto_corr(P['cache_plan'], eff_dp, label='omega_P vs bRT')
# Eran comment 1330: beta_MBMC vs beta_CB (raw params, uncorrected)
r, p = pearsonr(R[:, PN.index('MB_B')], R[:, PN.index('CB')])
rs, ps = spearmanr(R[:, PN.index('MB_B')], R[:, PN.index('CB')])
print(f'beta_MBMC vs beta_CB: pearson r={r:.3f} p={p:.3f} | spearman rho={rs:.3f} p={ps:.3f}')
