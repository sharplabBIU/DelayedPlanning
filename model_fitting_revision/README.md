# `model_fitting_revision` — CBM model fitting for Revision 1

Re-fits the delayed-planning meta-control model space with the **Computational &
Behavioural Modelling toolbox (CBM; Piray et al., 2019)** — Python port
[`cbm_python`](https://github.com/payampiray/cbm_python) — replacing the in-house
hierarchical Expectation–Maximisation procedure in `study*/model_fitting.py`.

It adds the two new offline meta-controllers Reviewer 1 requested (R1.7/R1.8):

* **SR** — a *successor-representation* meta-controller. Goal reachability is
  read off a forward, random-policy successor representation formed **offline,
  before the planning phase**. Control is taken/relinquished by the reviewer's
  rule: *"if both actions reach the goal about equally, relinquish."*
* **PR** — a *predecessor-representation* meta-controller (Sharp & Eldar, 2024):
  the same rule, but using the retrospective posterior P(origin | goal reached)
  — the Bayes inverse of the SR.

Both are **static across trials** (no in-trial sampling, no learning), so by
construction they cannot reproduce the trial-by-trial improvement in
adaptively-delayed planning that the winning **MBMC** model captures.

## Files

| File | Purpose |
|---|---|
| `cbm_models.py` | All likelihoods (MBMC ported verbatim from `model_fitting.py`, plus native SR/PR/CB), CBM wrappers, data loader. |
| `run_map.py` | **Fast (default).** Per-subject MAP, parallelised across cores, MBMC warm-started from its per-subject EM fit → **ΔBIC vs MBMC**. Minutes, not hours. |
| `run_cbm.py` | **Full (optional, slow).** CBM `cbm_lap` (Laplace evidence) → `cbm_hbi` (model frequencies + protected exceedance). |
| `make_notebook.py` | Regenerates the analysis notebook. |
| `cbm_model_fitting_r1.ipynb` | **Main deliverable** — model-comparison plots for both studies. |
| `results/` | `fits_*.csv`, `group_*.csv`, `map_params_*.npy` (fast route); `lap_*.pkl`, `hbi_summary_*.pkl` (full route). |

## How to run

Use the `coding_basic` conda environment (where `cbm` is installed):

```bash
conda activate coding_basic       # or: /opt/miniconda3/envs/coding_basic/bin/python
cd model_fitting_revision

# FAST default — per-subject MAP, ΔBIC vs MBMC (a few minutes per study):
python run_map.py study1
python run_map.py study2

# FULL CBM (optional, slow) — Laplace model evidence + HBI exceedance:
python run_cbm.py study1
python run_cbm.py study2
python run_cbm.py study1 --no-hbi      # Laplace only
```

Then open `cbm_model_fitting_r1.ipynb` and Run All — it loads `results/` and
produces every plot. Re-running `run_cbm.py` reuses any cached `lap_*.pkl`.

## Model set

| Model | k | Description |
|---|---|---|
| `MBMC` | 9 | Winning Cache-MC + Replan model. In-trial sampling + caching/forgetting/perseveration + control bias. Identical likelihood to the EM winner (`MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution`). |
| `SR` | 4 | Offline successor-representation meta-controller. Params: β (value weight), γ (SR discount), CB (control bias), κ_R (relinquish-reward weight). |
| `PR` | 4 | Offline predecessor-representation meta-controller (same params). |
| `CB` | 1 | Control-bias-only baseline. |

## Observation model

Identical to the EM code: at each of the 3 decisions per trial the agent makes a
binary meta-control choice `choice_numeric` (0 = take control [left/right],
1 = relinquish [space]); the log-likelihood is the summed log-probability of the
observed choices. The MBMC port was checked to reproduce the EM likelihood
**to machine precision**.

## Notes

* `num_init` (random restarts per subject) defaults to 10. The CBM default
  `min(7·d, 100)` ≈ 63 for MBMC is prohibitively slow; 10 is ample for these
  smooth likelihoods, and HBI warm-start refinement runs on top.
* Prior on unconstrained parameters: zero-mean Gaussian, variance 6.25 (CBM
  default broad prior). Native parameter spaces are recovered by transforms
  (`exp` for positive / EM-`gamma`, `sigmoid` for unit / EM-`beta`, identity for
  real / EM-`norm`).
