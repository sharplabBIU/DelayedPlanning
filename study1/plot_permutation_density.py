"""Fig. 2B (right): permutation-test null distributions of the proportion of optimally timed control choices,
per required planning depth, with the observed proportions as dashed lines.

Reads  permutations_optimal_score.csv            (null: 1,000 shuffled datasets; written by data/permutation_test_control_decision.py)
       permutations_optimal_score_ACTUALSUBS.csv (observed scores, same scoring)
Writes permtest.png

Scores are mean numbers of optimally timed trials per participant out of the 20 trials of each goal, so score/20 is
the proportion of the optimal control policy. This is the plotting cell of permutationTest_notebook.ipynb as a script
(that notebook's first cell re-implements the permutation on the raw, identifiable files and is superseded by
data/permutation_test_control_decision.py). Run from study1/.
"""
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sns.set(style='white', palette='mako', font_scale=2.0, rc=None)

observed = pd.read_csv('permutations_optimal_score_ACTUALSUBS.csv').iloc[0]
null = pd.read_csv('permutations_optimal_score.csv')
null = pd.melt(null, var_name='planning_depth', value_name='score')
null['planning_depth'] = null['planning_depth'].str.replace('_score', '')
null['percent_score'] = null['score'] / 20.0

# Set2: depth 1 green, depth 2 orange, depth 3 blue (the Fig. 2 legend)
set2 = sns.color_palette('Set2', 3)
palette = {'depth1': set2[0], 'depth2': set2[1], 'depth3': set2[2]}

plt.figure(figsize=(5, 3))
sns.kdeplot(data=null, x='percent_score', hue='planning_depth', hue_order=['depth3', 'depth2', 'depth1'],
            fill=True, palette=palette, legend=False)
for depth in ['depth3', 'depth2', 'depth1']:
    plt.axvline(x=observed[f'{depth}_score'] / 20.0, color=palette[depth], linewidth=2.5, linestyle='--')
plt.xlabel('% optimal control policy')
plt.ylabel('density')
plt.savefig('permtest.png', dpi=300, bbox_inches='tight')
print('saved permtest.png; observed proportions:',
      {d: round(observed[f'{d}_score'] / 20.0, 3) for d in ['depth1', 'depth2', 'depth3']})
