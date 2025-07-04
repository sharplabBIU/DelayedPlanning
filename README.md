# Delayed Planning in Human Decision Making

Welcome to the companion repository for **“Delayed planning in human decision making”** by **Paul B. Sharp & Eran Eldar**.
This repo contains the raw data, preprocessing pipelines, and analysis notebooks for the two behavioural experiments reported in the manuscript.

---

## ✨ Study Summary

Planning is computationally costly.  In complex, multi‑step problems it is often more efficient to ***delay*** detailed planning until doing so is actually useful.  We created a decision task in which—at specific nodes—every available action is equally good, making it *optimal to relinquish control* and postpone planning.  Across two experiments we show that human participants learn to identify these nodes and **delay planning optimally**, improving with experience.  A formal meta‑control model reveals that this behaviour is driven by a **search over a cognitive map of the task**, rather than by simple reinforcement from past outcomes.

---

## 🗂️ Repository Structure

```
.
├── study1/                       ← Material for Experiment 1
│   ├── data/                     ← Raw .csv files (filenames begin with 5* or 6*)
│   ├── preprocess_raw_data.py    ← Cleaning / wrangling script
│   └── analysis.ipynb            ← Main analysis notebook
│
├── study2/                       ← Material for Experiment 2
│   ├── data/
│   ├── preprocess_raw_data.py
│   └── analysis.ipynb
│
└── README.md                     ← *You are here*
```

> **Quick links**
> • [study 1](./study1/) → [data](./study1/data/) · [preprocess\_raw\_data.py](./study1/preprocess_raw_data.py) · [analysis.ipynb](./study1/analysis.ipynb)
> • [study 2](./study2/) → [data](./study2/data/) · [preprocess\_raw\_data.py](./study2/preprocess_raw_data.py) · [analysis.ipynb](./study2/analysis.ipynb)

---

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/<user>/delayed‑planning.git
   cd delayed‑planning
   ```
2. **Create the environment** (conda recommended)

   ```bash
   conda env create -f environment.yml   # or install requirements.txt
   conda activate delayed-planning
   ```
3. **Run the preprocessing**

   ```bash
   python study1/preprocess_raw_data.py
   python study2/preprocess_raw_data.py
   ```
4. **Open the analysis notebooks**

   ```bash
   jupyter notebook study1/analysis.ipynb
   jupyter notebook study2/analysis.ipynb
   ```

---

## 📝 Data Description

* **File format:** `.csv`
* **Location:** `studyX/data/`
* **Naming convention:** Raw files start with `5` or `6` followed by participant/session identifiers (e.g., `5_sub‑01.csv`).
* **Contents:** Trial‑level records with participant choice, reaction times, task state variables, and feedback.

> The preprocessing scripts standardise variable names, remove practice trials, and output tidy data frames ready for analysis.

---

## 🔧 Code Overview

| File                     | Purpose                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `preprocess_raw_data.py` | Loads raw CSVs, performs cleaning, and exports `tidy_data.csv`.                                             |
| `analysis.ipynb`         | Reproduces all figures and stats reported in the paper (model fits, behavioural stats, parameter recovery). |

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

This project is licensed under the MIT License – see `LICENSE` for details.

---

## 📧 Contact

For questions, please contact **Paul B. Sharp** (paul.sharp@biu.ac.il) or open an issue on GitHub.
