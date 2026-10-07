# Humans adaptively delay planning using cognitive maps

Companion archive for **Sharp, P. B., & Eldar, E. — "Humans adaptively delay planning using cognitive maps"** (*Psychological Science*, in press; manuscript PSCI-26-0102). It contains the anonymised raw data of both preregistered studies, the task implementation and stimuli (materials), the preprocessing pipeline, every analysis script and notebook behind the manuscript and its Supplemental Material, and the fitted parameters and posterior traces, so that every reported value can be re-derived.

| | |
|---|---|
| **Archived version of record (trusted repository)** | Zenodo: `https://doi.org/10.5281/zenodo.XXXXXXX` — *DOI to be inserted after the GitHub release is archived; see [Archiving, citation and license](#archiving-citation-and-license)* |
| **Development version** | https://github.com/sharplabBIU/DelayedPlanning |
| **Preregistrations (OSF registries)** | Study 1: https://doi.org/10.17605/OSF.IO/QS9JA (registered 26 May 2023) · Study 2: https://doi.org/10.17605/OSF.IO/5Y9Z6 (registered 18 June 2024) |
| **Incentive pilot study (Discussion)** | https://osf.io/kca68/files/osfstorage |
| **License** | CC BY 4.0 (data, materials and code) — see `LICENSE` |
| **Contact** | Paul B. Sharp, paul.sharp@biu.ac.il |

---

## Study summary

Planning is computationally costly. In multi-step problems it is often more efficient to ***delay*** planning until doing so is actually useful. We created a decision task in which — at specific decision points — every available action is equally likely to reach the instructed goal, making it *optimal to relinquish control* and postpone planning. Across two preregistered experiments we show that participants learn to identify these points and **delay planning adaptively**, improving with experience. A model-based meta-control (MBMC) model reveals that this behaviour is driven by **search over a cognitive map of the task**, rather than by reinforcement from experienced outcomes.

---

## Repository structure

```
.
├── README.md, data_dictionary.md    ← this file; column-level documentation of every data file
├── environment.yml                  ← conda environment used for the reproducibility check (Python 3.13, PyMC 5.22)
├── CITATION.cff, .zenodo.json       ← citation metadata for the Zenodo archive
├── study1/                          ← Experiment 1 (N = 101 recruited, 93 retained)
│   ├── data/                        ← anonymised raw PsychoPy session files (sub-XXX.csv) + preprocess_raw_data.py, correct_quizzes.py
│   │   └── bad_memory/              ← sessions excluded for failing the memory quizzes
│   ├── analysis.ipynb               ← behavioural notebook (Fig. 2 panels, quiz accuracy, RT model posterior summaries, Supp. Fig. S1)
│   ├── make_lmm_fixed.py, fit_rt_lmm.py, lmm_posterior_correlations.py   ← design matrix → RT mixed model → reported correlations
│   └── *.py, *.csv, *.nc, *.npy, *.png   ← scripts, derived data, posterior trace, simulation inputs, figure panels (inventory below)
├── study2/                          ← Experiment 2 (N = 251 recruited, 163 retained): data, task code, behavioural + modelling analyses
│   ├── data/, demographics/, task/  ← raw data; demographics; task implementation and stimuli (materials; see study2/task/README.md)
│   ├── analysis.ipynb               ← behavioural notebook (Fig. 3B empirical panels, Study 2 RT model summaries)
│   └── gated_soft.py, gatedsoft_run_all.py, softgate_model_comparison.py, …   ← winning soft-gated MBMC model, fits, comparisons, recovery
└── model_fitting_revision/          ← SR/PR competitor models, 13-model recovery, V-relinquish variant (own README)
    └── results/
```

---

## Quick start: environment and reproduction steps

### 1. Environment

```bash
git clone https://github.com/sharplabBIU/DelayedPlanning.git   # or download and unzip the Zenodo archive
cd DelayedPlanning
conda env create -f environment.yml
conda activate delayed-planning
python -m ipykernel install --user --name delayed-planning      # kernel for the notebooks
```

`environment.yml` pins the versions used for the independent reproducibility check (7 Oct 2026): Python 3.13, numpy 2.1.3, pandas 2.2.3, scipy 1.15.1, matplotlib 3.10.0, seaborn 0.13.2, PyMC 5.22.0, ArviZ 0.21.0, statsmodels 0.14.4, xarray 2024.11.0, networkx, openpyxl, JupyterLab/nbconvert. The published RT-model traces were produced with PyMC 5.16.1 (Study 1) and 5.22.0 (Study 2). The SR/PR competitor fits in `model_fitting_revision/` additionally require the `cbm_python` toolbox (see that folder's README).

**macOS note (Apple Silicon, Xcode 26 or newer).** PyTensor 2.30 (the version pinned by PyMC 5.22) passes a linker flag (`-ld64`) that recent Apple toolchains reject, so any script that samples with PyMC fails with `ld: library 'd64' not found`. Either upgrade PyTensor (`conda install -c conda-forge "pytensor>=2.31"`), or point PyTensor at a wrapper that drops the flag:

```bash
cat > ~/clangxx_nold64 <<'SH'
#!/bin/sh
args=""; for a in "$@"; do [ "$a" = "-ld64" ] || args="$args \"$a\""; done; eval exec /usr/bin/clang++ $args
SH
chmod +x ~/clangxx_nold64
export PYTENSOR_FLAGS="cxx=$HOME/clangxx_nold64"
```

Scripts that only use numpy/pandas/scipy/statsmodels are unaffected. Run plotting scripts with `MPLBACKEND=Agg` on a headless machine (several scripts call `plt.show()`).

### 2. Reproduction order and runtimes

All commands are run from the folder named in the first column. Every step can also be skipped because its outputs are committed; later steps read the committed outputs.

| Step | Folder | Command | Output → used by | Runtime |
|---|---|---|---|---|
| 1 Preprocess raw data | `study1/data`, `study2/data` | `python preprocess_raw_data.py` | `../preprocessed_data.csv` (tidy decision-level data) | seconds |
| 2 Memory-quiz scoring | `study1/data`, `study2/data` | `python correct_quizzes.py` (exclusion; already applied) ; `python route_quiz_accuracy.py` (accuracy of every participant) | `memory_accuracies_subjects_orig_fulltrajectories.csv` (failing sessions only, moved to `bad_memory/`); `route_quiz_accuracy_all.csv` | seconds |
| 3 Design matrix | `study1`, `study2` | `python make_lmm_fixed.py` (`--overwrite` to replace `lmm_fixed.csv`) | `lmm_fixed.csv` (regressors for the RT model, model fits and behavioural analyses) | 10 s |
| 4 Demographics | `study1`, `study2/demographics` | `python demographics_analyze.py` | Methods: 51% male, 39.98 y (S1); 50.9% male, 37.90 y (S2) | seconds |
| 5 Adaptive-control score | `study1`, `study2` | `python optimal_delayed_score.py` | `optimal_delayed_scores.csv` (Fig. 2C top-decile definition) | seconds |
| 6 Permutation test | `study1` | `python permutation_test_and_visualize.py`, `python visualize_perm_test.py` | Fig. 2B right (`permTest_Visualized.png`); reads the stored permutations `permutations_optimal_score*.csv` (re-create with `study2/permutation_test_control_decision.py`) | seconds (≈ 1 h to re-permute) |
| 7 RT mixed model | `study1`, `study2` | `python fit_rt_lmm.py` (writes `*_refit.nc`; `--noncentered` option) or notebook cell "RT model" | `RTdata_model_fitted_withintrial*.nc` → Fig. 2D/2E, Results (βRT mode 0.32 [0.21, 0.43]; interaction 0.21 [0.11, 0.33]) | 10–35 min per study |
| 8 Posterior summaries & correlations | `study1`, `study2` | `python lmm_posterior_correlations.py` ; notebook cells 21–22 (S1) / 17 (S2) | Results: r = 0.84 and r = −0.35 (Pearson, Study 1); posterior modes/HDIs | seconds |
| 9 Half-split analyses | `study2` | `python pct_halfsplit_decile.py`, `python abs_halfsplit_decile.py` | all top-decile vs bottom-90% values in Results (both studies) | seconds |
| 10 Behavioural figures | `study1`, `study2` | `jupyter nbconvert --to notebook --execute analysis.ipynb --ExecutePreprocessor.kernel_name=delayed-planning` | Fig. 2/3B panels (PNG files listed below); see "Notebook cell map" | 2–3 min (sampling cells excluded) |
| 11 Model fits (winning soft-gated MBMC) | `study2` | `python gatedsoft_run_all.py` (Study 2 fit + recovery + Fig. 3B simulation); `python fit_study1_softgate.py` (Study 1) | `em_params_study{1,2}_MBMCgatedsoft.npy`, `simulated_data_gatedsoft.csv`, Fig. 3B simulated panels | hours each |
| 12 Model comparison | `study2` | `python softgate_model_comparison.py` (`--smoke` for a quick run) ; `python softgate_extra_variants.py` | `softgate_model_comparison_BICs.csv` (Fig. 3A right, all in-text ΔBICs), `softgate_extra_variants_BICs.csv` | hours |
| 13 Parameter summaries & Fig. 3C | `study2` | `python summarize_softgate_params.py`, `python fig3c_softgate.py` | Supp. Tables S3–S4, Fig. S7 (`em_params_*_median_iqr.csv`); Fig. 3C panels and ρ values | seconds |
| 14 Recovery analyses | `study2`, `model_fitting_revision` | `python faithful_recovery_softgate.py` (Fig. 3A left); `python recovery_softgate_big.py` (Supp. Fig. S5); `python model_recovery_softgate_reps.py` (Supp. Fig. S4) | `faithful_recovery_softgate_corr.csv`, `recovery_softgate_big_corr.csv`, `results/model_recovery_softgate_reps_confusion.csv` | hours / 15 min / ≈ 6 h |
| 15 Decision-time analyses | `study2` | `python mbmc_rollout_rt_softgate.py` (Supp. Fig. S2), `python rt_lmm_simulated_softgate.py` (Supp. Fig. S6), `python rollout_rt_proxy.py` | `mbmc_simulated_RT_softgate_mean_study2.*`, `rt_lmm_simulated_softgate_*` | minutes / 5 min / minutes |
| 16 SR/PR competitors, V-relinquish variant | `model_fitting_revision` | `python run_map.py study1`, `python run_map.py study2`; `python fit_relinquish_variant.py` | `cbm_response_summary.csv` (Supp. Fig. S3), `results/relinquish_variant_ibic_study2.csv` | minutes |

### 3. Notebook cell map (`analysis.ipynb`)

Both notebooks run top-to-bottom in the environment above with the kernel `delayed-planning`; the two sampling cells can be skipped because the following cells load the stored traces. Cells that depend on files from a superseded model version are listed as *legacy* and are not needed for any reported result.

| Notebook | Cells | Produces | Status |
|---|---|---|---|
| `study1/analysis.ipynb` | 1 | derived columns (identical to `make_lmm_fixed.py`), merge of quiz accuracy | runs |
| | 3–7, 9–13 | Fig. 2A–C, 2E-left panels (`optimal_control*.png`, `controlTaking_by_time*.png`, `variability_*.png`, `optimal_planning_RTs*.png`, `RTs_by_time.png`, `optimalDelayed_by_time.png`, …) | runs (cell 11 fails with seaborn ≥ 0.13 on a legend call; the panels it draws are also saved by cells 9–10) |
| | 8 | Supp. Fig. S1 cost–benefit agent simulation (`simulation_with_metaplanning.png`) | runs |
| | 14–17 | logistic model of control choices over time (`choicedata_model_fitted_best.nc`) | *legacy* — not reported; the trace is not archived |
| | 20–22 | RT mixed model (`pm.sample`, ≈ 30 min) → `RTdata_model_fitted_withintrial.nc`; posterior summaries; Fig. 2D-right/2E-right (`posterior_delayed_planning_reaction*.png`) | runs; cell 22 prints the reported values exactly (0.32 [0.21, 0.43]; 0.21 [0.11, 0.33]) |
| | 24 | correlations between participant-level RT effects and behaviour (Spearman, Bonferroni-corrected) and original-model parameter plots | runs; **the Results report the Pearson correlations** (r = 0.84, −0.35), reproduced by `lmm_posterior_correlations.py` |
| `study2/analysis.ipynb` | 1–5, 8–10, 12–13 | derived columns; Fig. 3B empirical panels (`optimal_control.png`, `optimal_RT_by_planningdepth.png`, `variability_metacontrol.png`, stay plots) | run |
| | 15 | stay-plot of model-simulated data (reads `simulated_data_gatedsoft.csv`) | runs |
| | 16–18 | RT mixed model (`pm.sample`, target_accept 0.80) → `RTdata_model_fitted_withintrial2.nc`; summaries | run |
| | 6, 11, 19, 21, 22 | analyses of the original (pre-revision) model parameters (`MB_B_exec.npy`, …) | *legacy* — superseded by `fig3c_softgate.py` and `summarize_softgate_params.py` |

---

## Map: manuscript result → script → output

### Behaviour (Studies 1 & 2)

| Result | Code | Key outputs |
|---|---|---|
| Fig. 2 behavioural panels, Supp. Fig. S1 | `study1/analysis.ipynb` | `study1/*.png`, `study1/simulation_with_metaplanning.png`, `study1/Figures_Final.pdf` |
| Route-quiz accuracy of retained participants (Results: mean 98.7%, mode 100%) | `study{1,2}/data/route_quiz_accuracy.py` (scoring rule of `correct_quizzes.py`) | `study{1,2}/data/route_quiz_accuracy_all.csv` |
| Permutation test of adaptive control (Fig. 2B right) | `study1/permutation_test_and_visualize.py`, `study1/visualize_perm_test.py`, `study2/permutation_test_control_decision.py` | `study1/permutations_optimal_score*.csv`, `permTest_Visualized.png` |
| Adaptively delayed control score (top-decile definition, Fig. 2C) | `study{1,2}/optimal_delayed_score.py` | `optimal_delayed_scores.csv` |
| Exclusion-criterion check (r = 0.14, p = 0.17) | Pearson correlation of `optimal_delayed_score` and `percent_correct` in `study1/optimal_delayed_scores.csv` | — |
| Hierarchical Bayesian RT mixed model (Fig. 2D/2E) | `study{1,2}/make_lmm_fixed.py` → `study{1,2}/fit_rt_lmm.py` (or notebook cell "RT model") | `lmm_fixed.csv`; `study1/RTdata_model_fitted_withintrial.nc`, `study2/RTdata_model_fitted_withintrial2.nc` |
| βRT random effect vs control-choice accuracy (r = 0.84); interaction vs adaptively delayed control (r = −0.35) | `study1/lmm_posterior_correlations.py` | printed |
| Top decile vs bottom 90% (overall levels, relative and absolute change; both studies) | `study2/pct_halfsplit_decile.py`, `study2/abs_halfsplit_decile.py` | printed stats reported in Results |
| Demographics (Methods) | `study1/demographics_analyze.py`, `study2/demographics/demographics_analyze.py` | `study1/study1_demographics.csv`, `study2/demographics/study2_demographics.csv` |

### Computational modelling (winning soft-gated MBMC model)

| Result | Code | Key outputs |
|---|---|---|
| Winning model definition (soft-gated breadth) | `study2/gated_soft.py` (+ `recovery_common.py`, `recovery_em.py`, `recovery_faithful.py` EM machinery) | — |
| EM / iterative importance-sampling fits | `study2/gatedsoft_run_all.py` (Study 2), `study2/fit_study1_softgate.py` (Study 1) | `study2/em_params_study{1,2}_MBMCgatedsoft.npy` |
| 13-model comparison (Fig. 3A right; baseline BIC 26984.25 and all in-text ΔBICs) | `study2/softgate_model_comparison.py` (generates `mfit_softgate_gen.py` from `model_fitting_revision/mfit_likelihoods.py`) | `softgate_model_comparison_BICs.csv`, `softgate_model_comparison_figure.png` |
| MF learner + with-replacement variants (in-text ΔBICs) | `study2/softgate_extra_variants.py` | `softgate_extra_variants_BICs.csv` |
| V-relinquish variant (in-text ΔBIC = +2) | `model_fitting_revision/fit_relinquish_variant.py` | `results/relinquish_variant_ibic_study2.csv` |
| Parameter recovery at best-fit params (Fig. 3A left, mean r = 0.68) | `study2/faithful_recovery_softgate.py` | `faithful_recovery_softgate_corr.csv`, `_heatmap.png` |
| Model recapitulates behaviour (Fig. 3B bottom row) | `study2/gatedsoft_run_all.py` (simulation block) | `simulated_data_gatedsoft.csv`, `MODELsimulated_GATEDSOFT_*.png`, `stayPlot_SIM_GATEDSOFT.png` |
| Parameter–RT correlations (Fig. 3C: ρ = 0.63, −0.39, 0.34, −0.23, −0.04) | `study2/fig3c_softgate.py` | `study2/*_softgate.png` panels |
| Fitted parameters: Supp. Tables S3–S4, Supp. Fig. S7 | `study2/summarize_softgate_params.py` | `em_params_study{1,2}_median_iqr.csv`, `cbm_MBMCgatedsoft_params_EM_barplots.png` |

### Supplemental analyses

| Supp. item | Code | Key outputs |
|---|---|---|
| Fig. S1 cost–benefit agent simulation | `study1/analysis.ipynb` (cell 8) | `study1/simulation_with_metaplanning.png` |
| Fig. S2 model-derived decision time (rollouts; caption parameter means 1.24, 0.67, 0.48, 0.20, 0.26) | `study2/mbmc_rollout_rt_softgate.py` (+ `mbmc_rollout_rt_median.py`) | `mbmc_simulated_RT_softgate_mean_study2.png/.csv` |
| Rollout RT proxy vs. empirical RT | `study{1,2}/rollout_rt_proxy.py` | `rollout_rt_proxy_*.csv` |
| Fig. S3 SR/PR meta-controllers | `model_fitting_revision/` (`cbm_models.py`, `mfit_models.py`, `run_map.py`; see its README) | `cbm_deltaBIC_vs_MBMC.png`, `cbm_response_summary.csv`, `results/` |
| Fig. S4 model recovery (13 soft-gated models) | `model_fitting_revision/model_recovery_softgate_reps.py` | `model_recovery_softgate_reps_study2.png`, `results/model_recovery_softgate_reps_confusion.csv` |
| Fig. S5 parameter recovery, wide priors (Table S2 = `GROUND_TRUTH` in `recovery_parameter.py`) | `study2/recovery_softgate_big.py` | `recovery_softgate_big_corr.csv`, `_heatmap.png` |
| Fig. S6 simulated delayed-planning RT signature (LMM on model-generated RTs; interaction 0.46 [0.38, 0.53]) | `study2/rt_lmm_simulated_softgate.py` | `rt_lmm_simulated_softgate_posterior.png`, `_trace.nc` |

---

## Pipeline from raw data

```
study*/data/sub-XXX.csv  ──preprocess_raw_data.py──▶  study*/preprocessed_data.csv  ──make_lmm_fixed.py──▶  study*/lmm_fixed.csv
        │                                                                                                          │
        └──correct_quizzes.py──▶ memory_accuracies_subjects_orig_fulltrajectories.csv                              ├──▶ fit_rt_lmm.py / notebook ──▶ RTdata_model_fitted_withintrial*.nc
                                                                                                                   ├──▶ gatedsoft_run_all.py, fit_study1_softgate.py ──▶ em_params_*_MBMCgatedsoft.npy ──▶ comparisons, recovery, Fig. 3C
                                                                                                                   └──▶ optimal_delayed_score.py, pct/abs_halfsplit_decile.py, analysis.ipynb figures
```

Row-order note: the shipped `lmm_fixed.csv` files preserve the participant order of the original raw-file listing; a regenerated file follows `preprocessed_data.csv`. Row order affects no reported statistic, but the participant index of the stored posterior traces follows the shipped order, so `make_lmm_fixed.py` writes `lmm_fixed_regenerated.csv` by default and prints a column-wise comparison (all columns identical in Study 2; in Study 1 only the unused, order-dependent column `MB_decision` differs).

---

## Independent reproducibility check (7 Oct 2026)

Performed on a different computer from the original analyses (Apple Silicon Mac, macOS 27, 18 cores), in a fresh conda environment created from `environment.yml`, from a clean clone of the repository. **(re-run)** = executed end-to-end from the files in this repository and compared with the reported value; **(stored)** = committed output compared with the reported value because a full re-run takes hours (script and inputs present).

| Paper claim | Reported | Reproduced | How |
|---|---|---|---|
| Raw → tidy data (both studies) | — | `preprocessed_data.csv` regenerated **byte-identical** for Study 1 (16,740 rows) and Study 2 (29,340 rows) | re-run (`preprocess_raw_data.py`) |
| Tidy → design matrix | — | `lmm_fixed.csv` regenerated with identical values (Study 2 all columns; Study 1 all but the unused `MB_decision`) | re-run (`make_lmm_fixed.py`) |
| Demographics S1 (51% male, age 39.98) | 51%, 39.98 | 51.00%, 39.98 | re-run |
| Demographics S2 (50.9% male, age 37.90) | 50.9%, 37.90 | 50.92%, 37.90 | re-run |
| Exclusion-criterion correlation | r = 0.14, p = 0.17 | r = 0.145, p = 0.166 | re-run |
| Route-quiz accuracy (Results, Study 1) | mean 98.7%, mode 100% | **mode 100% reproduced; mean not reproduced exactly**: 97.9% with the scoring rule of `data/correct_quizzes.py` (`data/route_quiz_accuracy.py`), 98.1% from the `percent_correct` column shipped in `optimal_delayed_scores.csv` — flagged to the authors | re-run |
| Adaptive-control scores (Fig. 2C) | — | `optimal_delayed_scores.csv` reproduced (max abs. diff 3 × 10⁻¹⁰) | re-run |
| Permutation test (each depth) | p < 0.001 | p < 10⁻⁴ all depths | re-run from stored permutations |
| Study 1 RT model delayed-planning effect | mode 0.32, HDI [0.21, 0.43] | 0.32 [0.21, 0.43] (notebook cell 22) | re-run from stored trace |
| Study 1 delayed-planning × trial interaction | mode 0.21, HDI [0.11, 0.33] | 0.21 [0.11, 0.33] | re-run from stored trace |
| Study 2 RT model (replication) | "replicated" | 0.37 [0.29, 0.44]; interaction 0.24 [0.16, 0.33] | re-run from stored trace |
| βRT random effect vs control-choice accuracy | r = 0.84 | Pearson r = 0.843 (Spearman 0.74) — Study 1 | re-run (`lmm_posterior_correlations.py`) |
| Interaction vs adaptively delayed control | r = −0.35 | Pearson r = −0.352 (Spearman −0.27) — Study 1 | re-run |
| Half-split overall levels / relative / absolute change (both studies) | all Results values | exact match (0.71 vs 0.11; 0.96 vs 0.06; +41% [17, 70] vs +218% [100, 534], p = 0.0004; +21% [5, 45] vs +486%, p = 0.095; +0.24 [0.11, 0.37] vs +0.11 [0.07, 0.16], p = 0.077; +0.18 [0.05, 0.32] vs +0.09 [0.03, 0.15], p = 0.23) | re-run |
| Model-comparison BIC ladder (baseline BIC + 8 in-text ΔBICs) | 26984.25; 2276.45, 2313.87, 262.44, 1038.62, 261.56, 689.25; MF 437.92; V-relinquish +2 | all exact; +1.7 | stored (`softgate_model_comparison_BICs.csv`, `softgate_extra_variants_BICs.csv`, `relinquish_variant_ibic_study2.csv`); `softgate_model_comparison.py --smoke` re-run (23 s) confirms the pipeline executes |
| Fig. 3C correlations | ρ = 0.63, −0.39, −0.23, −0.04 (and βMBMC vs βRT) | 0.630, −0.386, −0.228, −0.044 (0.340) | re-run (`fig3c_softgate.py`) |
| Fig. 3A-left faithful recovery | mean r = 0.68 | 0.677 | stored (refit ≈ hours) |
| Supp. Tables S3/S4 medians + IQRs | all 36 values | exact from `em_params_*_MBMCgatedsoft.npy` | re-run (`summarize_softgate_params.py`) |
| Supp. Fig. S2 caption parameter means | 1.24, 0.67, 0.48, 0.20, 0.26 | 1.241, 0.671, 0.485, 0.199, 0.259 | re-run from stored fits |
| Supp. Fig. S4 model recovery | full model 0.95; 12/13 ≥ 0.90; 9 perfect; MBMC_BD 0 | exact | stored (re-run ≈ 6 h) |
| Supp. Fig. S5 wide-prior recovery (N = 1000 synthetic participants) | heatmap diagonal (mean r = 0.61) | stochastic re-run (8 min, 16 cores): mean r = 0.60, every parameter within 0.07 of the shipped value (`recovery_softgate_big_corr.csv`) | re-run |
| Supp. Fig. S6 simulated interaction | mean 0.46, HDI [0.38, 0.53] | 0.456 [0.383, 0.527] | re-run from stored trace |
| SR/PR ΔBIC (Supp. Fig. S3) | 589.7 / 1044.3 (SR), 1348.7 / 2103.0 (PR) | exact | stored (`cbm_response_summary.csv`) |

**Corrections made to the manuscript as a result of this check** (tracked changes in the resubmitted manuscript): the RT models were sampled with **four** NUTS chains (not two) and Study 2 used `target_accept = 0.80`; R̂ ≤ 1.01 holds for every population-level coefficient, but the standard deviations of the near-zero random slopes (goal switch, DelayedPlan × Trial; control state in Study 2) have R̂ = 1.12–1.65 and low ESS, so the Methods now state this; the correlations r = 0.84 and r = −0.35 are Pearson correlations computed on Study 1. A non-centred refit of both models (`fit_rt_lmm.py --noncentered --target-accept 0.99`, 4 chains) converges (all R̂ ≤ 1.02, no divergences) with identical population-level estimates (Study 1: 0.32 [0.22, 0.44] and 0.22 [0.11, 0.34]; Study 2: 0.36 [0.29, 0.44] and 0.25 [0.16, 0.32]); see `ROBUSTNESS_RESULTS.md`.

Not independently re-derived here (script and data present; expected runtimes above): the EM model fits themselves, the full 13-model comparison refit, the Fig. 3A faithful recovery, the Supp. Fig. S4 model recovery, and the empirical RT-model sampling itself (the stored traces were used; `fit_rt_lmm.py` refits them).

---

## Robustness checks for the preregistration-deviations table

Supplementary Table S5 of the manuscript reports deviations from the preregistrations. The checks it cites were run from this repository with `statsmodels` (frequentist linear mixed model, REML, same fixed effects as the Bayesian model, random intercept and random slopes for DelayedPlan and DelayedPlan × Trial, Wald z-tests) and with `fit_rt_lmm.py` (Bayesian refits):

| Check | Study 1 | Study 2 |
|---|---|---|
| Frequentist model, all trials (as analysed) | DelayedPlan b = 0.33, SE 0.06, p = 7 × 10⁻⁸; interaction b = 0.22, SE 0.07, p = 0.001 | b = 0.37, SE 0.04, p = 7 × 10⁻¹⁷; b = 0.24, SE 0.06, p = 2 × 10⁻⁵ |
| Frequentist model, optimally-delayed trials only (preregistered selection) | b = 0.95, SE 0.07, p < 10⁻³⁸; interaction b = 0.14, SE 0.10, p = 0.17 (random-intercept-only: b = 0.08, p = 0.25) | b = 0.99, SE 0.06, p < 10⁻⁶⁹; interaction b = 0.25, SE 0.06, p = 7 × 10⁻⁵ |
| Frequentist model excluding the 10 pilot participants (collected before preregistration) | b = 0.30, SE 0.06, p = 4 × 10⁻⁶; interaction b = 0.22, SE 0.08, p = 0.004 | — |
| Bayesian refits (`fit_rt_lmm.py --exclude-subs …`, `--optimally-delayed-only`, `--noncentered`) | see `ROBUSTNESS_RESULTS.md` | see `ROBUSTNESS_RESULTS.md` |

---

## Data description and anonymisation

- **Raw data:** one PsychoPy session file per participant in `study*/data/` (`sub-XXX.csv`), containing the complete trial-by-trial record of training, memory quizzes, planning phase and questionnaires (PsychoPy `thisExp` export convention). `study*/data/bad_memory/` holds sessions excluded for failing the memory quizzes; `study2/data/` also contains incomplete sessions that were never analysed.
- **Anonymisation:** all platform identifiers (`PROLIFIC_PID`, `STUDY_ID`, `SESSION_ID`) and the free-text `participant` field are replaced by the anonymised code or `REDACTED`; file names carry only the anonymised code; no names, e-mail addresses, IP addresses, dates of birth or web identifiers are present. Demographics files contain age and sex only. The code ↔ identifier mapping is held offline by the authors.
- **Derived data:** `preprocessed_data.csv` (tidy decision-level data) and `lmm_fixed.csv` (plus derived regressors) per study; fitted parameters (`.npy`), posterior traces (`.nc`) and comparison outputs (`.csv`).
- **Full column-level documentation:** [`data_dictionary.md`](./data_dictionary.md).

## Materials

The complete task implementation (PsychoPy Builder file, PsychoJS web export, Python export), all stimuli, the consent form, the condition files and the questionnaires are in [`study2/task/`](./study2/task/) — see [`study2/task/README.md`](./study2/task/README.md) for a file-by-file description and the procedure. Both studies used this experiment; the archived files are the Study 2 build (PsychoJS 2023.2.3), which differs from the Study 1 build (2021.1.3) only in showing feedback on the training quizzes and in the additional Study 2 questionnaires.

## Preregistrations and deviations

- Study 1: https://doi.org/10.17605/OSF.IO/QS9JA — registered 26 May 2023 after a pilot sample of 10 participants (sessions of 4–5 August 2022; `sub-009, -048, -049, -054, -055, -058, -061, -064, -071, -073`) had been collected and analysed (the pilot analyses are attached to the registration); the remaining participants were collected on 26–29 May 2023 and the pilot participants are included in the Study 1 sample.
- Study 2: https://doi.org/10.17605/OSF.IO/5Y9Z6 — registered 18 June 2024, before data collection (24–25 June 2024).
- All deviations from the preregistrations, with their justification and robustness checks, are listed in Supplementary Table S5 of the manuscript (Psychological Science deviation-table template).

## File inventory

### Root
| File | Description |
|---|---|
| `README.md`, `data_dictionary.md` | This file; column-level data documentation |
| `environment.yml`, `CITATION.cff`, `.zenodo.json`, `LICENSE`, `.gitignore` | Environment specification; citation metadata; Zenodo record metadata; CC BY 4.0 licence; ignore rules |

### `study1/` (Experiment 1)
| File | Description |
|---|---|
| `data/` | Raw PsychoPy session .csv per participant (`sub-XXX.csv`), `preprocess_raw_data.py` (raw → tidy), `correct_quizzes.py` (quiz-based exclusion), `route_quiz_accuracy.py` + `route_quiz_accuracy_all.csv` (route-quiz accuracy of every participant), `bad_memory/` |
| `analysis.ipynb` | Main notebook: Fig. 2 panels, quiz accuracy, RT model fit and posterior summaries, Supp. Fig. S1 simulation |
| `make_lmm_fixed.py`, `fit_rt_lmm.py`, `lmm_posterior_correlations.py` | Design matrix; RT mixed model (standalone, with non-centred option); reported correlations |
| `preprocessed_data.csv`, `lmm_fixed.csv` | Tidy decision-level data; design matrix |
| `RTdata_model_fitted_withintrial.nc` | Posterior trace of the hierarchical RT model (Fig. 2D/2E stats) |
| `permutation_test_and_visualize.py`, `visualize_perm_test.py`, `permutationTest_notebook.ipynb` | Permutation test of adaptive control (Fig. 2B right) |
| `permutations_optimal_score.csv`, `permutations_optimal_score_ACTUALSUBS.csv` | Permuted and actual optimal-control scores |
| `optimal_delayed_score.py`, `optimal_delayed_scores.csv` | Per-participant adaptively-delayed-control score (top-decile definition) |
| `demographics_analyze.py`, `study1_demographics.csv` | Methods demographics |
| `memory_accuracies_subjects_orig_fulltrajectories.csv` | Output of `data/correct_quizzes.py` (lists only sessions that failed the cutoff; header-only in Study 1 because the failing sessions had already been moved) |
| `rollout_rt_proxy.py`, `rollout_rt_proxy_*.csv` | Model-derived decision-time proxy vs empirical RT (Study 1) |
| `CB_exec.npy`, `MB_*.npy`, `breadth2_exec.npy`, `cache_*.npy`, `forget_exec.npy`, `mbcache_exec.npy` | Parameters of the original (pre-revision) model, loaded by legacy notebook cells |
| `Figures_Final.pdf` | Assembled final figures |
| `simulation_with_metaplanning.png` | Supp. Fig. S1 |
| `permTest_Visualized.png`, `optimal_planning_RTs*.png`, `posterior_*.png`, `controlTaking_by_time*.png`, `optimalDelayed_by_time.png`, `optimal_RT_overtime.png`, `RTs_by_time.png`, `optimal_control*.png`, `optimal_action_choice.png`, `optimal_metacontrol_choice.png`, `correct_control_action.png`, `total_score_plot.png`, `variability_*.png`, `simulated_optimal_Control_by_planningdepth.png`, `optimal_controlactualparticipantsempiricaldata*.png` | Fig. 2 panel images (regenerated by `analysis.ipynb`) |

### `study2/` (Experiment 2)
| File | Description |
|---|---|
| `data/` | Raw session .csv per participant, `preprocess_raw_data.py`, `correct_quizzes.py`, `memory_accuracies_subjects_orig_fulltrajectories.csv`, `bad_memory/` |
| `task/` | Task implementation and stimulus assets (materials) — see `task/README.md` |
| `demographics/` | `study2_demographics.csv` + `demographics_analyze.py` |
| `analysis.ipynb` | Behavioural notebook: Fig. 3B empirical panels, RT model fit and summaries |
| `make_lmm_fixed.py`, `fit_rt_lmm.py`, `lmm_posterior_correlations.py` | As for Study 1 |
| `preprocessed_data.csv`, `lmm_fixed.csv` | Tidy decision-level data; design matrix |
| `RTdata_model_fitted_withintrial2.nc` | Posterior trace of the Study 2 RT model |
| `permutation_test_control_decision.py`, `visualize_perm_test.py` | Study 2 permutation test |
| `optimal_delayed_score.py`, `optimal_delayed_scores.csv` | Per-participant adaptive-control score |
| `pct_halfsplit_decile.py`, `abs_halfsplit_decile.py` | Top decile vs bottom 90% half-split statistics (both studies) |
| `gated_soft.py` | **Winning soft-gated MBMC model** (likelihood + simulator) |
| `recovery_common.py`, `recovery_em.py`, `recovery_faithful.py`, `recovery_likelihoods.py` | EM / iterative importance-sampling machinery and the 13-model likelihood library |
| `mfit_softgate_gen.py` | Auto-generated soft-gated likelihoods (regenerated by `softgate_model_comparison.py`) |
| `gatedsoft_run_all.py`, `fit_study1_softgate.py` | EM fits of the winning model (Study 2 incl. recovery + Fig. 3B simulation; Study 1) |
| `fit_real_em.py`, `em_params_study{1,2}_MBMC.npy` | Original-model EM fit (reference; superseded) |
| `em_params_study{1,2}_MBMCgatedsoft.npy` | **Fitted parameters (winning model), native space** — source of Tables S3/S4, Fig. S7, Fig. S2 caption |
| `summarize_softgate_params.py`, `em_params_study{1,2}_median_iqr.csv` | Medians/IQRs for Supp. Tables S3–S4 |
| `softgate_model_comparison.py`, `softgate_model_comparison_BICs.csv`, `softgate_model_comparison_figure.png` | 13-model iBIC comparison (Fig. 3A right + in-text ΔBICs) |
| `softgate_extra_variants.py`, `softgate_extra_variants_BICs.csv` | MF learner and with-replacement variants |
| `faithful_recovery_softgate.py`, `faithful_recovery_softgate_corr.csv`, `_heatmap.png` | Fig. 3A-left parameter recovery |
| `fig3c_softgate.py`, `*_softgate.png` | Fig. 3C parameter–RT correlation panels |
| `simulated_data_gatedsoft.csv`, `MODELsimulated_GATEDSOFT_*.png`, `controlTaking_by_time_depth*_SIM_GATEDSOFT.png`, `stayPlot_SIM_GATEDSOFT.png`, `stayPlot_ALLPerformingSubjects_SIM.png` | Fig. 3B simulated-behaviour panels |
| `mbmc_rollout_rt_softgate.py`, `mbmc_rollout_rt_median.py`, `mbmc_simulated_RT_softgate_mean_study2.{png,csv}` | Supp. Fig. S2 |
| `rollout_rt_proxy.py`, `rollout_rt_proxy_*.csv`, `rollout_proxy_over_trials.png`, `true_vs_simulated_effects.png` | Decision-time proxy vs empirical RT (Study 2) |
| `recovery_parameter.py` | Wide generating priors (**Supp. Table S2** = `GROUND_TRUTH`) + recovery driver |
| `recovery_softgate_big.py`, `recovery_softgate_big_corr.csv`, `_heatmap.png` | Supp. Fig. S5 wide-prior parameter recovery (N = 1000) |
| `recovery_gatedsoft_corr_mean.csv`, `recovery_gatedsoft_heatmap.png` | Empirical-prior recovery of the winning model |
| `rt_lmm_simulated_softgate.py`, `rt_lmm_simulated_softgate_{data.csv,posterior.png,trace.nc}` | Supp. Fig. S6 |
| `cbm_MBMCgatedsoft_params_EM_barplots.png` | Supp. Fig. S7 |
| `optimal_control.png`, `optimal_RT_by_planningdepth.png`, `variability_metacontrol.png` | Fig. 3B empirical panels (from `analysis.ipynb`) |

### `model_fitting_revision/` (SR/PR competitors, recovery, variants)
| File | Description |
|---|---|
| `README.md` | Pipeline documentation for this folder |
| `cbm_models.py`, `mfit_models.py`, `mfit_likelihoods.py`, `fastdata.py` | SR / PR / CB / MBMC model definitions and likelihoods (Supp. Fig. S3) |
| `run_map.py` | Per-subject MAP fits + summed BIC (the reported SR/PR comparison) |
| `run_cbm.py`, `fast_lap.py`, `make_notebook.py`, `cbm_model_fitting_r1.ipynb` | Full CBM (Laplace/HBI) pipeline + rendered notebook |
| `fit_relinquish_variant.py`, `mfit_likelihoods_relhalf.py` | V-relinquish variant refit (in-text ΔBIC = +2) |
| `model_recovery_softgate_reps.py`, `recovery_mbmc_sim.py`, `model_recovery_softgate_reps_study2.png` | Supp. Fig. S4 model recovery |
| `cbm_deltaBIC_vs_MBMC.png`, `cbm_response_summary.csv` | Supp. Fig. S3 figure and SR/PR ΔBIC summary |
| `results/` | Per-subject and group-level fit summaries, MAP parameters, confusion matrix, relinquish-variant iBICs |

---

## Archiving, citation and license

GitHub is not a trusted repository under *Psychological Science*'s policy (no immutable versions or persistent identifiers), so the version of record is archived on **Zenodo** through the GitHub–Zenodo integration: enable the repository at https://zenodo.org/account/settings/github/, create a GitHub release (e.g. `v1.0.0`), and Zenodo archives the release and mints a DOI using the metadata in `.zenodo.json`. Insert the DOI at the top of this file and in the manuscript's Research Transparency Statement.

Please cite the article and the archive (see `CITATION.cff`):

> Sharp, P. B., & Eldar, E. (in press). Humans adaptively delay planning using cognitive maps. *Psychological Science*.
> Sharp, P. B., & Eldar, E. (2026). Humans adaptively delay planning using cognitive maps: data, task materials and analysis code [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

All data, materials and code are released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0; see `LICENSE`).
