"""Build lmm_fixed.csv (the trial-level design matrix used by the RT linear mixed model,
the computational-model fits, and the behavioural analyses) from preprocessed_data.csv.

This script reproduces, verbatim, the column-construction code from the first cell of
analysis.ipynb (which originally wrote lmm_fixed.csv), so that the full pipeline
raw data -> data/preprocess_raw_data.py -> preprocessed_data.csv -> make_lmm_fixed.py -> lmm_fixed.csv
can be re-run from scratch. Run from this study folder:  python make_lmm_fixed.py
Column definitions are documented in ../data_dictionary.md.
"""
import pandas as pd
import numpy as np

df=pd.read_csv('preprocessed_data.csv')
df['choice_numeric'] = [1 if choice == 'space' else 0 for choice in df['choices']]
df['choices_numeric'] = [0 if choice == 'left' else 1 if choice=='right' else 2 for choice in df['choices']]

# Step 1: Filter df where planning_depth == 3 and decision == 1
filtered_df = df[(df['planning_depth'] == 3)]
# Step 2: Group by 'sub' and count the number of 1s in 'choice_numeric'
counts = filtered_df.groupby('sub')['choice_numeric'].apply(lambda x: (x == 1).sum())

# Step 3: Identify subjects with more than 15 1s
subjects_to_exclude = counts[counts > 60].index

# Step 4: Exclude these subjects from df
df = df[~df['sub'].isin(subjects_to_exclude)]


# Initially, create the 'choice_numeric_last' column by shifting 'choice_numeric'
# Sort the DataFrame by subject_id, planning_depth, trial_id, and decision
df_sorted = df.sort_values(by=['sub', 'planning_depth','trial_num_within_goal', 'decision'])

# Group by subject_id, planning_depth, and decision, then shift the choice_numeric column to get the previous trial's choice
df['choice_numeric_last'] = df_sorted.groupby(['sub', 'planning_depth', 'decision'])['choice_numeric'].shift(1)

# Now, identify the first trial within each planning depth for each subject
# To do this, we can use a combination of groupby and transform to mark the first trial's rows
df['is_first_trial'] = df.groupby(['sub', 'planning_depth'])['trial_num'].transform(lambda x: x == x.min())

# Set 'choice_numeric_last' to 0 for all decisions within the first trial of each planning depth
df.loc[df['is_first_trial'] == True, 'choice_numeric_last'] = 0

# Drop the helper column 'is_first_trial' if it's no longer needed
df.drop(columns=['is_first_trial'], inplace=True)

# Ensure there are no NaN values in 'choice_numeric_last'; fill with 0 if any (should be redundant by now)
# Fill NaN values with 0, as these represent the first trial of each goal within each subject
print(df['choice_numeric_last'].value_counts())

df['choice_numeric_last'] = df['choice_numeric_last'].fillna(0)

df['interaction_won_and_metachoice'] = [
    1 if got_to_goal_last == 1 and choice_numeric_last == 1 
    else -1 if got_to_goal_last == 0 and choice_numeric_last == 1 
    else 0 if got_to_goal_last == 0 and choice_numeric_last == 0 
    else 0 if got_to_goal_last == 1 and choice_numeric_last == 0 
    else 0
    for got_to_goal_last, choice_numeric_last in zip(df['got_to_goal_last'], df['choice_numeric_last'])
]

df['got_to_goal_retrieved_cached'] = [
    'Won_Cached' if got_to_goal == 1 and retrieved_cached == 1 
    else 'Lost_Cached' if got_to_goal == 0 and retrieved_cached == 1 
    else 'Won_Novel' if got_to_goal == 0 and retrieved_cached == 0 
    else 'Lost_Novel' if got_to_goal == 1 and retrieved_cached == 0 
    else 0
    for got_to_goal, retrieved_cached in zip(df['got_to_goal'], df['retrieved_cached'])
]

# This solution takes into account the structure of your data, where each subject can have multiple goals
# defined by 'planning_depth', and each goal consists of 20 trials defined by 'trial_num_within_goal'.
# By grouping by both 'subject' and 'planning_depth', the 'choice_numeric_last' column is correctly calculated
# within the context of each goal, ensuring the integrity of the sequence for each goal within each subject.

# Fill NaN values (which will be present for the first trial of each subject) with 0

# This approach 
df=df.reset_index(drop=True)
print(len(df['sub'].unique()))




def calculate_optimal_metacontrol_choice(row):
    if row['planning_depth'] == 3:
        return 1 if row['choice_numeric'] == 0 else 0
    elif row['planning_depth'] == 2:
        if row['decision'] == 1:
            return 1 if row['choice_numeric'] == 1 else 0
        elif row['decision'] in [2, 3]:
            return 1 if row['choice_numeric'] == 0 else 0
        else:
            return 0
    elif row['planning_depth'] == 1:
        if row['decision'] in [1, 2]:
            return 1 if row['choice_numeric'] == 1 else 0
        elif row['decision'] == 3:
            return 1 if row['choice_numeric'] == 0 else 0
        else:
            return 0
    else:
        return 0


def create_optimal_mc(row): #points at which you should relinquish control
    if row['planning_depth'] == 3:
        return 0
    elif row['planning_depth'] == 2:
        if row['decision'] == 1:
            return 1
        elif row['decision'] in [2, 3]:
            return 1 if row['choice_numeric'] == 0 else 0
        else:
            return 0
    elif row['planning_depth'] == 1:
        if row['decision'] in [1, 2]:
            return 1 if row['choice_numeric'] == 1 else 0
        elif row['decision'] == 3:
            return 1 if row['choice_numeric'] == 0 else 0
        else:
            return 0
    else:
        return 0

def create_overcontrol(row): #points at which you should relinquish control
    if row['planning_depth'] == 3:
        if row['optimal_metacontrol_choice']==0:
            return 0
        else:
            return 0
    elif row['planning_depth'] == 2:
        if row['decision'] == 1:
            if row['optimal_metacontrol_choice']==0:
                return 1
            else:
                return -1
        elif row['decision'] in [2, 3]:
            if row['optimal_metacontrol_choice']==0:
                return 0
            else:
                return 0
        
    elif row['planning_depth'] == 1:
        if row['decision'] in [1, 2]:
            if row['optimal_metacontrol_choice']==0:
                return 1
            else:
                return -1
        elif row['decision'] == 3:
            if row['optimal_metacontrol_choice']==0:
                return 0
            else:
                return 0

# Initialize the dictionary
correct_MB_choices = {}

# Assuming df['current_state'] exists and represents the state at the time of making the decision
# Filter the DataFrame for rows where got_to_goal == 1
got_to_goal_df = df[df['got_to_goal'] == 1]

# Populate the dictionary with (planning_depth, decision, current_state) as keys
for _, row in got_to_goal_df.iterrows():
    key = (row['planning_depth'], row['decision'], row['current_state'])
    value = row['choices_numeric']
    # Ensure each key is unique to maintain consistency
    if key not in correct_MB_choices:
        correct_MB_choices[key] = value

def create_MB_decision(row):
    """
    Assigns a value to MB_decision based on the specified logic and the correct_MB_choices dictionary,
    now considering the triplet combination of planning_depth, decision, and current_state.
    
    Parameters:
    - row: a row from the DataFrame.
    
    Returns:
    - The value for MB_decision for the row.
    """
    # Direct conditions
    if row['planning_depth'] == 2 and row['decision'] == 1:
        return 2
    elif row['planning_depth'] == 1 and row['decision'] in [1, 2]:
        return 2
    else:
        # Reference the dictionary with the triplet key
        key = (row['planning_depth'], row['decision'], row['current_state'])
        return correct_MB_choices.get(key, -10)

# Apply the function to each row of the DataFrame
df['MB_decision'] = df.apply(create_MB_decision, axis=1)

    

def create_overplanning(row): #points at which you should relinquish control
    if row['planning_depth'] == 3:
        if row['decision']>1:
            return 1
        else:
            return 0
    elif row['planning_depth'] == 2:
        if row['decision'] == 3:
            return 1
        else:
            return 0
    elif row['planning_depth'] == 1:
        return 0
    else:
        return 0
sd_RT=df['RT'].std()
mean_RT=df['RT'].mean()





# Apply the function to each row
df['optimal_metacontrol_choice'] = df.apply(calculate_optimal_metacontrol_choice, axis=1)
# df['optimal_metacontrol_choice_accurate'] = df.apply(calculate_optimal_metacontrol_choice_accounting_for_accuracy, axis=1)

df['over_planning'] = df.apply(create_overplanning, axis=1)
df['over_control'] = df.apply(create_overcontrol, axis=1)

df['optimal_metacontrol_choice_last'] = df.groupby(['sub', 'planning_depth'])['optimal_metacontrol_choice'].shift()

# Now, identify the first trial within each planning depth for each subject
# To do this, we can use a combination of groupby and transform to mark the first trial's rows
df['is_first_trial'] = df.groupby(['sub', 'planning_depth'])['trial_num'].transform(lambda x: x == x.min())

# Set 'choice_numeric_last' to 0 for all decisions within the first trial of each planning depth
df.loc[df['is_first_trial'] == True, 'optimal_metacontrol_choice_last'] = 0

# Drop the helper column 'is_first_trial' if it's no longer needed
df.drop(columns=['is_first_trial'], inplace=True)
# df.drop(columns=['choices'], inplace=True)

# Ensure there are no NaN values in 'choice_numeric_last'; fill with 0 if any (should be redundant by now)
# Fill NaN values with 0, as these represent the first trial of each goal within each subject
df['optimal_metacontrol_choice_last'] = df['optimal_metacontrol_choice_last'].fillna(0)

# Adjusted Step 1: Calculate points from numeric_choice directly, with modification for non-goal-achieving actions
df['points_from_choice'] = df.apply(lambda row: -100 if row['choice_numeric'] == 1 and not row['got_to_goal'] else row['choice_numeric'] * 100, axis=1)

# Step 2: For each trial, determine if got_to_goal was achieved at least once
# This remains unchanged as it correctly calculates points from achieving goals
got_to_goal_per_trial = df.groupby(['sub', 'trial_num'])['got_to_goal'].max().reset_index()
got_to_goal_per_trial['points_from_goal'] = got_to_goal_per_trial['got_to_goal'] * 400
# Merge this back with the original df to associate points_from_goal with each decision
df = df.merge(got_to_goal_per_trial[['sub', 'trial_num', 'points_from_goal']], on=['sub', 'trial_num'], how='left')

# Now, calculate trial_points by summing points_from_choice and points_from_goal for each trial
# This step remains unchanged as it depends on the updated calculation from Step 1
df['trial_points'] = df.groupby(['sub', 'trial_num'])['points_from_choice'].transform('sum') + df['points_from_goal']

# Step 3: Calculate total_points for each subject by summing trial_points
# This step remains unchanged as it correctly sums up the trial points to calculate total points per subject
total_points_per_subject = df.groupby(['sub'])['trial_points'].sum().reset_index(name='total_points')

# If needed, merge total_points back to the original df
# This step ensures each participant's total points are reflected in the original dataframe
df = df.merge(total_points_per_subject[['sub', 'total_points']], on='sub', how='left')

#correct control actions

#transition structure deterministic where red is right, and blue is left



# Deterministic transition structure
deterministic_transitions = {
    ('start', 'red'): 'toothbrush',
    ('start', 'blue'): 'baby',
    ('baby', 'red'): 'bowtie',
    ('baby', 'blue'): 'backpack',
    ('toothbrush', 'red'): 'backpack',
    ('toothbrush', 'blue'): 'car',
    ('backpack', 'blue'): 'zebra',
    ('backpack', 'red'): 'lamp',
    ('bowtie', 'blue'): 'lamp',
    ('bowtie', 'red'): 'knight',
    ('car', 'blue'): 'cat',
    ('car', 'red'): 'lamp'
}
# Recursive helper function to find future states
def find_future_states(state, transitions, visited=None):
    if visited is None:
        visited = set()
    if state in visited:
        return set()
    visited.add(state)
    next_states = {transitions[s] for s in transitions if s[0] == state}
    all_future_states = set(next_states)
    for ns in next_states:
        all_future_states.update(find_future_states(ns, transitions, visited))
    return all_future_states



# To respect the original order of the DataFrame (grouped by decision across all trials),
# we need to build the results array in the same row order as the original DataFrame.

# First, save the original order using an index column
df['original_index'] = df.index

# Recompute correct_control_action values based on trial groupings
correct_action_values = []

# Create a temporary column for correct values, to merge back in order later
temp_df = pd.DataFrame(columns=['original_index', 'correct_control_action'])

for (sub, trial_num), group in df.groupby(['sub', 'trial_num']):
    goal = group['planning_depth'].iloc[0]
    gtg = group['got_to_goal'].iloc[0]
    goal_map = {3: 'cat', 2: 'zebra', 1: 'lamp'}
    critical_decisions_map = {3: 0, 2: 1, 1: 2}
    target_goal = goal_map[goal]
    critical_decision_threshold=critical_decisions_map[goal]
    state = 'start'

    correct_choices = 0
    control_choices = 0

    for _, row in group.sort_values('decision').iterrows():
        
        state = row['current_state']
        if state != 'start':
            state = state[7:-4]
        decision=row['decision']
        # print(decision)

        choice = row['choices']
        if decision>critical_decision_threshold:
            if choice != 'space':
                control_choices += 1
                choice_direction = 'red' if choice == 'right' else 'blue'
                correct_state = deterministic_transitions.get((state, choice_direction))
                if decision==3:
                    if gtg:
                        correct_choices+=1
                else:
                    
                    if target_goal in find_future_states(correct_state, deterministic_transitions):
                        correct_choices+=1
    percent_correct = np.nan if control_choices == 0 else correct_choices/control_choices
   

    for idx in group.index:
        temp_df.loc[len(temp_df)] = [idx, percent_correct]

# Sort the result to match the original order
temp_df = temp_df.sort_values('original_index')
df = df.sort_values('original_index').drop(columns=['original_index'])

# Merge correct values into main df
df['correct_control_action'] = temp_df['correct_control_action'].values
print(df['correct_control_action'])


# Add space_hit_points: 1 point for each space hit (choice_numeric == 1)
df['space_hit_points'] = df['choice_numeric']

# Add goal_points: 4 points if the goal was reached in that trial
goal_points_df = df.groupby(['sub', 'trial_num'])['got_to_goal'].max().reset_index()
goal_points_df['goal_points'] = goal_points_df['got_to_goal'] * 4
df = df.merge(goal_points_df[['sub', 'trial_num', 'goal_points']], on=['sub', 'trial_num'], how='left')

# Sum points per trial
trial_score_df = df.groupby(['sub', 'trial_num'])[['space_hit_points']].sum().reset_index()
df = df.merge(trial_score_df, on=['sub', 'trial_num'], suffixes=('', '_total'))

# Calculate total_score per trial
df['total_score'] = df['goal_points'] + df['space_hit_points_total']

# Final function: compares actual choice (choice_numeric) to optimal meta-control policy
def evaluate_metacontrol_accuracy(row):
    goal_map = {3: 'cat', 2: 'zebra', 1: 'lamp'}
    goal = goal_map.get(row['planning_depth'], None)

    if goal is None:
        return 0

    decision = row['decision']
    depth = row['planning_depth']
    actual_choice = row['choice_numeric']  # 0 = take control, 1 = give up

    # Rule-based optimal meta-control
    if (depth == 2 and decision == 1) or (depth == 1 and decision in [1, 2]):
        optimal_choice = 1
    else:
        state = row['current_state']
        if state != 'start':
            state = state[7:-4]  # Strip 'images/' and '.png'

        reachable_states = find_future_states(state, deterministic_transitions)

        if goal not in reachable_states and goal != state:
            optimal_choice = 1  # Give up control
        else:
            optimal_choice = 0  # Take control

    return 1 if actual_choice == optimal_choice else 0

# Apply to DataFrame
df['metacontrol_accuracy'] = df.apply(evaluate_metacontrol_accuracy, axis=1)

# Apply correctness calculation to df
print(df.correct_control_action.value_counts())


# df['correct_control_action']= [
#     1 if got_to_goal_last == 1 and choice_numeric_last == 0 
#     else 0 if got_to_goal_last == 0 and choice_numeric_last == 0 
#     else 0
#     for got_to_goal_last, choice_numeric_last in zip(df['got_to_goal'], df['choice_numeric'])
# ]

# #save df



# ---------------------------------------------------------------------------
# Output. By default the regenerated matrix is written to lmm_fixed_regenerated.csv and
# compared with the shipped lmm_fixed.csv (which the stored posterior traces and fitted
# parameters are indexed against). Use --overwrite to replace lmm_fixed.csv itself.
# Note: the shipped file preserves the participant/row order of the original (pre-anonymisation)
# raw-file listing; the regenerated file follows preprocessed_data.csv. Row order does not affect
# any reported statistic, but the participant index of the stored traces follows the shipped order.
# ---------------------------------------------------------------------------
import sys, os
out = 'lmm_fixed.csv' if '--overwrite' in sys.argv else 'lmm_fixed_regenerated.csv'
df.to_csv(out, index=False)
print(f'wrote {out}:', df.shape)
if os.path.exists('lmm_fixed.csv') and out != 'lmm_fixed.csv':
    ref = pd.read_csv('lmm_fixed.csv')
    ref = ref.drop(columns=[c for c in ref.columns if c.startswith('Unnamed')])
    key = ['sub', 'trial_num', 'decision']
    a = df.sort_values(key).reset_index(drop=True); b = ref.sort_values(key).reset_index(drop=True)
    diffs = []
    for c in [c for c in ref.columns if c in a.columns]:
        x, y = a[c], b[c]
        try:
            eq = np.allclose(x.astype(float).fillna(-999), y.astype(float).fillna(-999), atol=1e-9)
        except (ValueError, TypeError):
            eq = (x.fillna('NA').astype(str) == y.fillna('NA').astype(str)).all()
        if not eq: diffs.append(c)
    print('comparison with shipped lmm_fixed.csv (after aligning row order): differing columns =', diffs or 'none')
