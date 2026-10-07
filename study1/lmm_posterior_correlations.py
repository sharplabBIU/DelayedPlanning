"""Cross-participant correlations between participant-level RT-model effects and behaviour.

Reproduces the two correlations reported in the Results (Study 1):
  * "correlation between beta_RT random effect and control choice accuracy: r = 0.84, p < 0.001"
      -> Pearson r between each participant's posterior-mean DelayedPlan slope (slope_sub_dp) and the
         participant's mean proportion of optimally delayed control (optimally_delayed in lmm_fixed.csv)
  * "negative correlation ... between the interaction parameter and adaptively delayed control (r = -0.35, p < 0.001)"
      -> Pearson r between the posterior-mean DelayedPlan x Trial slope (slope_sub_interaction) and the same measure.
Spearman correlations are printed alongside for reference.

Usage (from the repository root or a study folder):  python lmm_posterior_correlations.py [study1|study2]
Requires the stored trace <study>/RTdata_model_fitted_withintrial[2].nc, whose participant index follows the
row order of the shipped <study>/lmm_fixed.csv (pd.factorize order).
"""
import os, sys, warnings
import numpy as np, pandas as pd, arviz as az
from scipy.stats import pearsonr, spearmanr
warnings.filterwarnings('ignore')
study = sys.argv[1] if len(sys.argv) > 1 else os.path.basename(os.path.abspath(os.curdir))
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sd = os.path.join(root, study)
trace = az.from_netcdf(os.path.join(sd, 'RTdata_model_fitted_withintrial.nc' if study == 'study1' else 'RTdata_model_fitted_withintrial2.nc'))
df = pd.read_csv(os.path.join(sd, 'lmm_fixed.csv'))
sub_idx, subs = pd.factorize(df['sub'])
pmean = trace.posterior.mean(dim=['chain', 'draw'])
beh = df.groupby('sub')['optimally_delayed'].mean().reindex(subs).values
for label, var in [('beta_RT (DelayedPlan) participant effect', 'slope_sub_dp'), ('beta_RT x Time (interaction) participant effect', 'slope_sub_interaction')]:
    x = pmean[var].values
    r, p = pearsonr(x, beh); rs, ps = spearmanr(x, beh)
    print(f'{study}: {label} vs. mean optimally delayed control: Pearson r = {r:.3f} (p = {p:.2e}); Spearman rho = {rs:.3f} (p = {ps:.2e}); n = {len(x)}')
