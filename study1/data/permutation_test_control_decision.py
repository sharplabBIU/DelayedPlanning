"""Permutation test of adaptive control choices (Fig. 2B right; Results "one-sample ... p < 0.001" / caption "each p < 0.001").

Vectorised, seeded re-implementation of study2/permutation_test_control_decision.py with identical scoring:
for every participant, the three control responses of each planning trial are shuffled within the trial and then
each decision column is shuffled across trials (goal labels stay in place); a trial counts as optimally controlled
when, for a depth-3 goal (cat), control was taken at all three decisions; for a depth-2 goal (zebra), control was
relinquished at decision 1 and taken at decisions 2 and 3; for a depth-1 goal (lamp), relinquished at decisions
1 and 2 and taken at decision 3. Scores are summed over the first 60 planning trials and averaged over participants.

Run from a study's data/ folder:  python permutation_test_control_decision.py
Writes ../permutations_optimal_score.csv (1000 permutations; columns depth3_score, depth2_score, depth1_score),
../permutations_optimal_score_ACTUALSUBS.csv (unshuffled scores) and ../permutation_test_pvalues.csv.
"""
import os, numpy as np, pandas as pd
N_PERM, SEED = 1000, 20261007
decision_answers = ['plan1_response.keys', 'plan2_response.keys', 'plan3_response.keys']
accepted = ['left', 'right', 'space']
PERMS3 = np.array([[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])
rng = np.random.default_rng(SEED)

subs = sorted(x for x in os.listdir('.') if x.startswith('sub-') and x.endswith('.csv'))
data = []
for sub in subs:
    df = pd.read_csv(sub, low_memory=False)
    df = df[df['plan2_response.keys'].isin(accepted)].reset_index(drop=True)
    goals = df['r2'].astype(object).values
    R = df[decision_answers].astype(object).values
    valid = np.array([isinstance(g, str) and any(k in g for k in ('cat', 'zebra', 'lamp')) for g in goals])
    rows = np.flatnonzero(valid)[:60]                       # the first 60 planning trials (as in the original loop)
    kind = np.array([3 if 'cat' in goals[i] else 2 if 'zebra' in goals[i] else 1 for i in rows])
    data.append((R, rows, kind))

def score(R, rows, kind):
    sp = (R[rows] == 'space')                               # NaN responses count as "control taken", as in the original
    s3 = int(((~sp).all(axis=1) & (kind == 3)).sum())
    s2 = int((sp[:, 0] & ~sp[:, 1] & ~sp[:, 2] & (kind == 2)).sum())
    s1 = int((sp[:, 0] & sp[:, 1] & ~sp[:, 2] & (kind == 1)).sum())
    return s3, s2, s1

actual = np.array([score(R, rows, kind) for R, rows, kind in data]).sum(axis=0) / len(subs)
null = np.zeros((N_PERM, 3))
for p in range(N_PERM):
    tot = np.zeros(3)
    for R, rows, kind in data:
        n = len(R)
        Rp = R[np.arange(n)[:, None], PERMS3[rng.integers(0, 6, size=n)]]   # shuffle within each trial
        for j in range(3):                                                   # then shuffle each decision column across trials
            Rp[:, j] = Rp[rng.permutation(n), j]
        tot += score(Rp, rows, kind)
    null[p] = tot / len(subs)
cols = ['depth3_score', 'depth2_score', 'depth1_score']
pd.DataFrame(null, columns=cols).to_csv('../permutations_optimal_score.csv', index=False)
pd.DataFrame([actual], columns=cols).to_csv('../permutations_optimal_score_ACTUALSUBS.csv', index=False)
pv = [(null[:, k] >= actual[k]).mean() for k in range(3)]
pd.DataFrame({'depth': [3, 2, 1], 'actual_mean_optimal_trials': actual, 'null_mean': null.mean(0), 'null_max': null.max(0),
              'p_one_sided': pv, 'n_participants': len(subs), 'n_permutations': N_PERM}).to_csv('../permutation_test_pvalues.csv', index=False)
for k, d in enumerate([3, 2, 1]):
    print(f'depth {d}: actual = {actual[k]:.2f} optimal trials per participant; null mean = {null[:, k].mean():.2f}, max = {null[:, k].max():.2f}; p = {pv[k]:.3f} (n = {len(subs)})')
