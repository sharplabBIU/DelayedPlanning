import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import sem
import itertools

# Increase text size
sns.set_context("talk", font_scale=2.8)

# Additional Code for Plotting
critical_values = {'depth=1': np.log(15), 'depth=2': np.log(19.59), 'depth=3': np.log(41.72)}
print(critical_values)

# Convert the results to a DataFrame for plotting
results_df = pd.read_csv('permutations_optimal_score.csv')
results_df = pd.melt(results_df, var_name='planning_depth', value_name='score')
results_df['ln(score)'] = np.log(results_df['score'])

# Define custom palette colors for each depth
custom_palette = {
    'depth1_score': sns.color_palette("Set2")[2],  # Green
    'depth2_score': sns.color_palette("Set2")[1],  # Orange
    'depth3_score': sns.color_palette("Set2")[0]   # Blue
}

# Plot the distributions on the same graph
plt.figure(figsize=(14, 6))

# Plot depth 1
sns.histplot(results_df[results_df['planning_depth'] == 'depth1_score'], x='ln(score)', kde=True, color=custom_palette['depth1_score'], label='Depth 1')
plt.axvline(x=critical_values['depth=1'], color=custom_palette['depth1_score'], linestyle='--', linewidth=4.5)

# Plot depth 2
sns.histplot(results_df[results_df['planning_depth'] == 'depth2_score'], x='ln(score)', kde=True, color=custom_palette['depth2_score'], label='Depth 2')
plt.axvline(x=critical_values['depth=2'], color=custom_palette['depth2_score'], linestyle='--', linewidth=4.5)

# Plot depth 3
sns.histplot(results_df[results_df['planning_depth'] == 'depth3_score'], x='ln(score)', kde=True, color=custom_palette['depth3_score'], label='Depth 3')
plt.axvline(x=critical_values['depth=3'], color=custom_palette['depth3_score'], linestyle='--', linewidth=4.5)

plt.xlabel("ln(score)")
plt.ylabel("Count")
plt.legend(title='Planning Depth', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.savefig('permTest_Visualized.png', dpi=300, bbox_inches='tight')

plt.show()
