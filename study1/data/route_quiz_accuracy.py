"""Final route-quiz accuracy for every participant (Results, "Initial study": mean and mode of accuracy).

Uses exactly the scoring rule of correct_quizzes.py (which only records participants who FAILED the
cutoff while moving them to bad_memory/): over the last full-route quiz (8 routes x 2 steps = 16 answers),
a step counts as correct if the first-step answer is correct (and the second step only if the first was).
Run from a study's data/ folder:  python route_quiz_accuracy.py
Writes route_quiz_accuracy_all.csv (sub, percent_correct, included) and prints the summary statistics
for the included participants (files in this folder) and for the excluded ones (bad_memory/).
"""
import os, math, csv
import pandas as pd
quiz1_answers, quiz2_answers, n_questions = 'answer_quiz1_3.corr', 'answer_quiz1_5.corr', 16

def score(path):
    df = pd.read_csv(path, low_memory=False)
    if quiz2_answers not in df.columns: return float('nan')
    quiz_score = quiz_counter = 0
    for row in range(len(df)):
        if not math.isnan(df[quiz2_answers][row]):
            quiz_counter += 1
            if 15 < quiz_counter < 24:
                if df[quiz1_answers][row] == 1:
                    quiz_score += 1
                    if df[quiz2_answers][row] == 1:
                        quiz_score += 1
    return quiz_score / float(n_questions)

rows = []
for folder, included in [('.', 1), ('bad_memory', 0)]:
    if not os.path.isdir(folder): continue
    for f in sorted(x for x in os.listdir(folder) if x.startswith('sub-') and x.endswith('.csv')):
        rows.append({'sub': f, 'percent_correct': score(os.path.join(folder, f)), 'included': included})
out = pd.DataFrame(rows)
out.to_csv('route_quiz_accuracy_all.csv', index=False)
inc = out[(out.included == 1)].dropna()
print(f'included participants: n = {len(inc)}, mean = {inc.percent_correct.mean()*100:.1f}%, median = {inc.percent_correct.median()*100:.1f}%, mode = {inc.percent_correct.mode().iloc[0]*100:.0f}%, min = {inc.percent_correct.min()*100:.1f}%')
exc = out[(out.included == 0)].dropna()
if len(exc): print(f'excluded (bad_memory): n = {len(exc)}, mean = {exc.percent_correct.mean()*100:.1f}%, max = {exc.percent_correct.max()*100:.1f}%')
