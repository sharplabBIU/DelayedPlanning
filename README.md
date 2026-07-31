# Humans adaptively delay planning using cognitive maps

Companion repository for **“Humans adaptively delay planning using cognitive maps”** (Sharp & Eldar). It contains the raw data, task code, preprocessing pipelines, and every analysis reported in the manuscript and Supplemental Material.

---

## ✨ Study Summary

Planning is computationally costly. In multi-step problems it is often more efficient to ***delay*** planning until doing so is actually useful. We created a decision task in which — at specific decision points — every available action is equally likely to reach the instructed goal, making it *optimal to relinquish control* and postpone planning. Across two preregistered experiments we show that participants learn to identify these points and **delay planning adaptively**, improving with experience. A model-based meta-control (MBMC) model reveals that this behavior is driven by **search over a cognitive map of the task**, rather than by reinforcement from experienced outcomes.

---

## 🗂️ Repository Structure

```
.
├── study1/                    ← Experiment 1 (n = 93): data + behavioral analyses
│   ├── data/                  ← Raw PsychoPy .csv files + preprocess_raw_data.py
│   └── analysis.ipynb         ← Main behavioral notebook (Fig. 2, Supp. Fig. S1)
├── study2/                    ← Experiment 2 (n = 163): data, task code, behavioral + modeling analyses
│   ├── data/                  ← Raw .csv files + preprocessing
│   ├── task/                  ← Task implementation (materials: stimuli, task assets)
│   ├── demographics/          ← Demographics data + script
│   └── analysis.ipynb         ← Behavioral notebook (Fig. 3B empirical panels)
└── model_fitting_revision/    ← SR/PR competitor models, model recovery, relinquish variant
    └── results/               ← Fitted parameters and model-comparison outputs
```

---

## 🗺️ Map: manuscript / supplement → analysis

### Behavior (Studies 1 & 2)

| Result | Code | Key outputs |
|---|---|---|
| Fig. 2 behavioral panels, memory-quiz accuracy, Supp. Fig. S1 cost–benefit simulation | `study1/analysis.ipynb` | `study1/*.png`, `study1/simulation_with_metaplanning.png`, `study1/Figures_Final.pdf` |
| Permutation test of adaptive control (Fig. 2B right) | `study1/permutation_test_and_visualize.py`, `study1/visualize_perm_test.py`, `study2/permutation_test_control_decision.py` | `study1/permutations_optimal_score*.csv`, `permTest_Visualized.png` |
| Adaptively delayed control score (top-decile definition, Fig. 2C) | `study{1,2}/optimal_delayed_score.py` | `optimal_delayed_scores.csv` |
| Hierarchical Bayesian RT LMM (Fig. 2D/2E; PyMC + NUTS) | `study1/lmm_create_design_matrix.py`; fit in `study{1,2}/analysis.ipynb` | `study1/RTdata_model_fitted_withintrial.nc`, `study2/RTdata_model_fitted_withintrial2.nc`, `lmm_fixed.csv` |
| Top decile vs bottom 90% half-split (Results: overall levels, relative and absolute change) | `study2/pct_halfsplit_decile.py`, `study2/abs_halfsplit_decile.py` | printed stats reported in Results |
| Demographics (Methods) | `study{1,2}/demographics_analyze.py` | `study1/study1_demographics.csv`, `study2/demographics/` |

### Computational modeling (winning soft-gated MBMC model)

| Result | Code | Key outputs |
|---|---|---|
| Winning model definition (soft-gated breadth) | `study2/gated_soft.py` (+ `recovery_common.py`, `recovery_em.py`, `recovery_faithful.py` EM machinery) | — |
| EM / iterative importance-sampling fits | `study2/gatedsoft_run_all.py` (Study 2), `study2/fit_study1_softgate.py` (Study 1) | `study2/em_params_study{1,2}_MBMCgatedsoft.npy` |
| 13-model comparison (Fig. 3A right) | `study2/softgate_model_comparison.py` (generates `mfit_softgate_gen.py` from `model_fitting_revision/mfit_likelihoods.py`) | `softgate_model_comparison_BICs.csv`, `softgate_model_comparison_figure.png` |
| MF learner + with-replacement variants (in-text ΔBICs) | `study2/softgate_extra_variants.py` | `softgate_extra_variants_BICs.csv` |
| V-relinquish variant (in-text ΔBIC = +2) | `model_fitting_revision/fit_relinquish_variant.py` | `results/relinquish_variant_ibic_study2.csv` |
| Parameter recovery at best-fit params (Fig. 3A left, mean r = 0.68) | `study2/faithful_recovery_softgate.py` | `faithful_recovery_softgate_corr.csv`, `_heatmap.png` |
| Model recapitulates behavior (Fig. 3B bottom row) | `study2/gatedsoft_run_all.py` (simulation block) | `simulated_data_gatedsoft.csv`, `MODELsimulated_GATEDSOFT_*.png`, `stayPlot_SIM_GATEDSOFT.png` |
| Parameter–RT correlations (Fig. 3C) | `study2/fig3c_softgate.py` (+ `analysis.ipynb`) | `study2/*_softgate.png` panels |
| Fitted parameters: Supp. Tables S3–S4, Supp. Fig. S7 | `study2/summarize_softgate_params.py` (medians/IQRs from the soft-gated fits) | `em_params_study{1,2}_median_iqr.csv`, `cbm_MBMCgatedsoft_params_EM_barplots.png` |

### Supplemental analyses

| Supp. item | Code | Key outputs |
|---|---|---|
| Fig. S1 cost–benefit agent simulation | `study1/analysis.ipynb` (simulation cells) | `study1/simulation_with_metaplanning.png` |
| Fig. S2 model-derived decision time (rollouts) | `study2/mbmc_rollout_rt_softgate.py` (+ `mbmc_rollout_rt_median.py` module) | `mbmc_simulated_RT_softgate_mean_study2.png/.csv` |
| Rollout RT proxy vs. empirical RT | `study{1,2}/rollout_rt_proxy.py` | `rollout_rt_proxy_*.csv` |
| Fig. S3 SR/PR meta-controllers | `model_fitting_revision/` (`cbm_models.py`, `mfit_models.py`, `run_map.py`; see its README) | `cbm_deltaBIC_vs_MBMC.png`, `cbm_response_summary.csv`, `results/` |
| Fig. S4 model recovery (13 soft-gated models) | `model_fitting_revision/model_recovery_softgate_reps.py` | `model_recovery_softgate_reps_study2.png`, `results/model_recovery_softgate_reps_confusion.csv` |
| Fig. S5 parameter recovery, wide priors (Table S2 = `GROUND_TRUTH` in `recovery_parameter.py`) | `study2/recovery_softgate_big.py` | `recovery_softgate_big_corr.csv`, `_heatmap.png` |
| Fig. S6 simulated delayed-planning RT signature (LMM on model-generated RTs) | `study2/rt_lmm_simulated_softgate.py` | `rt_lmm_simulated_softgate_posterior.png`, `_trace.nc` |

---

## ✅ Computational reproducibility

Every analysis in the paper was checked in one of two ways: **(re-run)** — executed end-to-end from the files in this repository and compared against the reported value; **(stored)** — the committed output file was checked against the reported value, because a full re-run takes hours (script and all inputs are present; expected runtime noted).

| Paper claim | Reported | Reproduced | How |
|---|---|---|---|
| Demographics S1 (51% male, age 39.98) | 51%, 39.98 | 51.00%, 39.98 | re-run |
| Demographics S2 (50.9% male, age 37.90) | 50.9%, 37.90 | 50.92%, 37.90 | re-run |
| Exclusion-criterion correlation | r = 0.14, p = 0.17 | r = 0.145, p = 0.166 | re-run |
| Permutation test (each depth) | p < 0.001 | p < 10⁻⁴ all depths | re-run from stored permutations |
| Study 1 RT LMM delayed-planning effect | mode 0.32, HDI [0.21, 0.43] | 0.322 [0.208, 0.432] | re-run from stored trace |
| Study 1 delayed-planning × trial interaction | mode 0.21, HDI [0.11, 0.33] | 0.214 [0.108, 0.335] | re-run from stored trace |
| βRT random effect vs control-choice accuracy | r = 0.84 | r = 0.843 (`optimally_delayed`) | re-run from stored trace |
| Interaction vs adaptively delayed control | r = −0.35 | Study 1 full-sample r = −0.329 (reported value pools studies) | re-run from stored trace |
| Half-split overall levels / relative / absolute change (both studies) | all Results values | exact match | re-run (`pct/abs_halfsplit_decile.py`) |
| Model-comparison BIC ladder (all 8 in-text ΔBICs + baseline BIC) | 26984.25; 2276.45 … 689.25; MF 437.92 | all exact | stored (`softgate_model_comparison_BICs.csv`; full refit ≈ hours) |
| Fig. 3C correlations | ρ = 0.63, −0.39, −0.23, −0.04 | 0.630, −0.386, −0.228, −0.044 | re-run (`fig3c_softgate.py`) |
| Fig. 3A-left faithful recovery | mean r = 0.68 | 0.677 | stored (refit ≈ hours) |
| Supp. Tables S3/S4 medians + IQRs | all 36 values | exact from `em_params_*_MBMCgatedsoft.npy` | re-run (`summarize_softgate_params.py`) |
| Supp. Fig. S2 caption parameter means | 1.24, 0.67, 0.48, 0.20, 0.26 | 1.241, 0.671, 0.485, 0.199, 0.259 | re-run from stored fits |
| Supp. Fig. S4 model recovery | full model 0.95; 12/13 ≥ 0.90; 9 perfect; MBMC_BD 0 | exact | stored (re-run ≈ 6 h) |
| Supp. Fig. S6 simulated interaction | mean 0.46, HDI [0.38, 0.53] | 0.456 [0.383, 0.527] | re-run from stored trace |
| SR/PR ΔBIC (response letter) | 589.7 / 1044.3 (SR), 1348.7 / 2103.0 (PR) | exact | stored (`cbm_response_summary.csv`) |
| V-relinquish variant | ΔBIC = +2 | +1.7 | stored (`results/relinquish_variant_ibic_study2.csv`) |

Not independently re-derived here (script + data present): the EM model fits themselves (`gatedsoft_run_all.py`, `fit_study1_softgate.py`; ≈ hours each), the empirical RT LMM fits (notebook cells; ≈ hours), Supp. Fig. S5 wide-prior recovery (`recovery_softgate_big.py`; ≈ 15 min), the S6 LMM refit, and notebook-computed values (route-quiz accuracy 98.7%, Fig. 2 panel renderings).

---

## 📁 File inventory

### Root
| File | Description |
|---|---|
| `README.md`, `LICENSE`, `.gitignore` | This file; CC-BY-4.0 license; ignore rules |

### `study1/` (Experiment 1, n = 93)
| File | Description |
|---|---|
| `data/` | Raw PsychoPy session .csv per participant + `preprocess_raw_data.py` (raw → tidy) |
| `analysis.ipynb` | Main notebook: preprocessing → Fig. 2 panels, quiz accuracy, RT LMM fit, Supp. Fig. S1 simulation |
| `preprocessed_data.csv`, `lmm_fixed.csv` | Tidy trial-level data; LMM design matrix (from `lmm_create_design_matrix.py`) |
| `RTdata_model_fitted_withintrial.nc` | Posterior trace of the hierarchical RT LMM (Fig. 2D/2E stats) |
| `permutation_test_and_visualize.py`, `visualize_perm_test.py`, `permutationTest_notebook.ipynb` | Permutation test of adaptive control (Fig. 2B right) |
| `permutations_optimal_score.csv`, `permutations_optimal_score_ACTUALSUBS.csv` | Permuted and actual optimal-control scores |
| `optimal_delayed_score.py`, `optimal_delayed_scores.csv` | Per-subject adaptively-delayed-control score (top-decile definition) |
| `demographics_analyze.py`, `study1_demographics.csv` | Methods demographics |
| `memory_accuracies_subjects_orig_fulltrajectories.csv` | Route-quiz accuracy placeholder (regenerated by the notebook) |
| `rollout_rt_proxy.py`, `rollout_rt_proxy_*.csv` | Model-derived decision-time proxy vs empirical RT (Study 1) |
| `lmm_create_design_matrix.py` | Builds `lmm_fixed.csv` from preprocessed data |
| `CB_exec.npy`, `MB_*.npy`, `breadth2_exec.npy`, `cache_*.npy`, `forget_exec.npy`, `mbcache_exec.npy` | Simulation inputs loaded by `analysis.ipynb` |
| `Figures_Final.pdf` | Assembled final figures |
| `simulation_with_metaplanning.png` | Supp. Fig. S1 (cost–benefit agent simulation) |
| `permTest_Visualized.png`, `optimal_planning_RTs*.png`, `posterior_*.png`, `controlTaking_by_time*.png`, `optimalDelayed_by_time.png`, `optimal_RT_overtime.png`, `RTs_by_time.png`, `optimal_control*.png`, `optimal_action_choice.png`, `optimal_metacontrol_choice.png`, `correct_control_action.png`, `total_score_plot.png`, `variability_*.png`, `simulated_optimal_Control_by_planningdepth.png`, `optimal_controlactualparticipantsempiricaldata*.png` | Fig. 2 panel images (regenerated by `analysis.ipynb`) |

### `study2/` (Experiment 2, n = 163)
| File | Description |
|---|---|
| `data/` | Raw session .csv per participant + preprocessing |
| `task/` | Task implementation and stimulus assets (materials) |
| `demographics/` | `study2_demographics.csv` + `demographics_analyze.py` |
| `analysis.ipynb` | Behavioral notebook: Fig. 3B empirical panels, RT LMM fit, quiz checks |
| `preprocessed_data.csv`, `lmm_fixed.csv` | Tidy trial-level data; LMM design matrix |
| `RTdata_model_fitted_withintrial2.nc` | Posterior trace of the Study 2 RT LMM |
| `permutation_test_control_decision.py`, `visualize_perm_test.py` | Study 2 permutation test |
| `optimal_delayed_score.py`, `optimal_delayed_scores.csv` | Per-subject adaptive-control score |
| `pct_halfsplit_decile.py`, `abs_halfsplit_decile.py` | Top decile vs bottom 90% half-split stats (relative %, absolute change, overall levels; both studies) |
| `gated_soft.py` | **Winning soft-gated MBMC model** (likelihood + simulator) |
| `recovery_common.py`, `recovery_em.py`, `recovery_faithful.py`, `recovery_likelihoods.py` | EM / iterative importance-sampling machinery and the 13-model likelihood library |
| `mfit_softgate_gen.py` | Auto-generated soft-gated likelihoods (regenerated by `softgate_model_comparison.py`) |
| `gatedsoft_run_all.py` | Study 2 EM fit + recovery + Fig. 3B simulation for the winning model |
| `fit_study1_softgate.py` | Study 1 EM fit of the winning model |
| `fit_real_em.py` | Original-model EM fit (reference; superseded by the soft-gated fits) |
| `em_params_study{1,2}_MBMCgatedsoft.npy` | **Fitted parameters (winning model), native space** — source of Tables S3/S4, Fig. S7, Fig. S2 caption |
| `em_params_study{1,2}_MBMC.npy` | Original-model fits (reference) |
| `summarize_softgate_params.py`, `em_params_study{1,2}_median_iqr.csv` | Medians/IQRs for Supp. Tables S3–S4 |
| `softgate_model_comparison.py`, `softgate_model_comparison_BICs.csv`, `softgate_model_comparison_figure.png` | 13-model iBIC comparison (Fig. 3A right + in-text ΔBICs) |
| `softgate_extra_variants.py`, `softgate_extra_variants_BICs.csv` | MF learner and with-replacement variants (in-text ΔBICs) |
| `faithful_recovery_softgate.py`, `faithful_recovery_softgate_corr.csv`, `_heatmap.png` | Fig. 3A-left parameter recovery (mean r = 0.68) |
| `fig3c_softgate.py`, `*_softgate.png` | Fig. 3C parameter–RT correlation panels |
| `simulated_data_gatedsoft.csv`, `MODELsimulated_GATEDSOFT_*.png`, `controlTaking_by_time_depth*_SIM_GATEDSOFT.png`, `stayPlot_SIM_GATEDSOFT.png`, `stayPlot_ALLPerformingSubjects_SIM.png` | Fig. 3B simulated-behavior panels |
| `mbmc_rollout_rt_softgate.py`, `mbmc_rollout_rt_median.py`, `mbmc_simulated_RT_softgate_mean_study2.{png,csv}` | Supp. Fig. S2 model-derived decision time |
| `rollout_rt_proxy.py`, `rollout_rt_proxy_*.csv`, `rollout_proxy_over_trials.png`, `true_vs_simulated_effects.png` | Decision-time proxy vs empirical RT (Study 2) |
| `recovery_parameter.py` | Wide generating priors (**Supp. Table S2** = `GROUND_TRUTH`) + recovery driver |
| `recovery_softgate_big.py`, `recovery_softgate_big_corr.csv`, `_heatmap.png` | Supp. Fig. S5 wide-prior parameter recovery (N = 1000) |
| `recovery_gatedsoft_corr_mean.csv`, `recovery_gatedsoft_heatmap.png` | Empirical-prior recovery of the winning model |
| `rt_lmm_simulated_softgate.py`, `rt_lmm_simulated_softgate_{data.csv,posterior.png,trace.nc}` | Supp. Fig. S6 simulated RT-signature LMM |
| `cbm_MBMCgatedsoft_params_EM_barplots.png` | Supp. Fig. S7 fitted-parameter barplots |
| `optimal_control.png`, `optimal_RT_by_planningdepth.png`, `variability_metacontrol.png` | Fig. 3B empirical panels (from `analysis.ipynb`) |

### `model_fitting_revision/` (SR/PR competitors, recovery, variants)
| File | Description |
|---|---|
| `README.md` | Pipeline documentation for this folder |
| `cbm_models.py`, `mfit_models.py`, `mfit_likelihoods.py`, `fastdata.py` | SR / PR / CB / MBMC model definitions and likelihoods (Supp. Fig. S3) |
| `run_map.py` | Per-subject MAP fits + summed BIC (the reported SR/PR comparison) |
| `run_cbm.py`, `fast_lap.py`, `make_notebook.py`, `cbm_model_fitting_r1.ipynb` | Full CBM (Laplace/HBI) pipeline + rendered notebook |
| `fit_relinquish_variant.py`, `mfit_likelihoods_relhalf.py` | V-relinquish variant refit (in-text ΔBIC = +2) |
| `model_recovery_softgate_reps.py`, `recovery_mbmc_sim.py`, `model_recovery_softgate_reps_study2.png` | Supp. Fig. S4 model recovery (13 soft-gated models) |
| `cbm_deltaBIC_vs_MBMC.png` | Supp. Fig. S3 figure |
| `cbm_response_summary.csv` | SR/PR ΔBIC summary (both studies) |
| `results/fits_study{1,2}.csv`, `results/group_study{1,2}.csv` | Per-subject and group-level SR/PR fit summaries |
| `results/map_params_study{1,2}_{CB,MBMC,PR,SR}.npy` | MAP parameter estimates |
| `results/mbmc_params_study{1,2}_median_iqr.csv` | MBMC (CBM route) parameter summaries |
| `results/model_recovery_softgate_reps_confusion.csv` | Supp. Fig. S4 confusion matrix |
| `results/relinquish_variant_ibic_study2.csv` | Relinquish-variant iBICs |

---

## 🚀 Getting Started

```bash
git clone https://github.com/sharplabBIU/DelayedPlanning.git
cd DelayedPlanning
```

Suggested order: preprocess raw data (`study*/data/preprocess_raw_data.py`) → behavioral notebooks (`analysis.ipynb`) → model fitting (`study2/gatedsoft_run_all.py`, `study2/fit_study1_softgate.py`) → comparisons and recovery analyses (scripts in the map above). Fitted parameters and model-comparison outputs are included, so downstream scripts can run without refitting.

## 🐍 Python Dependencies

Python ≥ 3.10. A minimal environment:

```yaml
name: delayed-planning
channels:
  - conda-forge
dependencies:
  - python=3.13
  - numpy=2.1.3
  - pandas=2.2.3
  - scipy=1.15.1
  - matplotlib=3.10.0
  - seaborn=0.13.2
  - pymc=5.22.0
  - arviz=0.21.0
  - statsmodels=0.14.4
  - xarray=2024.11.0
  - xarray-einstats=0.6.0
  - jupyterlab
  - ipykernel
```

## 📝 Data Description

- **File format:** `.csv`, one file per participant/session in `study*/data/`, anonymized as `sub-XXX.csv` (no recruitment-platform identifiers are included anywhere in the repository)
- **Contents:** trial-level records of choices, reaction times, task state variables, and feedback
- The preprocessing scripts standardize variable names, remove practice trials, and output tidy data frames (`preprocessed_data.csv`, `lmm_fixed.csv`) ready for analysis.
- **Full column-level documentation:** see [`data_dictionary.md`](./data_dictionary.md).
- **Materials:** the task implementation and stimulus assets are in [`study2/task/`](./study2/task/) (both studies used this task; Study 2 additionally showed quiz feedback during training).

## 📑 Preregistrations

- Study 1: https://osf.io/qs9ja
- Study 2: https://osf.io/5y9z6
- Incentive pilot study (Discussion): https://osf.io/kca68/files/osfstorage

## 📄 Citation

```text
TBD
```

## 🛡️ License

This project is licensed under the CC-BY-4.0 License – see `LICENSE` for details.
