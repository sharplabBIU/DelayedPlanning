#!/usr/bin/env python
# coding: utf-8
"""
run_cbm.py  --  fit the revision-1 model set with CBM (Piray) for one study.

Usage
-----
    python run_cbm.py study1            # Laplace (cbm_lap) + HBI
    python run_cbm.py study2 --no-hbi   # Laplace only
    python run_cbm.py study1 --models MBMC,SR,PR,CB

Outputs (written to ./results/)
    lap_<study>_<MODEL>.pkl   CBM Laplace (MAP) fit per model (used by HBI)
    fits_<study>.csv          per-subject loglik / LME / BIC for every model
    group_<study>.csv         group summary: ΣLME, ΣBIC, ΔBIC vs MBMC, ...
    hbi_<study>.pkl           full HBIResult
    hbi_summary_<study>.pkl   compact HBI summary (freqs, exceedance, group params)

The Laplace step is saved *before* HBI starts, so the model-evidence / BIC
comparison survives even if the (slower) HBI run is interrupted.
"""

import os
import sys
import time
import pickle
import argparse
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')

import cbm_models as M
from cbm import individual_fit, hbi_main

HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR_VAR = 6.25          # CBM default broad Gaussian prior (std 2.5) on unconstrained params


def _lap_path(outdir, study, nm):
    return os.path.join(outdir, f'lap_{study}_{nm}.pkl')


# EM `*_exec.npy` file name per MBMC parameter (study folders).
_EM_FILES = {'MB_B': 'MB_B', 'MB_depth': 'MB_depth', 'MB_breadth': 'MB_breadth',
             'breadth2': 'breadth2', 'mbcache': 'mbcache', 'CB': 'CB',
             'forgetC': 'forget', 'cache_reward': 'cache_reward',
             'cache_plan': 'cache_plan'}


def _to_unconstrained(native, t):
    native = float(native)
    if t == 'pos':
        return float(np.log(max(native, 1e-6)))
    if t == 'unit':
        p = min(max(native, 1e-4), 1 - 1e-4)
        return float(np.log(p / (1 - p)))
    return native


def em_warmstart_init(study, name):
    """Return a single unconstrained init vector (group-median EM fit, 1-D
    length-d) for MBMC, or None if EM `*_exec.npy` files are unavailable."""
    if name != 'MBMC':
        return None
    study_dir = os.path.join(HERE, '..', study)
    md = MODELS[name]
    vec = []
    for p, t in zip(md['params'], md['types']):
        f = os.path.join(study_dir, f'{_EM_FILES[p]}_exec.npy')
        if not os.path.exists(f):
            return None
        a = np.asarray(np.load(f, allow_pickle=True), dtype=float)
        vec.append(_to_unconstrained(np.median(a), t))
    return np.array(vec, dtype=float)   # 1-D, length d (CBM `inits` format)


def run_laplace(study, models, data, subs, outdir, num_init=10, warmstart=False):
    """cbm_lap (Laplace/MAP) for each model; returns {name: FitResult}, [paths]."""
    results, paths = {}, []
    for nm in models:
        md = MODELS[nm]
        d = md['npar']
        fn = _lap_path(outdir, study, nm)
        if os.path.exists(fn):
            with open(fn, 'rb') as f:
                res = pickle.load(f)
            print(f'[{study}] {nm:5s}  (loaded cached Laplace fit)', flush=True)
        else:
            t = time.time()
            # `num_init` random restarts per subject.  The CBM default
            # min(7*d,100) is ~63 for the 9-param MBMC, and it *escalates* to
            # num_init_med/up for subjects that miss the strict gradient
            # tolerance -- prohibitively slow.  We fix all three equal (no
            # escalation), cap BFGS iterations and relax the gradient tolerance
            # slightly.  This is ample for these smooth likelihoods, and HBI
            # warm-start refinement runs on top.  MBMC is the expensive 9-param
            # model, so it uses fewer restarts -- it is seeded from the EM fit.
            ni = 1 if nm == 'MBMC' else num_init
            cfg = {'verbose': 0, 'num_init': ni,
                   'num_init_med': ni, 'num_init_up': ni,
                   'max_iter': 40, 'tol_grad': 0.05}
            if warmstart:
                init = em_warmstart_init(study, nm)
                if init is not None:
                    cfg['inits'] = init   # shared EM-median start point
            res = individual_fit(data, md['func'], np.zeros(d), PRIOR_VAR,
                                 fname=fn, config=cfg)
            print(f'[{study}] {nm:5s}  Laplace fit: {time.time()-t:6.1f}s '
                  f'(ΣLME={np.nansum(res.output.log_evidence):.1f})', flush=True)
        results[nm] = res
        paths.append(fn)
    return results, paths


def per_subject_table(study, models, lap_results, data, subs):
    """Pure log-likelihood at the MAP + per-subject BIC for every model."""
    rows = []
    for nm in models:
        d = MODELS[nm]['npar']
        res = lap_results[nm]
        for i in range(len(subs)):
            raw = np.asarray(res.output.parameters[i], dtype=float).ravel()
            ll = M.raw_loglik_at(nm, raw, data[i])
            n_obs = int(len(data[i]))                       # 180 decisions/subject
            bic = -2.0 * ll + d * np.log(n_obs)
            rows.append(dict(study=study, model=nm, sub=str(subs[i]), npar=d,
                             loglik=ll, lme=float(res.output.log_evidence[i]),
                             bic=bic, n_obs=n_obs))
    return pd.DataFrame(rows)


def group_summary(study, models, fits):
    """Group-level model comparison table, ΔBIC referenced to MBMC."""
    g = (fits.groupby('model')
              .agg(npar=('npar', 'first'),
                   sum_loglik=('loglik', 'sum'),
                   sum_lme=('lme', 'sum'),
                   sum_bic=('bic', 'sum'),
                   n_sub=('sub', 'nunique'))
              .reset_index())
    ref = 'MBMC' if 'MBMC' in g['model'].values else g.sort_values('sum_bic').iloc[0]['model']
    bic_ref = g.loc[g['model'] == ref, 'sum_bic'].values[0]
    lme_ref = g.loc[g['model'] == ref, 'sum_lme'].values[0]
    g['delta_BIC_vs_MBMC'] = g['sum_bic'] - bic_ref       # >0 = worse than MBMC
    g['delta_LME_vs_MBMC'] = g['sum_lme'] - lme_ref       # <0 = worse than MBMC
    g['study'] = study
    g = g.sort_values('sum_bic').reset_index(drop=True)
    return g


def run_hbi(study, models, data, lap_paths, outdir, maxiter=30):
    """Hierarchical Bayesian Inference across the model set."""
    model_funcs = [MODELS[nm]['func'] for nm in models]
    fn = os.path.join(outdir, f'hbi_{study}.pkl')
    t = time.time()
    hbi = hbi_main(data, model_funcs, lap_paths, fname=fn,
                   config={'verbose': 1, 'maxiter': maxiter})
    print(f'[{study}] HBI: {time.time()-t:6.1f}s', flush=True)
    summary = dict(
        study=study, models=list(models),
        model_frequency=np.asarray(hbi.output.model_frequency).ravel(),
        exceedance_prob=np.asarray(hbi.output.exceedance_prob).ravel(),
        protected_exceedance_prob=np.asarray(hbi.output.protected_exceedance_prob).ravel(),
        responsibility=np.asarray(hbi.output.responsibility),
        group_mean=[np.asarray(x).ravel() for x in hbi.output.group_mean],
        parameters=[np.asarray(x) for x in hbi.output.parameters],
        param_names=[MODELS[nm]['params'] for nm in models],
        param_types=[MODELS[nm]['types'] for nm in models],
    )
    with open(os.path.join(outdir, f'hbi_summary_{study}.pkl'), 'wb') as f:
        pickle.dump(summary, f)
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('study', choices=['study1', 'study2'])
    ap.add_argument('--models', default='MBMC,SR,PR,CB')
    ap.add_argument('--no-hbi', action='store_true')
    ap.add_argument('--maxiter', type=int, default=30)
    ap.add_argument('--num_init', type=int, default=10)
    ap.add_argument('--warmstart', action='store_true',
                    help='seed MBMC from the EM *_exec.npy group-median fit')
    ap.add_argument('--outdir', default=os.path.join(HERE, 'results'))
    args = ap.parse_args()

    global MODELS
    MODELS = M.build_models()
    models = [m.strip() for m in args.models.split(',') if m.strip()]
    os.makedirs(args.outdir, exist_ok=True)

    study_dir = os.path.join(HERE, '..', args.study)
    data, subs = M.load_subject_data(study_dir)
    print(f'[{args.study}] {len(subs)} subjects, {len(data[0])} rows/subject, '
          f'models={models}', flush=True)

    t0 = time.time()
    lap_results, lap_paths = run_laplace(args.study, models, data, subs, args.outdir,
                                         num_init=args.num_init, warmstart=args.warmstart)

    fits = per_subject_table(args.study, models, lap_results, data, subs)
    fits.to_csv(os.path.join(args.outdir, f'fits_{args.study}.csv'), index=False)
    grp = group_summary(args.study, models, fits)
    grp.to_csv(os.path.join(args.outdir, f'group_{args.study}.csv'), index=False)
    print(f'\n[{args.study}] group model comparison (Laplace):')
    print(grp[['model', 'npar', 'sum_loglik', 'sum_lme', 'sum_bic',
               'delta_BIC_vs_MBMC']].to_string(index=False), flush=True)

    if not args.no_hbi:
        run_hbi(args.study, models, data, lap_paths, args.outdir, maxiter=args.maxiter)

    print(f'\n[{args.study}] ALL DONE in {time.time()-t0:.1f}s', flush=True)


if __name__ == '__main__':
    main()
