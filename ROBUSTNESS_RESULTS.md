# Robustness checks (Study 1 = the 81 participants recruited after preregistration)

All checks were run on 7 Oct 2026 from the files in this repository (environment: `environment.yml`), after the ten
pilot sessions collected before the Study 1 preregistration were excluded (see `study1/data/pilot_preregistration/`) and the
Study 1 raw data were replaced by the complete Pavlovia re-download (which removed two duplicate copies of single sessions).
Model: log RT ~ DelayedPlan + Trial + GoalSwitch + Decision + Control + PlanDepth + DelayedPlan × Trial with
participant-level random effects (the published hierarchical Bayesian model; `study*/fit_rt_lmm.py`).

## 1. Published model (centred parameterisation; 4 chains × 1,000 draws after 1,000 tuning iterations)

| Study | DelayedPlan (βRT), mode [95% HDI] | DelayedPlan × Trial | max R̂ population-level | R̂ of near-zero random-slope SDs |
|---|---|---|---|---|
| 1 (N = 81; target_accept 0.99) | 0.30 [0.18, 0.42] | 0.21 [0.10, 0.35] | 1.00 | goal switch 1.53, interaction 1.26, control 1.03 |
| 2 (N = 163; target_accept 0.80) | 0.37 [0.29, 0.44] | 0.24 [0.16, 0.33] | 1.01 | goal switch 1.33, interaction 1.65, control 1.25 |

Pearson correlations of the participant-level posterior means with mean adaptively delayed control (Results):
Study 1 βRT r = 0.83, interaction r = −0.32 (p = 0.004); Study 2 r = 0.83 and −0.39 (`study*/lmm_posterior_correlations.py`).

## 2. Frequentist linear mixed models (the preregistered analysis form)

`statsmodels` MixedLM, REML, Wald z-tests; random intercept plus random slopes for DelayedPlan and DelayedPlan × Trial.

| Data | Study | DelayedPlan (βRT) | DelayedPlan × Trial (learning) |
|---|---|---|---|
| All trials (as analysed in the paper) | 1 (n = 81) | b = 0.303, SE = 0.065, p = 2.8 × 10⁻⁶ | b = 0.220, SE = 0.076, p = 0.004 |
| | 2 (n = 163) | b = 0.366, SE = 0.044, p = 6.9 × 10⁻¹⁷ | b = 0.240, SE = 0.056, p = 2.0 × 10⁻⁵ |
| Optimally-delayed trials only (preregistered selection) | 1 | b = 0.946, SE = 0.078, p = 2 × 10⁻³³ | b = 0.126, SE = 0.108, p = 0.25 (random intercept only: b = 0.043, p = 0.54) |
| | 2 | b = 0.987, SE = 0.056, p = 2 × 10⁻⁷⁰ | b = 0.249, SE = 0.063, p = 7.4 × 10⁻⁵ |

Conclusions: the delayed-planning RT effect (hypothesis 1b) is robust to every specification and is larger under the
preregistered trial selection. The learning effect (DelayedPlan × Trial, hypothesis 2) is robust in Study 2 under both
specifications, but in Study 1 it is significant only when all trials are analysed (as in the paper) and not under the
preregistered restriction to optimally-delayed trials.

## 3. Bayesian refits of the published model with the preregistered trial selection (`robustness_lmm.py` logic; 2 chains)

| Fit | DelayedPlan (βRT) | DelayedPlan × Trial |
|---|---|---|
| Study 1, optimally-delayed trials only (80 participants with such trials, 5,979 decisions) | mode 0.90, HDI [0.76, 1.06] | mode 0.07, HDI [−0.10, 0.28] (HDI includes 0) |
| Study 2, optimally-delayed trials only (162 participants, 12,870 decisions) | mode 0.92, HDI [0.82, 1.03] | mode 0.27, HDI [0.13, 0.41] |

## 4. Non-centred reparameterisation of the published model (`fit_rt_lmm.py --noncentered --target-accept 0.99`, 4 chains)

Addresses the poor mixing of the near-zero random-slope standard deviations in the centred fits.

| Study | DelayedPlan (βRT) | DelayedPlan × Trial | max R̂ (all parameters) | divergences |
|---|---|---|---|---|
| 1 (N = 81) | mode 0.29, HDI [0.18, 0.42] | mode 0.22, HDI [0.09, 0.34] | 1.03 (ESS ≥ 234; participant-level effects all ≤ 1.03) | 0 |
| 2 (N = 163) | mode 0.36, HDI [0.29, 0.44] | mode 0.25, HDI [0.16, 0.32] | 1.02 (participant-level effects all ≤ 1.02; ESS ≥ 290) | 0 (62 with the published target_accept 0.80) |

With the non-centred Study 1 trace the Results correlations are r = 0.83 (βRT) and r = −0.32 (interaction), identical to the centred-trace values. Non-centred traces are not tracked by git (`*_noncentered_refit.nc`); regenerate them with the command above.

## 5. Earlier samples (for the record)

With the ten pilot participants and the two duplicate files included (N = 93; the analyses of manuscript v18): βRT mode 0.32 [0.21, 0.43], interaction
0.21 [0.11, 0.33], Pearson r = 0.84 and −0.35; frequentist all-trials b = 0.33 (p = 7 × 10⁻⁸) and 0.22 (p = 0.001);
preregistered selection b = 0.95 (p < 10⁻³⁸) and 0.14 (p = 0.17). The full before/after comparison, including figures,
is in the manuscript folder (`Study1_pilot_exclusion_comparison.pdf`).
The intermediate 83-participant rerun (pilot excluded, duplicates still present) gave βRT 0.29 [0.18, 0.41] and interaction 0.22 [0.10, 0.34].
