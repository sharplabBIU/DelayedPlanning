#!/usr/bin/env python
# coding: utf-8
"""
run_map.py  --  FAST per-subject MAP model comparison (no Laplace Hessian, no HBI).

A lightweight alternative to `run_cbm.py`: each subject is fit by plain MAP
(penalised maximum likelihood) with L-BFGS-B, parallelised across cores.  MBMC
is warm-started from its *per-subject* EM fit (`study*/*_exec.npy`), so it
converges in one shot.  The model comparison is BIC-based:

    BIC_i = -2 * loglik_i(MAP) + k * ln(n_obs_i)        (n_obs = 180 decisions)

summed over subjects, reported as ΔBIC vs MBMC (the quantity Reviewer 1 asked
for).  Outputs are written in the SAME schema as `run_cbm.py`, so the notebook
works unchanged:

    fits_<study>.csv          per-subject loglik / bic for every model
    group_<study>.csv         ΣBIC, ΔBIC vs MBMC, Σloglik, ...
    map_params_<study>_<MODEL>.npy   N×d MAP parameters (unconstrained)

Usage
-----
    python run_map.py study1
    python run_map.py study2 --models MBMC,SR,PR,CB
"""

import os
import sys
import time
import argparse
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from multiprocessing import Pool, cpu_count

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cbm_models as M

PRIOR_VAR = 6.25                       # weak zero-mean Gaussian prior (MAP regulariser)
_EM_FILES = {'MB_B': 'MB_B', 'MB_depth': 'MB_depth', 'MB_breadth': 'MB_breadth',
             'breadth2': 'breadth2', 'mbcache': 'mbcache', 'CB': 'CB',
             'forgetC': 'forget', 'cache_reward': 'cache_reward',
             'cache_plan': 'cache_plan'}

_G = {}                                # per-worker globals


def _to_unconstrained(native, t):
    native = float(native)
    if t == 'pos':
        return float(np.log(max(native, 1e-6)))
    if t == 'unit':
        p = min(max(native, 1e-4), 1 - 1e-4)
        return float(np.log(p / (1 - p)))
    return native


def mbmc_em_inits(study_dir, N):
    """Per-subject unconstrained MBMC init from the EM `*_exec.npy` fits, or None."""
    md = M.build_models()['MBMC']
    cols = []
    for p, t in zip(md['params'], md['types']):
        f = os.path.join(study_dir, f'{_EM_FILES[p]}_exec.npy')
        if not os.path.exists(f):
            return None
        a = np.asarray(np.load(f, allow_pickle=True), dtype=float)
        if len(a) != N:
            return None
        cols.append([_to_unconstrained(v, t) for v in a])
    return np.array(cols, dtype=float).T            # N x d unconstrained


def _init_worker(study_dir):
    data, subs = M.load_subject_data(study_dir)
    _G['data'] = data
    _G['models'] = M.build_models()


def _fit_task(task):
    nm, i, raw_init, n_random, maxiter, seed = task
    md = _G['models'][nm]
    f, d = md['func'], md['npar']
    data_sub = _G['data'][i]
    prior_prec = 1.0 / PRIOR_VAR

    def negpost(raw):
        ll = f(raw, data_sub)
        lp = -0.5 * prior_prec * float(np.dot(raw, raw))
        return -(ll + lp)

    rng = np.random.RandomState(seed)
    starts = [np.asarray(raw_init, float) if raw_init is not None else np.zeros(d)]
    for _ in range(n_random):
        starts.append(rng.randn(d) * 0.5)

    best = None
    for x0 in starts:
        try:
            r = minimize(negpost, x0, method='L-BFGS-B', options={'maxiter': maxiter})
            if best is None or r.fun < best.fun:
                best = r
        except Exception:
            pass
    raw = best.x if best is not None else starts[0]
    ll = f(raw, data_sub)
    return nm, i, np.asarray(raw, float), float(ll)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('study', choices=['study1', 'study2'])
    ap.add_argument('--models', default='MBMC,SR,PR,CB')
    ap.add_argument('--outdir', default=os.path.join(HERE, 'results'))
    args = ap.parse_args()

    models = [m.strip() for m in args.models.split(',') if m.strip()]
    os.makedirs(args.outdir, exist_ok=True)
    study_dir = os.path.join(HERE, '..', args.study)

    MODELS = M.build_models()
    data, subs = M.load_subject_data(study_dir)
    N = len(subs)
    print(f'[{args.study}] {N} subjects, {len(data[0])} rows/subject, models={models}',
          flush=True)

    em = mbmc_em_inits(study_dir, N)   # N x d or None
    print(f'[{args.study}] MBMC EM warm-start available: {em is not None}', flush=True)

    # build task list (model x subject)
    tasks = []
    for nm in models:
        d = MODELS[nm]['npar']
        for i in range(N):
            if nm == 'MBMC' and em is not None:
                # warm-started at the per-subject EM optimum -> few steps needed
                raw_init, n_random, maxiter = em[i], 0, 30
            else:
                raw_init, n_random, maxiter = None, 2, 200
            tasks.append((nm, i, raw_init, n_random, maxiter, 1000 + i))

    ncores = max(1, cpu_count() - 1)
    t0 = time.time()
    with Pool(processes=ncores, initializer=_init_worker, initargs=(study_dir,)) as pool:
        results = pool.map(_fit_task, tasks, chunksize=1)
    print(f'[{args.study}] fit {len(tasks)} subject-models on {ncores} cores '
          f'in {time.time()-t0:.1f}s', flush=True)

    # assemble
    raw_params = {nm: np.zeros((N, MODELS[nm]['npar'])) for nm in models}
    rows = []
    for nm, i, raw, ll in results:
        raw_params[nm][i] = raw
        d = MODELS[nm]['npar']
        n_obs = int(len(data[i]))
        bic = -2.0 * ll + d * np.log(n_obs)
        rows.append(dict(study=args.study, model=nm, sub=str(subs[i]), npar=d,
                         loglik=ll, lme=ll, bic=bic, n_obs=n_obs))
    fits = pd.DataFrame(rows)
    fits.to_csv(os.path.join(args.outdir, f'fits_{args.study}.csv'), index=False)
    for nm in models:
        np.save(os.path.join(args.outdir, f'map_params_{args.study}_{nm}.npy'),
                raw_params[nm])

    # group summary, ΔBIC vs MBMC
    g = (fits.groupby('model')
              .agg(npar=('npar', 'first'), sum_loglik=('loglik', 'sum'),
                   sum_lme=('lme', 'sum'), sum_bic=('bic', 'sum'),
                   n_sub=('sub', 'nunique')).reset_index())
    ref = 'MBMC' if 'MBMC' in g['model'].values else g.sort_values('sum_bic').iloc[0]['model']
    g['delta_BIC_vs_MBMC'] = g['sum_bic'] - g.loc[g['model'] == ref, 'sum_bic'].values[0]
    g['delta_LME_vs_MBMC'] = g['sum_lme'] - g.loc[g['model'] == ref, 'sum_lme'].values[0]
    g['study'] = args.study
    g = g.sort_values('sum_bic').reset_index(drop=True)
    g.to_csv(os.path.join(args.outdir, f'group_{args.study}.csv'), index=False)

    print(f'\n[{args.study}] MAP model comparison:')
    print(g[['model', 'npar', 'sum_loglik', 'sum_bic', 'delta_BIC_vs_MBMC']]
          .to_string(index=False), flush=True)
    print(f'\n[{args.study}] ALL DONE in {time.time()-t0:.1f}s', flush=True)


if __name__ == '__main__':
    main()
