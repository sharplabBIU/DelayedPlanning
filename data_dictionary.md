# Data dictionary

This document describes the data files shared in this repository (STAR item 8.5). The same schema applies to Study 1 and Study 2.

## Anonymization

All participant identifiers have been removed. Session files are named `sub-001.csv`, `sub-002.csv`, … per study, in the alphabetical order of the original session file names: analysed participants first (Study 1 `sub-001`–`sub-081`, Study 2 `sub-001`–`sub-163`), then the sessions excluded for failing the memory quizzes in `bad_memory/` (Study 1 `sub-082`–`sub-090`, Study 2 `sub-164`–`sub-257`); the ten Study 1 pilot sessions in `pilot_preregistration/` are `pilot-01`–`pilot-10`. The same codes are used in the `sub` column of every derived file (as `sub-XXX.csv`). The Study 1 session files were re-downloaded from Pavlovia on 7 Oct 2026 and anonymised afresh with this scheme; the re-download removed two duplicate copies of the same session that the earlier anonymisation had counted as separate participants (inflating the Study 1 sample to 83). Inside the raw files, the recruitment-platform identifiers (`PROLIFIC_PID`, `STUDY_ID`, `SESSION_ID`) are set to the anonymised code or to `REDACTED`, and the free-text `participant` field (which some participants filled with initials, a first name or their platform ID) has been replaced by the anonymised code in every file. The only remaining session metadata are the PsychoPy session timestamp (`date`), operating system (`OS`) and PsychoPy version. `study{1,2}/data/bad_memory/` contains sessions excluded for failing the memory quizzes; `study2/data` additionally contains incomplete sessions that were never analysed. `study1/data/pilot_preregistration/` holds the ten pilot sessions collected in August 2022, before Study 1 was preregistered; they were analysed for the registration's preliminary results and are excluded from every analysis in the manuscript (the preprocessing script only reads the parent folder). The demographics files contain only age and sex (Prolific export columns `Status`, `Age`, `Sex`; rows without a `sub` code are returned/unmatched submissions). The mapping between anonymised codes and platform identifiers is held offline by the authors and is not shared.

## Raw data (`study{1,2}/data/*.csv`)

One PsychoPy session file per participant, containing the complete trial-by-trial record: training-phase navigation trials, memory quizzes (one-step and full-route), and planning-phase trials. Columns follow PsychoPy's `thisExp` export convention (`<component>.keys`, `<component>.rt`, plus task state variables). `study{1,2}/data/preprocess_raw_data.py` converts these into the tidy files below.

## `study{1,2}/preprocessed_data.csv`

Tidy planning-phase data: one row per decision (3 decisions × 60 trials per participant; Study 1 N = 81, Study 2 N = 163).

| Column | Description |
|---|---|
| `sub` | Participant/session identifier |
| `trial_num` | Trial number across the planning phase |
| `trial_num_within_goal` | Trial number within the current goal block (1–20) |
| `current_state` | State occupied at this decision |
| `decision` | Decision step within the trial (1–3) |
| `got_to_goal` / `got_to_goal_last` | Whether the current / previous trial ended at the instructed goal |
| `goal_switch` | 1 if the instructed goal changed relative to the previous trial |
| `control_regressor` | Optimal control state at this decision (1 = relinquishing is optimal) |
| `RT` | Reaction time for this decision (s) |
| `eligible_decisions_accuracy` | Accuracy over decisions where a specific action was required |
| `retrieved_cached` | Whether the previous control choice at this state–goal pair is repeated |
| `planning_depth` | Required planning depth of the instructed goal (1–3) |
| `delayed_planning` | 1 = the depth-appropriate planning-initiation decision (the delayed-planning indicator in the RT LMM) |
| `choices` | Raw choice (action taken or relinquish) |
| `worry` | Self-reported worry score (collected but not analyzed in the paper) |
| `optimally_delayed` | 1 = control was delayed when optimal to delay |
| `optimally_control_choice` | 1 = control choice (take or relinquish) was optimal |
| `optimally_delayed_last` | Previous-trial value of `optimally_delayed` |

## `study{1,2}/lmm_fixed.csv`

`preprocessed_data.csv` plus derived regressors used by the RT linear-mixed model, the computational-model fits and the behavioural analyses. It is produced from `preprocessed_data.csv` by `study{1,2}/make_lmm_fixed.py` (the column-construction code of the first notebook cell, made standalone). Two provenance notes: (1) the shipped file keeps the participant/row order of the original raw-file listing, whereas a regenerated file follows the order of `preprocessed_data.csv` — row order affects no reported statistic, but the participant index of the stored posterior traces (`RTdata_model_fitted_withintrial*.nc`) follows the shipped file, so `make_lmm_fixed.py` writes `lmm_fixed_regenerated.csv` by default and reports a column-wise comparison; (2) in Study 1 the column `MB_decision` depends on the row order in which goal-reaching trials are first encountered and is not used in any reported analysis. Additional columns:

| Column | Description |
|---|---|
| `choice_numeric`, `choices_numeric`, `choice_numeric_last` | Numeric codings of the control choice (current / previous) |
| `interaction_won_and_metachoice` | Previous-outcome × control-choice interaction coding |
| `got_to_goal_retrieved_cached` | Reward-conditioned repetition coding |
| `MB_decision` | Decision requiring model-based control |
| `optimal_metacontrol_choice` (+ `_accurate`, `_last`) | Optimal-meta-control coding (current / previous) |
| `over_planning`, `over_control` | Indicators of taking control where relinquishing was optimal |
| `points_from_choice`, `points_from_goal`, `trial_points`, `total_points` | Points earned (relinquish bonus, goal reward, per-trial, cumulative) |
| `correct_control_action` | Correct action chosen when control was taken |
| `meta_action` | Combined meta-control/action coding |
| `switch_order` | Goal-block order |
| `goal_reachability` | Number of actions from the current state that can still reach the goal |

## Model-fit outputs

| File | Description |
|---|---|
| `study2/em_params_study{1,2}_MBMCgatedsoft.npy` | Per-participant EM posterior-mean parameters of the winning soft-gated MBMC model, native space; columns ordered βMBMC, γd, b̃1, b̃2, κC, βCB, γC, κR, ωP |
| `study2/em_params_study{1,2}_median_iqr.csv` | Median/IQR/mean/SEM summaries of the above (Supp. Tables S3–S4, Fig. S7) |
| `study2/softgate_model_comparison_BICs.csv` | iBIC for all 13 candidate models (Fig. 3A right) |
| `study2/softgate_extra_variants_BICs.csv` | iBIC for the MF-learner and with-replacement variants |
| `study{1,2}/RTdata_model_fitted_withintrial*.nc` | ArviZ/NetCDF posterior traces of the hierarchical RT LMMs |
| `model_fitting_revision/results/` | SR/PR MAP fits, model-recovery confusion matrix, relinquish-variant iBICs (see that folder's README) |

## `study{1,2}/optimal_delayed_scores.csv`

Per-participant adaptively-delayed-control score (`optimal_delayed_score`; top-decile definition used in Fig. 2C and the half-split analyses), PSWQ worry total (`worry`), and in Study 1 the route-quiz accuracy (`percent_correct`, merged from `memory_accuracies_subjects_orig_fulltrajectories.csv`); Study 2 additionally has the momentary-stress total (`stress`) and a worry manipulation-check item (`manipCheckWorry`). Produced by `study{1,2}/optimal_delayed_score.py`.

## Demographics

`study1/study1_demographics.csv` and `study2/demographics/study2_demographics.csv`: recruitment-platform exports used for the Methods demographics (age, sex).
