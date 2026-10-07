# Task materials (`study2/task/`)

Complete implementation of the delayed-planning task used in both studies, as deployed online
(Pavlovia/PsychoJS; recruitment via Prolific). The experiment was built in **PsychoPy Builder** and
exported to **PsychoJS 2023.2.3** (the version recorded in every Study 2 data file; Study 1 used the
2021.1.3 export of the same experiment — see "Study 1 vs Study 2" below).

| File | What it is |
|---|---|
| `thisExp.psyexp` | PsychoPy Builder experiment file (source of everything below; last saved with PsychoPy 2024.2.4). Open with PsychoPy to inspect every routine, all on-screen instruction texts, timing and response settings. |
| `thisExp.js`, `thisExp-legacy-browsers.js`, `index.html` | The PsychoJS (JavaScript) export that participants ran in the browser. `index.html` loads `lib/psychojs-2023.2.3.*` from the Pavlovia CDN. |
| `thisExp.py`, `thisExp_lastrun.py` | Python export of the same experiment (runs locally in PsychoPy). |
| `images/` | All stimuli: the eight state pictures of the decision tree (`baby`, `backpack`, `bowtie`, `car`, `cat`, `knight`, `lamp`, `toothbrush`, `zebra`, …), the start-state and goal icons, instruction graphics (`decision_tree*.png`), and the Python scripts that drew the instruction graphics (`plot_*.py`, which use `networkx`). |
| `consent1.png`, `consent2.png` | The informed-consent form shown before the task (Hebrew University of Jerusalem ethics approval 2021-11282). |
| `image_train_press.xlsx`, `try_game.xlsx`, `stage2_4_practice.csv` | Condition files for the practice/instruction trials of the training phase. |
| `forgetting1.xlsx`, `quiz_1.xlsx` | Condition files for the memory quizzes administered during training (one-step transition quiz every 40 trials; full-route quiz every 80 trials). |
| `planning_trials.xlsx` | Condition file for the 60 planning-phase trials (20 per instructed goal / required planning depth). |
| `SBPQ.xlsx`, `moment_emotion_questionnaire_updated.csv` | Momentary mood/stress rating items ("Rate how you feel at this moment": dissatisfied, alert, depressed, sad, active, impatient, annoyed, angry, irritated, grouchy), administered in Study 2 (collected, not analysed in the paper). |
| (in `thisExp.psyexp`) | The 16-item Penn State Worry Questionnaire (PSWQ; both studies) and the Schizotypal Personality Questionnaire–Brief (SPQ-B; Study 2) are implemented as form routines inside the experiment file. |
| `apple.png`, `basket.png`, `fireworks.png`, `planet.png`, `tree.png` | Feedback/instruction graphics used by the experiment. |
| `Book1.xlsx`, `forgetting2.xlsx`, `image_train_press1trial.xlsx`, `quiz_2_revised.xlsx`, `replanning_trials.xlsx` | Development files that are **not referenced** by the final experiment (kept for completeness). |

## Procedure in brief (see the manuscript Methods for details)

1. Consent (`consent1.png`, `consent2.png`) and instructions.
2. **Training phase** (240 trials): participants learn the deterministic three-step decision tree by starting
   at a random state, pressing the instructed key (← / →) and seeing the successor state for 1000 ms.
   Every 40 trials a one-step transition quiz, every 80 trials a full-route quiz (4-alternative forced choice).
   Study 2 additionally displayed feedback on quiz answers.
3. **Planning phase** (60 trials): the instructed goal picture is shown at the top of the screen; at each of
   three decision steps participants either choose an action themselves ("Plan myself") or relinquish control
   ("Let computer choose", +100 points immediately). Reaching the goal yields 400 points.
4. Questionnaires (PSWQ in both studies; momentary stress items and SPQ-B in Study 2) and debriefing.

## Study 1 vs Study 2

The archived files are the **Study 2 build**. Study 1 used the same experiment exported with PsychoPy
2021.1.3; it differed only in (i) not showing feedback on the training quizzes and (ii) not including the
Study 2 questionnaires (momentary stress items, SPQ-B). The reward magnitudes (400 goal / 100 relinquish),
the decision tree, the stimuli and the trial structure were identical.

## Running the task

* Online: upload the folder to a Pavlovia project (or any static web server) and open `index.html`;
  participant and session identifiers are passed as URL parameters (`participant`, `PROLIFIC_PID`,
  `STUDY_ID`, `SESSION_ID`), which is why these columns appear in the raw data (anonymised in this archive).
* Locally: open `thisExp.psyexp` in PsychoPy (≥ 2023.2) and press Run, or run `python thisExp_lastrun.py`
  from this folder with the `psychopy` package installed.

The task code refers to a Prolific completion URL in `thisExp.js`; the completion code is study-specific and
no longer active.
