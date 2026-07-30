"""
Parameter recovery for the winning MBMC model
(MBMC_Breadth2_Depth_CCRF_CB_CP; likelihood
 MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution).

Procedure (identical to model_fitting.py): sample broad ground-truth parameters
for N synthetic subjects — each from the same functional form used in the
fitting (gamma/beta/normal) — generate fully synthetic task templates matching
the experiment's structure (60 trials, blocked goal order 20 x depth-3 /
20 x depth-2 / 20 x depth-1; no real-subject data), simulate choice data with
the model's own generative process — give-up-control transitions land on the
template's pre-drawn random states (the actually-experienced environment
randomness), take-control transitions follow from the plan via the task
transition function — then fit the model back with the hierarchical EM
procedure. Correlate ground-truth vs. recovered posterior-mean
parameters and render a heatmap.
"""
import matplotlib
matplotlib.use('Agg')
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr, pearsonr
import recovery_common as rc
from recovery_faithful import MF_faithful_simulate
from recovery_em import em_fit, posterior_means

N_SUB = 100
SAMPLE_SIZE = 10000
CORES = max(1, (os.cpu_count() or 8) - 2)
SEED = 1
# 'faithful' -> planning-success drawn from the exact likelihood mixture (default);
# 'published' -> the original MF_ChoiceBias_MB_Breadth_Depth_simulate.
SIMULATOR = os.environ.get('SIMULATOR', '_published')
TAG = '' if SIMULATOR == 'faithful' else '_published'

# 9 parameters, in the order the likelihood indexes samples[0..8]
PARAM_INFO = [
    ['MB_B',        'gamma', [1,1]],   # beta_MBMC   (meta-control weight)
    ['MB_depth',    'beta',  [1, 1]],   # gamma_d     (discount)
    ['MB_breadth',  'beta',  [1, 1]],   # b1          (one-step breadth, raw)
    ['breadth2',    'beta',  [1, 1]],   # b2          (two-step breadth, raw)
    ['mbcache',     'gamma', [1,1]],   # kappa_C     (cache value)
    ['CB',          'norm',  [0, 1]],   # beta_CB     (choice bias)
    ['forget',      'gamma', [1,1]],   # gamma_C     (cache forgetting)
    ['cache_reward','norm',  [0, 1]],   # kappa_R     (reward effect on cache)
    ['cache_plan',  'gamma', [1,1]],   # omega_P     (cached plan execution)
]
SYMBOLS = [r'$\beta_{\mathrm{MBMC}}$', r'$\gamma_d$', r'$\tilde b_1$', r'$\tilde b_2$',
           r'$\kappa_C$', r'$\beta_{\mathrm{CB}}$', r'$\gamma_C$', r'$\kappa_R$',
           r'$\omega_P$']

# Broad ground-truth distributions matched to each parameter's fitted functional
# form (same parameterizations as recovery_em.refit: gamma -> (shape, scale),
# beta -> (a, b) on [0,1], norm -> (mean, sd)), each set wide enough to span the
# plausible parameter range.
GROUND_TRUTH = {
    'mb_control':  ('gamma', (8,0.2)),    # mean 3.0, sd 2.1  (~0-7+)
    'discount':    ('beta',  (2,1)),    # mean 0.67, mass over ~0.2-1.0
    'breadth1':    ('beta',  (2,1)),    # broad over (0, 1)
    'breadth2':    ('beta',  (1,1)),    # broad over (0, 1)
    'mb_cache':    ('gamma', (2,1)),   # mean 1.5, sd 1.1  (~0-3+)
    'choice_bias': ('norm',  (0.5,0.5)),    # ~(-2, 2)
    'forget':      ('gamma', (1,1)),  # mean 1.0, sd 1.0  (~0-3.7), matches fitting family
    'cache_reward':('norm',  (0.5,0.5)),    # ~(-2, 2)
    'cache_plan':  ('gamma', (2,1)),    # mean 1.0, sd 0.7  (~0-2+)
}


def sample_truth(rng, key, n):
    dist, (h1, h2) = GROUND_TRUTH[key]
    if dist == 'gamma':
        return rng.gamma(h1, h2, n)
    if dist == 'beta':
        return rng.beta(h1, h2, n)
    return rng.normal(h1, h2, n)


# ---- synthetic task templates (no real-subject data) ----
# Same design as the experiment: 60 trials, blocked goal order
# (20 x depth-3, 20 x depth-2, 20 x depth-1), 3 decisions per trial.
# The template pre-draws the environment's randomness as a uniform random walk
# over the task graph: on give-up-control the simulators transition to the
# template's pre-drawn (actually-experienced) state, which the fit then
# conditions on. Take-control transitions are action-driven: optimal if the
# plan succeeded, fresh random otherwise.
DEPTH_BLOCKS = [3] * 20 + [2] * 20 + [1] * 20


# Empirical task graph, verified against every real-subject trajectory in
# lmm_fixed.csv (~9,800 trials): bowtie is only reachable from baby, car only
# from toothbrush, backpack from both.
TASK_GRAPH = {'start':      {'toothbrush', 'baby'},
              'toothbrush': {'backpack', 'car'},
              'baby':       {'bowtie', 'backpack'}}


def check_transitions(sim_df):
    """Assert every simulated state transition exists in the empirical task
    graph; called on the simulator output before fitting."""
    w = sim_df.pivot_table(index=['sub', 'trial_num'], columns='decision',
                           values='current_state', aggfunc='first')
    s1, s2, s3 = w[1], w[2], w[3]
    assert (s1 == 'start').all(), 'trial not starting at start'
    bad = (~pd.concat([s1, s2], axis=1).apply(
               lambda r: r[2] in TASK_GRAPH[r[1]], axis=1) |
           ~pd.concat([s2, s3], axis=1).apply(
               lambda r: r[3] in TASK_GRAPH[r[2]], axis=1))
    assert not bad.any(), ('simulated transitions violate the empirical task '
                           'graph in %d trials' % int(bad.sum()))
    print('Transition check: all %d simulated trials respect the empirical '
          'task graph.' % len(w))


def make_template(rng):
    """One synthetic subject dataframe with the columns the simulators read:
    trial_num, trial_num_within_goal, planning_depth, decision, current_state
    (the pre-drawn random walk the environment follows on give-up-control),
    RT and got_to_goal (read but unused)."""
    rows = []
    for t, depth in enumerate(DEPTH_BLOCKS):
        s2 = sorted(TASK_GRAPH['start'])[rng.integers(2)]
        s3 = sorted(TASK_GRAPH[s2])[rng.integers(2)]
        states = ['start', 'images/%s.png' % s2, 'images/%s.png' % s3]
        for d in (1, 2, 3):
            rows.append({'sub': 0, 'trial_num': t + 1,
                         'trial_num_within_goal': t % 20 + 1,
                         'planning_depth': depth, 'decision': d,
                         'current_state': states[d - 1],
                         'RT': 0.0, 'got_to_goal': 0})
    return pd.DataFrame(rows)


def main():
    rng = np.random.default_rng(SEED)
    templates = [make_template(rng) for _ in range(N_SUB)]

    truth = {k: sample_truth(rng, k, N_SUB) for k in GROUND_TRUTH}
    # simulator wants breadth on the *8 / *4 scale; everything else raw
    sim_params = [truth['mb_control'], truth['discount'],
                  truth['breadth1'] * 8, truth['breadth2'] * 4,
                  truth['mb_cache'], truth['choice_bias'], truth['forget'],
                  truth['cache_reward'], truth['cache_plan']]
    # ground-truth matrix aligned to PARAM_INFO order (raw breadth, matches recovered)
    T = np.column_stack([truth['mb_control'], truth['discount'], truth['breadth1'],
                         truth['breadth2'], truth['mb_cache'], truth['choice_bias'],
                         truth['forget'], truth['cache_reward'], truth['cache_plan']])

    print('Simulating %d subjects (broad form-matched ground truth, %s simulator)...'
          % (N_SUB, SIMULATOR))
    simulate = (MF_faithful_simulate if SIMULATOR == 'faithful'
                else rc.MF_ChoiceBias_MB_Breadth_Depth_simulate)
    sim = simulate(sim_params, templates)
    sim_df = pd.DataFrame(sim)
    check_transitions(sim_df)
    sim_dfs = [sim_df[sim_df['sub'] == s].reset_index(drop=True)
               for s in sim_df['sub'].unique()]

    print('Fitting winning model (EM, ss=%d, cores=%d)...' % (SAMPLE_SIZE, CORES))
    lik = rc.MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution
    ibic, results, fitted = em_fit(sim_dfs, PARAM_INFO, lik,
                                   sample_size=SAMPLE_SIZE, cores=CORES,
                                   verbose=True)
    R = posterior_means(results, PARAM_INFO)   # N x 9 recovered posterior means
    np.savez('recovery_parameter_arrays%s.npz' % TAG, truth=T, recovered=R,
             symbols=np.array(SYMBOLS))

    # Individual-level recovery is reported only for the parameters linked to
    # individual differences in the manuscript: choice bias, breadth2, beta_MBMC.
    # (The full truth/recovered arrays are still saved in the npz above.)
    FOCAL = [5, 3, 0]   # CB, breadth2, MB_B — indices into PARAM_INFO order
    focal_symbols = [SYMBOLS[i] for i in FOCAL]
    Tf, Rf = T[:, FOCAL], R[:, FOCAL]

    # Spearman rank correlation: rows = ground truth, cols = recovered
    P = len(FOCAL)
    C = np.zeros((P, P))
    for i in range(P):
        for j in range(P):
            C[i, j] = spearmanr(Tf[:, i], Rf[:, j]).correlation

    rec = pd.DataFrame({'parameter': focal_symbols,
                        'recovery_rho (diagonal)': np.round(np.diag(C), 3)})
    print('\nParameter recovery, individual-difference parameters '
          '(diagonal Spearman rho):')
    print(rec.to_string(index=False))
    pd.DataFrame(C, index=focal_symbols, columns=focal_symbols).to_csv(
        'recovery_parameter_corr%s.csv' % TAG)

    # ---- heatmap ----
    sns.set(style='white', font_scale=1.6)
    plt.figure(figsize=(6.5, 5.5))
    ann = np.vectorize(lambda x: ('%.2f' % x).replace('0.', '.').replace('-.', '-.'))(C)
    ax = sns.heatmap(C, annot=ann, fmt='', cmap='coolwarm', vmin=-1, vmax=1,
                     linewidths=0.5, square=True,
                     xticklabels=focal_symbols, yticklabels=focal_symbols,
                     cbar_kws={'label': r'Spearman $\rho$', 'shrink': 0.8})
    ax.set_xlabel('Recovered parameter')
    ax.set_ylabel('Ground-truth parameter')
    ax.tick_params(axis='x', rotation=0)
    ax.tick_params(axis='y', rotation=0)
    plt.title('Parameter recovery (N=%d)' % N_SUB)
    plt.tight_layout()
    plt.savefig('recovery_parameter_heatmap%s.png' % TAG, dpi=300, bbox_inches='tight')
    plt.close()
    print('\nSaved: recovery_parameter_heatmap%s.png, recovery_parameter_corr%s.csv'
          % (TAG, TAG))


if __name__ == '__main__':
    main()
