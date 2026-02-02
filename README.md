# Humans adaptively delay planning using cognitive maps

Welcome to the companion repository for **“Humans adaptively delay planning using cognitive maps”** by **Paul B. Sharp & Eran Eldar**. This repo contains the raw data, preprocessing pipelines, and analysis notebooks for the two behavioural experiments reported in the manuscript.

---

## ✨ Study Summary

Planning is computationally costly.  In complex, multi‑step problems it is often more efficient to ***delay*** detailed planning until doing so is actually useful.  We created a decision task in which—at specific nodes—every available action is equally good, making it *optimal to relinquish control* and postpone planning.  Across two experiments we show that human participants learn to identify these nodes and **delay planning optimally**, improving with experience.  A formal meta‑control model reveals that this behaviour is driven by a **search over a cognitive map of the task**, rather than by simple reinforcement from past outcomes.

---

## 🗂️ Repository Structure

```
.
├── study1/                       ← Material for Experiment 1
│   ├── data/                     ← Raw .csv files (filenames begin with 5* or 6*)
│   ├── data/preprocess_raw_data.py    ← Cleaning / wrangling script
│   └── analysis.ipynb            ← Main analysis notebook
│
├── study2/                       ← Material for Experiment 2
│   ├── data/
│   ├── data/preprocess_raw_data.py
│   └── analysis.ipynb
│
└── README.md                     ← *You are here*
```

> **Quick links** • [study 1](./study1/) → [data](./study1/data/) · [preprocess\_raw\_data.py](./study1/data/preprocess_raw_data.py) · [analysis.ipynb](./study1/analysis.ipynb) • [study 2](./study2/) → [data](./study2/data/) · [preprocess\_raw\_data.py](./study2/data/preprocess_raw_data.py) · [analysis.ipynb](./study2/analysis.ipynb)

---

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/<user>/delayed‑planning.git
   cd delayed‑planning
   ```

2. **Create the environment** (conda recommended)

   ```bash
   conda env create -f environment.yml
   conda activate delayed-planning
   ```

3. **Run the preprocessing** (raw → tidy CSVs)

   ```bash
   python study1/preprocess_raw_data.py
   python study2/preprocess_raw_data.py
   ```

4. **Generate **``

   Open *either* `study1/analysis.ipynb` or `study2/analysis.ipynb` and **run only the first cell**.\
   This writes `lmm_fixed.csv` to the repository root—*model\_fitting.py* needs this file.

5. **Fit the computational models**

   ```bash
   python model_fitting.py
   ```

6. **Run the full analyses**

   Open the notebooks again and execute the remaining cells to reproduce every figure and statistic reported in the paper.

---

## 🐍 Python Dependencies

The analysis notebooks (`studyX/analysis.ipynb`) and model‑fitting script (`model_fitting.py`) rely on the following third‑party libraries.  Exact versions correspond to the development environment and are pinned in *environment.yml*.

| Package                      | Version           | Purpose                                              |
| ---------------------------- | ----------------- | ---------------------------------------------------- |
| `numpy`                      | 2.1.3             | Core numerical arrays & linear algebra               |
| `pandas`                     | 2.2.3             | Data wrangling & I/O                                 |
| `scipy`                      | 1.15.1            | Scientific computing utilities (stats, optimisation) |
| `matplotlib`                 | 3.10.0            | Plotting backend (used implicitly by seaborn)        |
| `seaborn`                    | 0.13.2            | Statistical data visualisation                       |
| `arviz`                      | 0.21.0            | Bayesian model diagnostics & visualisation           |
| `pymc`                       | 5.22.0            | Probabilistic programming / Bayesian inference       |
| `statsmodels`                | 0.14.4            | Classical statistical modelling                      |
| `xarray` & `xarray‑einstats` | 2024.11.0 / 0.6.0 | Label‑aware N‑D arrays (required by ArviZ)           |

> **Note**   `pymc` pulls in `pytensor` and (via optional back‑ends) JAX or Aesara.  These transitive dependencies are handled automatically by conda.

A minimal *environment.yml* to reproduce all analyses:

```yaml
name: delayed-planning
channels:
  - conda-forge
dependencies:
  # Core
  - python=3.13
  - numpy=2.1.3
  - pandas=2.2.3
  - scipy=1.15.1

  # Visualisation
  - matplotlib=3.10.0
  - seaborn=0.13.2

  # Bayesian modelling & statistics
  - pymc=5.22.0
  - arviz=0.21.0
  - statsmodels=0.14.4

  # ArviZ backend helpers
  - xarray=2024.11.0
  - xarray-einstats=0.6.0

  # Notebook support (optional but convenient)
  - jupyterlab
  - ipykernel
```

If you prefer **pip**, the same set of pinned versions is available in `requirements.txt`.

---

## 📝 Data Description

- **File format:** `.csv`
- **Location:** `studyX/data/`
- **Naming convention:** Raw files start with `5` or `6` followed by participant/session identifiers (e.g., `5_sub‑01.csv`).
- **Contents:** Trial‑level records with participant choice, reaction times, task state variables, and feedback.

> The preprocessing scripts standardise variable names, remove practice trials, and output tidy data frames ready for analysis.

---

## 🔧 Code Overview

| File                     | Purpose                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `preprocess_raw_data.py` | Loads raw CSVs, performs cleaning, and exports `tidy_data.csv`.                                             |
| `analysis.ipynb`         | Reproduces all figures and stats reported in the paper (model fits, behavioural stats, parameter recovery). |
| `model_fitting.py`       | Hierarchical EM fitting for all computational models.                                                       |

---

## 📄 Citation

If you use this code or data, please cite:

```text
Sharp, P. B. & Eldar, E. (2025). Delayed planning in human decision making. <Journal / preprint DOI>
```

---

## 🤝 Contributing

Pull requests are welcome!  If you find a bug or have a suggestion, please open an issue.

---

## 🛡️ License

This project is licensed under the CC-BY-4.0 License – see `LICENSE` for details.

---

## 📧 Contact

For questions, please contact **Paul B. Sharp** ([paul.sharp@biu.ac.il](mailto\:paul.sharp@biu.ac.il)) or open an issue on GitHub.
