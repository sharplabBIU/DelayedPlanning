"""
Follow-up to pct_halfsplit_decile.py, per Eran's v16 comments on R2.2:

1. OVERALL delayed-planning RT signature (mean over ALL within-goal trials,
   not just first half), top decile vs bottom 90%, with a between-group test
   ("Change these to the overall stats, not just first half").
2. ABSOLUTE first->second half change (H2-H1) per group, with bootstrap CIs
   and a between-group test of the absolute difference (Welch t + bootstrap),
   Studies 1 and 2 ("Add study 2/1 stats"; "If it is significant then we
   would need to rephrase").

Signature definition identical to pct_halfsplit_decile.py: per-subject,
per-trial mean log-RT at delayed_planning==1 minus ==0; halves = within-goal
trials 1-10 vs 11-20; groups = top decile by adaptively delayed control
(Fig 2C definition) vs remaining 90%.
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
    overall = sig.mean(axis=1)
    score = pd.read_csv(lfp).groupby('sub')['optimal_metacontrol_choice'].mean().reindex(subs)
    top = pd.Series(False, index=score.index)
    top[score.sort_values(ascending=False).index[:ntop]] = True
    rng = np.random.default_rng(11)
    print(f'=== {study} ===')
    grp = {}
    for name, mask in (('top decile', top), ('bottom 90%', ~top)):
        OV = overall[mask].dropna()
        H1, H2 = h1[mask].dropna(), h2[mask].dropna()
        common = H1.index.intersection(H2.index)
        AB = (H2[common]-H1[common])
        grp[name] = dict(OV=OV, AB=AB)
        bs = np.array([AB.values[rng.integers(0,len(AB),len(AB))].mean() for _ in range(10000)])
        lo, hi = np.percentile(bs,[2.5,97.5])
        t1, p1 = stats.ttest_1samp(AB, 0)
        print(f'  {name:11s} n={len(OV):3d}: OVERALL={OV.mean():+.3f} (SEM {OV.sem():.3f})  '
              f'H1={H1.mean():+.3f} H2={H2.mean():+.3f}  '
              f'ABS=+{AB.mean():.3f} [{lo:+.3f}, {hi:+.3f}] '
              f'(vs 0: t({len(AB)-1})={t1:.2f} p={p1:.3g})')
    # between-group: overall level
    tOV, pOV = stats.ttest_ind(grp['top decile']['OV'], grp['bottom 90%']['OV'], equal_var=False)
    # between-group: absolute change
    A, B = grp['top decile']['AB'], grp['bottom 90%']['AB']
    tAB, pAB = stats.ttest_ind(A, B, equal_var=False)
    bsd = np.array([A.values[rng.integers(0,len(A),len(A))].mean()
                    - B.values[rng.integers(0,len(B),len(B))].mean() for _ in range(10000)])
    lo, hi = np.percentile(bsd,[2.5,97.5])
    p_boot = 2*min(float(np.mean(bsd>=0)), float(np.mean(bsd<=0)))
    print(f'  OVERALL level top vs bottom: Welch t={tOV:.2f} p={pOV:.3g}')
    print(f'  ABS change  top vs bottom: diff={A.mean()-B.mean():+.3f} [{lo:+.3f}, {hi:+.3f}] '
          f'Welch t={tAB:.2f} p={pAB:.3g}  bootstrap two-sided p={p_boot:.3g}')
