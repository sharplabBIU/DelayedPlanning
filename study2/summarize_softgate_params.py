"""
Summarize the soft-gated MBMC EM fits (per-participant posterior means, native
space) into the median/IQR tables reported as Supplemental Tables S3 (Study 1)
and S4 (Study 2), and the mean/SEM values shown in Supplemental Figure S7.

Inputs : em_params_study{1,2}_MBMCgatedsoft.npy  (n_subjects x 9)
Outputs: em_params_study{1,2}_median_iqr.csv
"""
import numpy as np
import pandas as pd

PARAMS = ['MB_B', 'MB_depth', 'MB_breadth', 'breadth2', 'mbcache',
          'CB', 'forget', 'cache_reward', 'cache_plan']
SYMBOLS = ['beta_MBMC', 'gamma_d', 'b1_tilde', 'b2_tilde', 'kappa_C',
           'beta_CB', 'gamma_C', 'kappa_R', 'omega_P']

for st in ('study1', 'study2'):
    R = np.load(f'em_params_{st}_MBMCgatedsoft.npy')
    out = pd.DataFrame({
        'parameter': PARAMS,
        'symbol': SYMBOLS,
        'n': R.shape[0],
        'mean': R.mean(0).round(4),
        'sem': (R.std(0, ddof=1) / np.sqrt(R.shape[0])).round(4),
        'median': np.median(R, 0).round(4),
        'Q1': np.percentile(R, 25, 0).round(4),
        'Q3': np.percentile(R, 75, 0).round(4),
    })
    out.to_csv(f'em_params_{st}_median_iqr.csv', index=False)
    print(f'{st}: n={R.shape[0]}  medians={np.median(R,0).round(3).tolist()}')
print('Saved em_params_study{1,2}_median_iqr.csv (soft-gated fits; Supp Tables S3-S4, Fig S7)')
