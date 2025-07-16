import pandas as pd
import os
import csv
import math
import shutil

# --------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------
quiz1_answers = 'answer_quiz1_3.corr'
quiz2_answers = 'answer_quiz1_5.corr'
im_col_unused  = 'ans3'               # still referenced by legacy comments
good_cutoff    = 0.80                 # ≥80 % → “good” subject
n_questions    = 16                   # denominator for the percentage
parent_dir     = os.pardir            # one level up ("..")

# current working directory is assumed to contain the raw subject files
subs = [x for x in os.listdir('.') if x.startswith(('5', '6'))]

csv_lines = [['sub', 'percent_correct']]
bad_memory_dir = 'bad_memory'         # still produced for the “bad” list
skipped_dir='skipped_subs'

for sub in subs:
    quiz_score   = 0
    quiz_counter = 0

    df = pd.read_csv(sub)

    # --------------------------------------------------------------
    # SCORING LOOP
    # --------------------------------------------------------------
    for row in range(len(df)):
        if not math.isnan(df[quiz2_answers][row]):
            quiz_counter += 1
            if 15 < quiz_counter < 24:          # preserve original bounds
                if df[quiz1_answers][row] == 1:
                    quiz_score += 1
                    if df[quiz2_answers][row] == 1:
                        quiz_score += 1

    pct_correct = quiz_score / float(n_questions)

    # --------------------------------------------------------------
    # ROUTE THE FILES
    # --------------------------------------------------------------
    if pct_correct >= good_cutoff:
        dest_path = os.path.join(parent_dir, sub)   # “…/sub”
        # move only if that name doesn’t already exist in the parent dir
        if not os.path.exists(dest_path):
            print(f'moved GOOD sub → {dest_path}  ({pct_correct:.1%})')
        else:
            print(f'skipped {sub}: {dest_path} already exists')
    else:
        csv_lines.append([sub, pct_correct])

# --------------------------------------------------------------------
# WRITE SUMMARY CSV
# --------------------------------------------------------------------
with open('memory_accuracies_subjects_orig_fulltrajectories.csv', 'w',
          newline='') as f:
    csv.writer(f).writerows(csv_lines)
