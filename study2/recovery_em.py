"""
Shared EM driver for parameter- and model-recovery, reusing the exact fitting
procedure from model_fitting.py / simulate_full_model.py (imported via
recovery_common). The only model-object-dependent step (M-step hyperparameter
refitting) is replicated verbatim from fit_hyperparameters_parallel.
"""
import numpy as np
import multiprocessing as mp
from scipy.stats import beta as beta_d, gamma as gamma_d, norm as norm_d, uniform as uniform_d
import recovery_common as rc

NUM_TRIALS = 60  # trials per subject (3 goals x 20), as in the fitting code
try:
    _CTX = mp.get_context('fork')      # true parallelism; ~12x over threads
except ValueError:                     # pragma: no cover
    _CTX = mp.get_context()


def _seeded_process(args):
    """Worker wrapper: reseed NumPy per (iteration, subject) so fork'd children do
    not all inherit the same RNG state, then run the standard process_subject."""
    subject, pinfo, data, lik, ss, seed = args
    np.random.seed(seed % (2 ** 32))
    return rc.process_subject(subject, pinfo, data, lik, ss)


def refit(dist, samples):
    """Refit group hyperparameters for one parameter — identical to
    fit_hyperparameters_parallel in the fitting code."""
    samples = np.asarray(samples, dtype=float)
    if dist == 'gamma':
        h = gamma_d.fit(samples, floc=0);            return [h[0], h[2]]
    if dist == 'uniform':
        h = uniform_d.fit(samples);                  return [h[0], h[1] + h[0]]
    if dist == 'norm':
        h = norm_d.fit(samples);                     return [h[0], h[1]]
    s = np.clip(samples, 1e-5, 0.99999)
    h = beta_d.fit(s, floc=0, fscale=1);             return [h[0], h[1]]


def em_fit(sim_dfs, param_info, lik, sample_size=4000, cores=6, max_iter=30,
           verbose=False, seed0=0):
    """Hierarchical EM fit (same loop as model_fitting.py). param_info is a list of
    [name, distribution, [h1, h2]]; hyperparameters are updated in place each iter.
    Returns (best_ibic, best_results, fitted_param_info)."""
    N = len(sim_dfs)
    pinfo = [[n, d, list(h)] for (n, d, h) in param_info]  # deep copy
    bic = 1e12
    best = (bic, None, pinfo)
    for it in range(max_iter):
        old_bic = bic
        tasks = [(i, pinfo, sim_dfs, lik, sample_size, seed0 + it * 100003 + i * 7919)
                 for i in range(N)]
        with _CTX.Pool(cores) as pool:
            results = pool.map(_seeded_process, tasks)
        # M-step: refit each parameter's group hyperparameters
        for pi in range(len(pinfo)):
            name, dist, _ = pinfo[pi]
            samp = []
            for r in results:
                for item in r[2:]:
                    if item[0] == name:
                        samp += item[3]
            pinfo[pi][2] = refit(dist, samp)
        total_evidence = sum(r[1][0] for r in results)
        nparams = 2 * len(pinfo)
        bic = -2.0 * float(total_evidence) + nparams * np.log(N * NUM_TRIALS)
        if bic < best[0]:
            best = (bic, results, [[n, d, list(h)] for (n, d, h) in pinfo])
        if verbose:
            print('    iter %2d  iBIC=%.1f  (evidence=%.1f)' % (it, bic, total_evidence))
        if old_bic - bic <= 0:
            break
    return best  # (ibic, results, fitted_param_info)


def posterior_means(results, param_info):
    """(n_subjects x n_params) matrix of posterior-mean parameters, columns in the
    order of param_info."""
    names = [p[0] for p in param_info]
    M = np.full((len(results), len(names)), np.nan)
    for si, r in enumerate(results):
        for item in r[2:]:
            if item[0] in names:
                M[si, names.index(item[0])] = item[1]
    return M
