"""
Gated b1/b2 model: (1) fit Study 2, (2) parameter recovery, (3) model-agnostic
analyses. Hierarchical EM, ss=10000 throughout.
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
from scipy.stats import pearsonr, spearmanr

from recovery_common import basename_without_ext
from recovery_em import em_fit, posterior_means
import recovery_parameter as RP
import gated_soft as GB

SSAMP = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
MAXITER = 30
BASELINES = {'original k=9': 11373.4, 'hard-split k=8': 11377.0,
             'staged k=8': 11516.8, 'start+step k=9': 11499.6, 'gated k=9': 11428.5, 'gated-sat k=9': 11403.6}


def stage1():
    d = pd.read_csv('lmm_fixed.csv')
    d['current_state'] = d['current_state'].map(basename_without_ext)
    subs = d['sub'].unique()
    dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
    print(f'[stage1] fitting SOFT-gated + tailored saturation (k=9, ss={SSAMP}) to {len(dfs)} subjects',
          flush=True)
    t0 = time.time()
    ibic, results, _ = em_fit(dfs, GB.PARAM_INFO_GSOFT, GB.gatedsoft_lik, sample_size=SSAMP,
                              cores=CORES, max_iter=MAXITER, verbose=True, seed0=1)
    R = posterior_means(results, GB.PARAM_INFO_GSOFT)
    np.save('em_params_study2_MBMCgatedsoft.npy', R)
    print(f'[stage1] GATED-SOFT iBIC={ibic:.1f} ({time.time()-t0:.0f}s)', flush=True)
    for k, v in BASELINES.items():
        print(f'    vs {k}: {v} (delta {ibic-v:+.1f})', flush=True)
    b1 = R[:, GB.PN_GSOFT.index('MB_breadth')]
    b2 = R[:, GB.PN_GSOFT.index('breadth2')]
    print(f'[stage1] b1 median={np.median(b1):.3f} IQR=[{np.percentile(b1,25):.3f},'
          f'{np.percentile(b1,75):.3f}] | b2 median={np.median(b2):.3f} '
          f'IQR=[{np.percentile(b2,25):.3f},{np.percentile(b2,75):.3f}]', flush=True)
    return subs, R


N_SUB, N_ITER, BASE_SEED = 60, 10, 10300
SYMBOLS = [r'$\beta_{\mathrm{MBMC}}$', r'$\gamma_d$', r'$\tilde b_1$',
           r'$\tilde b_2$ (gated)', r'$\kappa_C$', r'$\beta_{\mathrm{CB}}$',
           r'$\gamma_C$', r'$\kappa_R$', r'$\omega_P$']


def stage2():
    P = len(GB.PARAM_INFO_GSOFT)
    mats = []
    for it in range(N_ITER):
        rng = np.random.default_rng(BASE_SEED + it)
        templates = [RP.make_template(rng) for _ in range(N_SUB)]
        gt = {k: RP.sample_truth(rng, k, N_SUB) for k in RP.GROUND_TRUTH}
        T = np.column_stack([gt['mb_control'], gt['discount'], gt['breadth1'],
                             gt['breadth2'], gt['mb_cache'], gt['choice_bias'],
                             gt['forget'], gt['cache_reward'], gt['cache_plan']])
        sim_params = [gt['mb_control'], gt['discount'], gt['breadth1'] * 8,
                      gt['breadth2'] * 4, gt['mb_cache'], gt['choice_bias'],
                      gt['forget'], gt['cache_reward'], gt['cache_plan']]
        sim_df = pd.DataFrame(GB.gatedsoft_simulate(sim_params, templates))
        dfs = [sim_df[sim_df['sub'] == s].reset_index(drop=True)
               for s in sim_df['sub'].unique()]
        t0 = time.time()
        ibic, results, _ = em_fit(dfs, GB.PARAM_INFO_GSOFT, GB.gatedsoft_lik, sample_size=SSAMP,
                                  cores=CORES, max_iter=MAXITER, verbose=False,
                                  seed0=(BASE_SEED + it) * 1000)
        R = posterior_means(results, GB.PARAM_INFO_GSOFT)
        C = np.zeros((P, P))
        for i in range(P):
            for j in range(P):
                C[i, j] = pearsonr(T[:, i], R[:, j])[0]
        mats.append(C)
        print(f'[stage2] iter {it+1}/{N_ITER} iBIC={ibic:.1f} b1 r={C[2,2]:.3f} '
              f'b2 r={C[3,3]:.3f} ({time.time()-t0:.0f}s)', flush=True)
    mats = np.stack(mats)
    Cmean, Cstd = np.nanmean(mats, 0), np.nanstd(mats, 0)
    pd.DataFrame(Cmean, index=SYMBOLS, columns=SYMBOLS).to_csv(
        'recovery_gatedsoft_corr_mean.csv')
    print('[stage2] mean diagonal:', flush=True)
    for s, dg, sd in zip(SYMBOLS, np.diag(Cmean), np.diag(Cstd)):
        print('   %-26s %.3f (SD %.3f)' % (s, dg, sd), flush=True)
    sns.set(style='white', font_scale=1.2)
    plt.figure(figsize=(9.2, 7.8))
    ann = np.vectorize(lambda x: ('%.2f' % x).replace('0.', '.'))(Cmean)
    ax = sns.heatmap(Cmean, annot=ann, fmt='', cmap='coolwarm', vmin=-1, vmax=1,
                     linewidths=0.5, square=True, xticklabels=SYMBOLS,
                     yticklabels=SYMBOLS,
                     cbar_kws={'label': r'mean Pearson $r$ (%d iters)' % N_ITER,
                               'shrink': 0.82})
    ax.set_xlabel('Recovered parameter'); ax.set_ylabel('Ground-truth parameter')
    ax.tick_params(axis='x', rotation=25); plt.setp(ax.get_xticklabels(), ha='right')
    plt.title('Parameter recovery, gated + state-tailored saturation\n(mean over %d iterations, N=%d)'
              % (N_ITER, N_SUB))
    plt.tight_layout()
    plt.savefig('recovery_gatedsoft_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('[stage2] saved recovery_gatedsoft_heatmap.png', flush=True)


def stage3(subs, R):
    d = pd.read_csv('lmm_fixed.csv')
    dfs = [d[d['sub'] == s].reset_index(drop=True) for s in subs]
    p9 = [R[:, 0], R[:, 1], R[:, 2] * 8, R[:, 3] * 4, R[:, 4], R[:, 5], R[:, 6],
          R[:, 7], R[:, 8]]
    sim = pd.DataFrame(GB.gatedsoft_simulate(p9, dfs))
    sim.to_csv('simulated_data_gatedsoft.csv', index=False)
    sim['planning depth'] = sim['planning_depth']

    sns.set(style='white', font_scale=3.6, palette='Set2')
    plt.figure(figsize=(9, 7))
    ax = sns.barplot(x='planning depth', y='control choice', hue='decision', data=sim)
    for bg, ds in zip(ax.containers, [0.33, 0.667, 1]):
        for bar, color in zip(bg, plt.cm.Set2.colors):
            bar.set_facecolor(sns.desaturate(color, ds))
    if ax.get_legend():
        ax.get_legend().remove()
    plt.tight_layout()
    plt.savefig('MODELsimulated_GATEDSOFT_Control_by_planningdepth.png', dpi=300,
                bbox_inches='tight')
    plt.close()

    palettes = {1: [(0.5209, 0.6399, 0.6024), (0.4601, 0.7007, 0.6249), (0.4, 0.7608, 0.6471)],
                2: [(0.7859, 0.6423, 0.5866), (0.8877, 0.5973, 0.4849), (0.9882, 0.5529, 0.3843)],
                3: [(0.6344, 0.6590, 0.7146), (0.5934, 0.6431, 0.7556), (0.5529, 0.6275, 0.7961)]}
    sns.set(style='white', font_scale=2.5)
    for depth in (1, 2, 3):
        g = sns.lmplot(data=sim[sim['planning_depth'] == depth], x='trial',
                       y='control choice', hue='decision', palette=palettes[depth],
                       logistic=True, scatter=False, legend=False)
        for axs in g.axes.flat:
            axs.set_xticks([1, 5, 10, 15, 20]); axs.set_yticks([0, 0.5, 1])
        plt.savefig(f'controlTaking_by_time_depth{depth}_SIM_GATEDSOFT.png', dpi=300,
                    bbox_inches='tight')
        plt.close()
    print('[stage3] saved barplot + 3 time-course figures', flush=True)

    real = pd.read_csv('lmm_fixed.csv'); real['cc'] = 1 - real['choice_numeric']
    sim['twg'] = sim['trial_num_within_goal']; real['twg'] = real['trial_num_within_goal']
    print('[stage3] early->late control choice (real | soft-gated sim):', flush=True)
    for (g_, d_) in [(1, 1), (1, 2), (2, 1), (3, 1)]:
        out = []
        for df_, col in [(real, 'cc'), (sim, 'control choice')]:
            s = df_[(df_.planning_depth == g_) & (df_.decision == d_)]
            out.append(f"{s[s.twg <= 5][col].mean():.2f}->{s[s.twg > 15][col].mean():.2f}")
        print(f'   depth{g_} d{d_}:  real {out[0]}   sim {out[1]}', flush=True)

    import arviz as az
    t = az.from_netcdf('RTdata_model_fitted_withintrial2.nc')
    post = t.posterior if hasattr(t, 'posterior') else t['posterior']
    nb = pd.read_csv('preprocessed_data.csv')
    _, nc_subs = pd.factorize(nb['sub'])
    idx = {s: i for i, s in enumerate(nc_subs)}
    keep = [i for i, s in enumerate(subs) if s in idx]
    order = [idx[subs[i]] for i in keep]
    print('[stage3] correlations with RT-LMM random slopes:', flush=True)
    for pname, col in [('b1', 2), ('b2', 3), ('beta_MBMC', 0), ('beta_CB', 5)]:
        pv = R[:, col][keep]
        for v, vl in [('slope_sub_dp', 'delayed planning'),
                      ('slope_sub_interaction', 'dp x trial')]:
            re_ = post[v].mean(dim=('chain', 'draw')).values[order]
            r, p_ = pearsonr(pv, re_)
            rho, ps_ = spearmanr(pv, re_)
            print(f'   {pname:10s} vs {vl:18s} r={r:+.3f} (p={p_:.4f})  '
                  f'rho={rho:+.3f} (p={ps_:.4f})', flush=True)


if __name__ == '__main__':
    subs, R = stage1()
    stage2()
    stage3(subs, R)
    print('ALL STAGES DONE', flush=True)
