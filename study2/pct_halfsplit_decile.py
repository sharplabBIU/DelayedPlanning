"""
Half-split of the ORIGINAL delayed-planning RT signature (all goals, incl.
depth 3; plain log-RT; delayed_planning==1 vs ==0 contrast), top decile of the
sample (by adaptively delayed control, as Fig 2C) vs bottom 90%.

Reports per group: first-half (trials 1-10) and second-half (11-20) means,
within-group paired t-tests, ABSOLUTE increase, and PERCENTAGE increase
relative to the group's own first-half level (group-level ratio; bootstrap CIs
over participants; bootstrap comparison of the two groups' percentages).
Source of the manuscript/response numbers: top decile +41% vs bottom 90% +218%
(Study 2, P=0.0004); +21% vs +486% (Study 1, unstable near-zero baseline).
"""
import numpy as np, pandas as pd
from scipy import stats

CFG = {'study2': ('preprocessed_data.csv','lmm_fixed.csv',18),
       'study1': ('../study1/preprocessed_data.csv','../study1/lmm_fixed.csv',9)}

for study,(pp,lfp,ntop) in CFG.items():
    d = pd.read_csv(pp).dropna(subset=['RT'])
    m = (d.groupby(['sub','trial_num_within_goal','delayed_planning'])['RT']
         .mean().unstack('delayed_planning'))
    sig = (m[1]-m[0]).unstack('trial_num_within_goal')
    subs = list(pd.unique(d['sub'])); sig = sig.reindex(subs)
    h1 = sig[[c for c in sig.columns if c<=10]].mean(axis=1)
    h2 = sig[[c for c in sig.columns if c>=11]].mean(axis=1)
    score = pd.read_csv(lfp).groupby('sub')['optimal_metacontrol_choice'].mean().reindex(subs)
    top = pd.Series(False, index=score.index)
    top[score.sort_values(ascending=False).index[:ntop]] = True
    rng = np.random.default_rng(11)
    print(f'=== {study} ===')
    pct_bs = {}
    for name, mask in (('top decile', top), ('bottom 90%', ~top)):
        H1, H2 = h1[mask].dropna(), h2[mask].dropna()
        t, p = stats.ttest_rel(H2, H1)
        pct = 100*(H2.mean()-H1.mean())/H1.mean()
        bs = []
        for _ in range(10000):
            i = rng.integers(0, len(H1), len(H1))
            m1 = H1.values[i].mean()
            if abs(m1) > 0.02:
                bs.append(100*(H2.values[i].mean()-m1)/m1)
        bs = np.array(bs); pct_bs[name] = bs
        lo, hi = np.percentile(bs,[2.5,97.5])
        print(f'  {name:11s} n={len(H1):3d}: H1={H1.mean():+.3f} H2={H2.mean():+.3f}  '
              f'abs=+{H2.mean()-H1.mean():.3f} (paired t({len(H1)-1})={t:.2f} p={p:.3g})  '
              f'pct={pct:+.0f}% [{lo:+.0f}%, {hi:+.0f}%]')
    nb = min(map(len, pct_bs.values()))
    dff = pct_bs['top decile'][:nb] - pct_bs['bottom 90%'][:nb]
    print(f'  P(top pct >= bottom pct) = {float(np.mean(dff >= 0)):.4f}')
