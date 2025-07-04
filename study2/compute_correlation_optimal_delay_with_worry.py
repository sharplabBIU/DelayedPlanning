import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr as corrp
from statsmodels.othermod.betareg import BetaModel
import statsmodels.api as sm

# Load the dataset
optimally_delayed_csv = 'optimal_delayed_scores.csv'
df = pd.read_csv(optimally_delayed_csv)
df=df.dropna()
# Transform the 'optimal_delayed_score' values
opt_scores = df['optimal_delayed_score'].values
opt_scored_transformed = [x + 0.0001 if x==0 else x-0.001 if x==1 else x for x in opt_scores]
print(np.min(opt_scored_transformed))
print(np.max(opt_scored_transformed))

# Prepare the predictors by adding a constant (for the intercept) and the independent variables
X = df[['worry']]
X = sm.add_constant(X)

# Define the dependent variable
y = opt_scored_transformed

# Fit the regression model
model = BetaModel(y, X).fit()

# Display the summary of the regression model
print(model.summary())

# Calculate the Spearman correlation
r, p = corrp(df['percent_correct'], df['optimal_delayed_score'])
print('correl percent correct memory and optimal delayed score: {}, pval:{}'.format(r, p))

# Create the seaborn regression plot with jitter
plt.figure(figsize=(10, 6))
sns.regplot(x='percent_correct', y='optimal_delayed_score',x_jitter=0.0, data=df, scatter=True, color='blue')
plt.xlabel('memory score')
plt.ylabel('optimallly delayed control')
plt.savefig('memory_optDelay_relationship.png',dpi=300)
plt.show()
