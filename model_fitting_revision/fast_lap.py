"""
Fast Laplace fits for CBM/HBI.

cbm.individual_fit is exact but does ~1450 likelihood evals/subject (the ~20 ms
likelihood then costs ~40 s/subject -> infeasible for 20 models). Here we instead:
  * warm-start each subject at its per-subject EM fit (study2/*_exec.npy),
  * find the MAP with L-BFGS-B (+ a couple of random restarts),
  * build the Laplace approximation from a central finite-difference Hessian of the
    negative log-posterior at the MAP,
using the SAME log-posterior / Laplace-evidence formula as cbm.individual_fit
(lme = logpost(MAP) + 0.5 d ln 2pi - 0.5 log|H|). The result is packaged as a cbm
FitResult so cbm.hbi_main consumes it unchanged. Subjects run in parallel (fork).
"""
import os
import time
import pickle
import numpy as np
import multiprocessing as mp
from datetime import datetime
from scipy.optimize import minimize

from cbm.map_estimation import log_posterior
from cbm.individual_fit import FitResult, FitMath, FitOutput, FitInput, FitProfile
from cbm.optimization import Config

HERE = os.path.dirname(os.path.abspath(__file__))
_EM = {'MB_B': 'MB_B', 'MB_depth': 'MB_depth', 'MB_breadth': 'MB_breadth',
       'breadth2': 'breadth2', 'mbcache': 'mbcache', 'CB': 'CB', 'forgetC': 'forget',
       'forget': 'forget', 'cache_reward': 'cache_reward', 'cache_plan': 'cache_plan'}
_G = {}                                       # per-worker globals (fork-shared)


def _unc(v, t):
    if t == 'pos':
        return float(np.log(max(float(v), 1e-6)))
    if t == 'unit':
        p = min(max(float(v), 1e-4), 1 - 1e-4)
        return float(np.log(p / (1 - p)))
    return float(v)


def em_inits(study_dir, params, types, n):
    """Per-subject warm-start init matrix (n x d): EM fit where available, else 0."""
    d = len(params)
    W = np.zeros((n, d))
    for j, (p, t) in enumerate(zip(params, types)):
        f = os.path.join(study_dir, f'{_EM[p]}_exec.npy') if p in _EM else None
        if f and os.path.exists(f):
            a = np.asarray(np.load(f, allow_pickle=True), dtype=float).ravel()
            for i in range(n):
                W[i, j] = _unc(a[i % len(a)], t)
    return W


def _hessian(neg, x, h=1e-3):
    d = len(x)
    f0 = neg(x)
    H = np.zeros((d, d))
    e = np.eye(d) * h
    fp = np.array([neg(x + e[i]) for i in range(d)])
    fm = np.array([neg(x - e[i]) for i in range(d)])
    for i in range(d):
        H[i, i] = (fp[i] - 2 * f0 + fm[i]) / h ** 2
    for i in range(d):
        for j in range(i + 1, d):
            fpp = neg(x + e[i] + e[j]); fmm = neg(x - e[i] - e[j])
            fpm = neg(x + e[i] - e[j]); fmp = neg(x - e[i] + e[j])
            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4 * h ** 2)
    H = 0.5 * (H + H.T)
    # ensure positive-definite (floor eigenvalues)
    w, V = np.linalg.eigh(H)
    if np.any(w < 1e-6):
        w = np.clip(w, 1e-6, None)
        H = (V * w) @ V.T
    return H


def _fit_one(args):
    i, init = args
    func, data, prior_mean, prior_prec, d, nrestart, seed, mit = (
        _G['func'], _G['data'][i], _G['pm'], _G['pp'], _G['d'], _G['nr'],
        _G['seed'], _G['maxiter'])
    neg = lambda p: -log_posterior(np.asarray(p, float), func, data, prior_mean, prior_prec)
    rng = np.random.default_rng(seed + i)
    starts = [init] + [init + rng.normal(0, 0.5, d) for _ in range(nrestart)]
    best = None
    for x0 in starts:
        try:
            r = minimize(neg, x0, method='L-BFGS-B',
                         options={'maxiter': mit, 'maxfun': mit * (d + 1)})
            if np.isfinite(r.fun) and (best is None or r.fun < best.fun):
                best = r
        except Exception:
            continue
    if best is None:
        best = type('R', (), {'x': init, 'fun': neg(init)})()
    xm = np.asarray(best.x, float)
    H = _hessian(neg, xm)
    logpost = log_posterior(xm, func, data, prior_mean, prior_prec)   # positive
    logdetH = np.linalg.slogdet(H)[1]
    lme = logpost + 0.5 * d * np.log(2 * np.pi) - 0.5 * logdetH
    hinv_diag = np.diag(np.linalg.inv(H))
    return i, xm, logpost, lme, hinv_diag, logdetH, H


def build_lap(name, entry, data, study_dir, prior_var=6.25, cores=12,
              nrestart=2, seed=0, outdir=None, maxiter=60):
    d = entry['npar']
    W = em_inits(study_dir, entry['params'], entry['types'], len(data))
    _G.update(func=entry['func'], data=data, pm=np.zeros(d),
              pp=np.eye(d) / prior_var, d=d, nr=nrestart, seed=seed, maxiter=maxiter)
    ctx = mp.get_context('fork')
    with ctx.Pool(cores) as pool:
        res = pool.map(_fit_one, [(i, W[i]) for i in range(len(data))])
    res.sort(key=lambda r: r[0])
    N = len(data)
    params = [r[1] for r in res]
    loglik = np.array([r[2] for r in res])
    lme = np.array([r[3] for r in res])
    hinv = [r[4] for r in res]
    logdet = np.array([r[5] for r in res])
    hess = [r[6] for r in res]

    math = FitMath(loglik=loglik, parameters=params, hessian=hess, lme=lme,
                   hessian_inv_diag=hinv, log_det_hessian=logdet,
                   flag=np.ones(N), gradient=np.zeros((d, N)))
    out = FitOutput(parameters=np.array(params), log_evidence=lme)
    fit = FitResult(method='fast_lap', input=FitInput(name, np.zeros(d),
                    np.eye(d) / prior_var, None),
                    profile=FitProfile(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                       'fast_lap', 0.0, Config(d=d), np.zeros(d),
                                       np.eye(d) / prior_var),
                    math=math, output=out)
    if outdir:
        fn = os.path.join(outdir, f'lap_full_{name}.pkl')
        with open(fn, 'wb') as f:
            pickle.dump(fit, f)
        return fit, fn
    return fit, None
