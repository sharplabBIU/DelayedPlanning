import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set Seaborn style
sns.set(style='white', font_scale=2.5, palette='Set2')

# 1. Load the BIC dictionary from pickle
# Load your dict

models_BICs_record = {'MBMC_optimal': np.float64(26984.05491280084), 'MBMC_Depth': np.float64(25180.54011043868), 
                      'MBMC_Breadth1_Depth': np.float64(24667.34493574834), 
                      'MBMC_Breadth2_Depth': np.float64(15837.933909123849), 'MBMC_Breadth2_Depth_CC': np.float64(13572.64694328037), 
                      'MBMC_Breadth2_Depth_CCR': np.float64(13334.645848139357), 'MBMC_Breadth2_Depth_CCRF': np.float64(12322.586894605158), 'MBMC_Breadth2_Depth_CCRF_CB': np.float64(12057.490946332953), 
                      'MBMCF_Breadth2_Depth_CCRF_CB': np.float64(12149.95380454981), 'MBMCsequential_Breadth2_Depth_CCRF_CB': np.float64(12080.269159028569), 'MBMC_Breadth2_Depth_MF': np.float64(12790.254026570794), 
                      'CCRF_CB': np.float64(26058.399485907583),
                       'CCRF': np.float64(26714.563278686648), 
                       'CB': np.float64(26003.598437929715), 
                       'MBMCreplace_Breadth2_Depth_CCRF_CB_CP': np.float64(11392.973160951411),
                         'MBMC_Breadth2_Depth_CCRF_CB_CP': np.float64(11380.859559289484)}


# # Rename keys in-place
# for old_key in list(models_BICs_record.keys()):

#     if 'Forget' in old_key:
#         print(old_key)
#         new_key = old_key.replace('PE', 'CP')
#         # pop the old entry and assign it under the new key
#         models_BICs_record[new_key] = models_BICs_record.pop(old_key)

# (Optional) If you want to overwrite the file with the updated dict:
with open('model_BICs_final.pkl', 'wb') as f:
    pickle.dump(models_BICs_record, f)
# 2. Convert to DataFrame
df_bic = pd.DataFrame({
    'Model': list(models_BICs_record.keys()),
    'BIC':   list(models_BICs_record.values())
})
df_bic.to_csv('BICs.csv')
min_bic = df_bic['BIC'].min()
df_bic['Delta_BIC'] = df_bic['BIC'] - min_bic
# 3. Compute Delta-BIC relative to the best (min) BIC
from itertools import combinations
import pandas as pd

# df_bic already loaded and contains columns:  'Model'  and  'BIC'
# -----------------------------------------------------------------

records = []
for (_, row_i), (_, row_j) in combinations(df_bic.iterrows(), 2):
    if row_i['BIC'] == row_j['BIC']:
        continue                    # ignore ties (ΔBIC = 0)
    # ensure “larger – smaller” order
    larger, smaller = (row_i, row_j) if row_i['BIC'] > row_j['BIC'] else (row_j, row_i)

    records.append({
        'Delta_BIC' : larger['BIC'] - smaller['BIC'],
        'Larger_BIC': larger['Model'],   # model with the higher BIC
        'Smaller_BIC': smaller['Model']  # model with the lower BIC
    })

df_delta = pd.DataFrame(records).sort_values('Delta_BIC', ascending=False)

df_delta.to_csv('delta-BICs.csv', index=False)


# 4. Sort for plotting
df_bic_sorted = df_bic.sort_values('Delta_BIC')

# 5. Plot with Seaborn
plt.figure(figsize=(10, 7.5))
ax = sns.barplot(
    x='Delta_BIC',
    y='Model',
    data=df_bic_sorted,
    dodge=False,
    color='black'
)
ax.tick_params(axis='y', labelsize=20)  # adjust labelsize if needed
ax.axvline(0, color='k', linewidth=0.8)
ax.set_xlabel(r'$\Delta_{BIC}$')
ax.set_ylabel('')
plt.title('Model Comparison',fontsize=22)
plt.tight_layout()
plt.savefig('model_comparison_figure_final.png', dpi=300,bbox_inches='tight')
plt.show()
