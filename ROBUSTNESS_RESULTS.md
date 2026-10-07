# Robustness checks cited in Supplementary Table S5 (preregistration deviations)

All checks were run on 7 Oct 2026 from the files in this repository (environment: `environment.yml`).
Model: log RT ~ DelayedPlan + Trial + GoalSwitch + Decision + Control + PlanDepth + DelayedPlan × Trial,
with participant-level random effects (the published hierarchical Bayesian model; see `study*/fit_rt_lmm.py`).

## 1. Frequentist linear mixed models (the preregistered analysis form)

`statsmodels` MixedLM, REML, Wald z-tests; random intercept plus random slopes for DelayedPlan and DelayedPlan × Trial
(the random-intercept-only variant is given in parentheses where it differs materially).

| Data | Study | DelayedPlan (βRT) | DelayedPlan × Trial (learning) |
|---|---|---|---|
| All trials (as analysed in the paper) | 1 (n = 93) | b = 0.326, SE = 0.061, p = 7.4 × 10⁻⁸ | b = 0.224, SE = 0.069, p = 0.0012 |
| | 2 (n = 163) | b = 0.366, SE = 0.044, p = 6.9 × 10⁻¹⁷ | b = 0.240, SE = 0.056, p = 2.0 × 10⁻⁵ |
| Optimally-delayed trials only (preregistered selection) | 1 | b = 0.948, SE = 0.072, p = 4 × 10⁻³⁹ | b = 0.136, SE = 0.099, p = 0.17 (random intercept only: b = 0.075, SE = 0.064, p = 0.25) |
| | 2 | b = 0.987, SE = 0.056, p = 2 × 10⁻⁷⁰ | b = 0.249, SE = 0.063, p = 7.4 × 10⁻⁵ |
| All trials, excluding the 10 pilot participants collected before preregistration | 1 (n = 83) | b = 0.296, SE = 0.064, p = 4.0 × 10⁻⁶ | b = 0.218, SE = 0.076, p = 0.0041 |
| Optimally-delayed trials only, excluding pilot participants | 1 (n = 83) | b = 0.934, SE = 0.079, p = 2 × 10⁻³² | b = 0.108, SE = 0.109, p = 0.32 |

Conclusions: the delayed-planning RT effect (hypothesis 1b) is robust to every specification and is larger under the
preregistered trial selection. The learning effect (DelayedPlan × Trial, hypothesis 2) is robust in Study 2 under
both specifications, but in Study 1 it is significant only when all trials are analysed (as in the paper) and not
under the preregistered restriction to optimally-delayed trials.

## 2. Bayesian refits of the published model (`fit_rt_lmm.py`)

Two chains × 1,000 draws after 1,000 tuning iterations, target_accept = 0.99, otherwise identical to the published model.
Posterior mode and 95% HDI.

| Fit | DelayedPlan (βRT) | DelayedPlan × Trial |
|---|---|---|
| Study 1, excluding the 10 pilot participants | PENDING | PENDING |
| Study 1, optimally-delayed trials only | PENDING | PENDING |
| Study 2, optimally-delayed trials only | PENDING | PENDING |

## 3. Non-centred reparameterisation of the published model (`fit_rt_lmm.py --noncentered`, 4 chains)

Addresses the poor mixing of the near-zero random-slope standard deviations in the published (centred) fits
(R̂ 1.12–1.65 for σ_goalswitch and σ_interaction, and σ_control in Study 2; population-level coefficients R̂ ≤ 1.01).

| Study | DelayedPlan (βRT) | DelayedPlan × Trial | max R̂ (all parameters) | divergences |
|---|---|---|---|---|
| 1 | PENDING | PENDING | PENDING | PENDING |
| 2 | PENDING | PENDING | PENDING | PENDING |
