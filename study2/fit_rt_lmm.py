"""Hierarchical Bayesian linear mixed model of log reaction times (Methods: "Testing whether
participants delayed planning when they delayed control"; Fig. 2D/2E; Results values
"beta_RT mode = 0.32, 95% HDI [0.21, 0.43]" and interaction "mode = 0.21, 95% HDI [0.11, 0.33]").

Standalone script version of the model defined in analysis.ipynb (cell "RT model").
The same script serves both studies:

    python fit_rt_lmm.py --study study1            # as published: 4 chains, 1000 tune, 1000 draws, target_accept 0.99
    python fit_rt_lmm.py --study study2            # as published for Study 2: target_accept 0.80 (see --target-accept)
    python fit_rt_lmm.py --study study1 --noncentered   # non-centred parameterisation of the random effects

Inputs : <study>/lmm_fixed.csv (design matrix; see data_dictionary.md)
Outputs: <study>/RTdata_model_fitted_withintrial[2].nc unless --out is given (ArviZ NetCDF trace),
         plus a printed summary (posterior mode, 95% HDI, R-hat, ESS) for the population-level coefficients.

Published traces: study1/RTdata_model_fitted_withintrial.nc (PyMC 5.16.1) and
study2/RTdata_model_fitted_withintrial2.nc (PyMC 5.22.0), both 4 chains x 1000 draws after 1000 tuning
iterations. Predictor coding: Study 1 used raw decision step (1-3) and planning depth (1-3); Study 2
centred both at 2 (as in the notebook); this only changes the intercept.

Runtime: roughly 10-30 min per study on a laptop (the published Study 1 fit took 32 min).
macOS note: with Xcode 26+ the PyTensor C compiler step may fail with "ld: library 'd64' not found";
see README (Dependencies) for the one-line workaround.
"""
import argparse, os, sys, time, warnings
import numpy as np, pandas as pd

p = argparse.ArgumentParser()
p.add_argument('--study', default=os.path.basename(os.path.abspath(os.curdir)), choices=['study1', 'study2'])
p.add_argument('--chains', type=int, default=4)
p.add_argument('--draws', type=int, default=1000)
p.add_argument('--tune', type=int, default=1000)
p.add_argument('--target-accept', type=float, default=None, help='default 0.99 for study1, 0.80 for study2 (as published)')
p.add_argument('--noncentered', action='store_true', help='non-centred random effects (recommended for convergence of variance components)')
p.add_argument('--exclude-subs', default='', help='comma-separated sub codes to exclude (robustness checks)')
p.add_argument('--optimally-delayed-only', action='store_true', help='restrict to trials with optimally delayed control (preregistered selection)')
p.add_argument('--seed', type=int, default=20261007)
p.add_argument('--out', default=None)
a = p.parse_args()
warnings.filterwarnings('ignore')
import pymc as pm, arviz as az
from scipy.stats import gaussian_kde

root = os.path.dirname(os.path.abspath(__file__))
study_dir = os.path.join(os.path.dirname(root), a.study)
df = pd.read_csv(os.path.join(study_dir, 'lmm_fixed.csv'))
if a.exclude_subs:
    excl = [s if s.endswith('.csv') else s + '.csv' for s in a.exclude_subs.split(',')]
    df = df[~df['sub'].isin(excl)]
if a.optimally_delayed_only:
    df = df[df['optimally_delayed'] == 1]
df = df.reset_index(drop=True)
target_accept = a.target_accept if a.target_accept is not None else (0.99 if a.study == 'study1' else 0.80)
print(f'{a.study}: n_participants={df["sub"].nunique()} n_decisions={len(df)} chains={a.chains} target_accept={target_accept} noncentered={a.noncentered}', flush=True)

sub_idx, subs = pd.factorize(df['sub'])
RT = df['RT'].values                                   # natural-log RT (preprocessing)
delayed_planning = df['delayed_planning'].values.astype(float)
trial_num_v = (df['trial_num_within_goal'].values - 21) / 20.0   # centred so that the final trial ~ 0
goalswitch = df['goal_switch'].values.astype(float)
offset = 0 if a.study == 'study1' else 2
decision = df['decision'].values.astype(float) - offset
planning_depth = df['planning_depth'].values.astype(float) - offset
control_effect = df['control_regressor'].values.astype(float)
interaction = delayed_planning * trial_num_v
n = len(subs)

with pm.Model():
    intercept = pm.Normal('intercept', 0, 2)
    coef_delayed_planning = pm.Normal('coef_delayed_planning', 0, 2)
    coef_trial_num = pm.Normal('coef_trial_num', 0, 2)
    coef_goalswitch = pm.Normal('coef_goalswitch', 0, 2)
    coef_decision = pm.Normal('coef_decision', 0, 2)
    coef_planning_depth = pm.Normal('coef_planning_depth', 0, 2)
    coef_c = pm.Normal('coef_c', 0, 2)
    coef_interaction = pm.Normal('coef_interaction', 0, 2)
    # participant-level random effects (variable names as in the published traces)
    sigma_sub = pm.HalfNormal('sigma_sub', 2)
    if a.noncentered:
        z0 = pm.Normal('z_intercept_sub', 0, 1, shape=n); intercept_sub = pm.Deterministic('intercept_sub', sigma_sub * z0)
    else:
        intercept_sub = pm.Normal('intercept_sub', mu=0, sigma=sigma_sub, shape=n)
    def slope(name):
        sigma = pm.HalfNormal(f'sigma_{name.replace("slope_sub_", "slope_")}', 2)
        if a.noncentered:
            z = pm.Normal(f'z_{name}', 0, 1, shape=n); return pm.Deterministic(name, sigma * z)
        return pm.Normal(name, mu=0, sigma=sigma, shape=n)
    slope_sub_dp = slope('slope_sub_dp'); slope_sub_c = slope('slope_sub_c'); slope_sub_gs = slope('slope_sub_gs')
    slope_sub_d = slope('slope_sub_d'); slope_sub_pd = slope('slope_sub_pd'); slope_sub_tn = slope('slope_sub_tn')
    slope_sub_interaction = slope('slope_sub_interaction')
    mu = (intercept + intercept_sub[sub_idx]
          + (coef_delayed_planning + slope_sub_dp[sub_idx]) * delayed_planning
          + (coef_trial_num + slope_sub_tn[sub_idx]) * trial_num_v
          + (coef_goalswitch + slope_sub_gs[sub_idx]) * goalswitch
          + (coef_decision + slope_sub_d[sub_idx]) * decision
          + (coef_c + slope_sub_c[sub_idx]) * control_effect
          + (coef_planning_depth + slope_sub_pd[sub_idx]) * planning_depth
          + (coef_interaction + slope_sub_interaction[sub_idx]) * interaction)
    pm.Normal('RT_obs', mu=mu, sigma=1, observed=RT)      # observation model as published (sigma fixed at 1)
    t0 = time.time()
    trace = pm.sample(draws=a.draws, tune=a.tune, chains=a.chains, cores=min(a.chains, os.cpu_count() or 1),
                      target_accept=target_accept, random_seed=a.seed, progressbar=False)
    print(f'sampling took {time.time() - t0:.0f} s', flush=True)

out = a.out or os.path.join(study_dir, 'RTdata_model_fitted_withintrial.nc' if a.study == 'study1' else 'RTdata_model_fitted_withintrial2.nc')
if a.out is None and os.path.exists(out):
    out = out.replace('.nc', '_refit.nc')      # never overwrite the published trace silently
trace.to_netcdf(out); print('saved trace to', out)

def mode_hdi(x):
    x = np.asarray(x).ravel(); kde = gaussian_kde(x); g = np.linspace(x.min(), x.max(), 1000)
    return g[np.argmax(kde(g))], az.hdi(x, hdi_prob=0.95)
fixed = ['coef_delayed_planning', 'coef_interaction', 'coef_trial_num', 'coef_goalswitch', 'coef_decision', 'coef_planning_depth', 'coef_c', 'intercept']
sig = [v for v in trace.posterior.data_vars if v.startswith('sigma')]
for v in ['coef_delayed_planning', 'coef_interaction']:
    m, h = mode_hdi(trace.posterior[v].values); print(f'{v}: posterior mode = {m:.3f}, 95% HDI = [{h[0]:.3f}, {h[1]:.3f}]')
s = az.summary(trace, var_names=fixed + sig, hdi_prob=0.95)
print(s[['mean', 'hdi_2.5%', 'hdi_97.5%', 'ess_bulk', 'r_hat']].to_string())
print('divergences:', int(trace.sample_stats['diverging'].sum()))
