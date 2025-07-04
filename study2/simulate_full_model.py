
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from random import shuffle,sample
import seaborn as sns
from scipy.special import expit, softmax
from matplotlib.legend_handler import HandlerTuple
import os


def basename_without_ext(path):
    return os.path.splitext(os.path.basename(path))[0]



def MF_ChoiceBias_MB_Breadth_Depth_simulate(parameters,df):
	from scipy.special import comb
	sim_data=[]
	j=0
	for i in range(len(parameters[0])):
		for play in range(1):
			data=df[i] # subject dataframe
			subject=i+1
			
			np.seterr(divide='ignore')

			# extract parameters
			mb_control=parameters[0][i]
			discount_rate = parameters[1][i]
			mb_breadth =parameters[2][i]
			mb_breadth2 = parameters[3][i]
			mb_cache = parameters[4][i]
			choice_bias = parameters[5][i]
			
			forgetting_cache = parameters[6][i]
			
			effect_reward = parameters[7][i]
			cache_plan=parameters[8][i]

		
			mb_key = {
				(3, 1, 'start'):           [1, 8], 
				(3, 2, 'toothbrush'): [1,4], 
				(3, 2, 'baby'):        [0,    0],
				(3, 3, 'car'):        [1,2], 
				(3, 3, 'backpack'):   [0,    0],
				(3, 3, 'bowtie'):     [0,    0],
				(2, 1, 'start'):           [2,8], 
				(2, 2, 'toothbrush'): [1,4], 
				(2, 2, 'baby'):        [1,4], 
				(2, 3, 'backpack'):   [1,2], 
				(2, 3, 'bowtie'):     [0,    0],
				(2, 3, 'car'):        [0,    0],
				(1, 1, 'start'):           [4,8], 
				(1, 2, 'toothbrush'): [2,4], 
				(1, 2, 'baby'):        [2,4], 
				(1, 3, 'backpack'):   [1,2], 
				(1, 3, 'bowtie'):     [1,2], 
				(1, 3, 'car'):        [1,2], 
			}
			
			mb_key2 = {
				(3, 1, 'start'):           [0, 0],
				(3, 2, 'toothbrush'): [0.0, 0],
				(3, 2, 'baby'):        [0.0,    0],
				(3, 3, 'car'):        [0.0,  0],
				(3, 3, 'backpack'):   [0,    0],
				(3, 3, 'bowtie'):     [0,    0],
				(2, 1, 'start'):           [1,4], 
				(2, 2, 'toothbrush'): [0.0, 0],
				(2, 2, 'baby'):        [0.0, 0],
				(2, 3, 'backpack'):   [0.0,  0],
				(2, 3, 'bowtie'):     [0,    0],
				(2, 3, 'car'):        [0,    0],
				(1, 1, 'start'):           [2,4], 
				(1, 2, 'toothbrush'): [1,2], 
				(1, 2, 'baby'):        [1,2], 
				(1, 3, 'backpack'):   [0,  0],
				(1, 3, 'bowtie'):     [0,  0],
				(1, 3, 'car'):        [0,  0],
			}
			optimal_key = {
				(3, 1, 'start'):['toothbrush'],
				(3, 2, 'toothbrush'): ['car'],
				(3, 2, 'baby'):['backpack'],
				(3, 3, 'car'):        [0,1],
				(3, 3, 'backpack'):   [0,0],
				(3, 3, 'bowtie'):     [0,1],
				(2, 1, 'start'):['toothbrush','baby'],
				(2, 2, 'toothbrush'): ['backpack'],
				(2, 2, 'baby'): ['backpack'],
				(2, 3, 'backpack'):   [0,1],
				(2, 3, 'bowtie'):    [0,0],
				(2, 3, 'car'):        [0,0],
				(1, 1, 'start'):           ['toothbrush','baby'],
				(1, 2, 'toothbrush'): ['backpack','bowtie','car'],
				(1, 2, 'baby'):       ['backpack','bowtie','car'],
				(1, 3, 'backpack'):  [0,1],
				(1, 3, 'bowtie'):     [0,1],
				(1, 3, 'car'):        [0,1],
			}

			cache_plans={(3, 1):np.zeros((2)),
				(3, 2): np.zeros((2)),
				(3, 3): np.zeros((2)),
				(2, 1):np.zeros((2)), 
				(2, 2):np.zeros((2)),
				(2, 3): np.zeros((2)),
			
				(1, 1): np.zeros((2)), 
				(1, 2): np.zeros((2)), 
				(1, 3):   np.zeros((2))
				}
			keys = list(mb_key.keys())
			learned_policy = {key: [0,0] for key in keys}
			cached_policy = {key: [0,0] for key in keys}

			choice_biases = {key: [0,0] for key in keys}
			for key in keys:
				choice_biases[key][0] = choice_bias
			
			transitions = {
			'start': ['space','toothbrush', 'baby'],
			'baby': ['space','bowtie','backpack'],
			'toothbrush': ['space','backpack', 'car'],
			'backpack': ['space','lamp', 'zebra'],
			'bowtie': ['space','knight', 'lamp'],
			'car': ['space','lamp', 'cat']}

			keys_caching = {(*k, s): np.zeros((2))
                  for k in keys
                  for s in (0, 1)}


			experiences_action1 = {key: 0 for key in keys}
			experiences_action2 = {key: 0 for key in keys}
			last_outcome_a1 = {key: 0 for key in keys}
			last_outcome_a2 = {key: 0 for key in keys}

			optimal_policy_1 = {key: [0,0] for key in keys}
			

			# MB key: base probabilities and initial experience (second element unused after vectorizing)
			# MB key: base probabilities and initial experience (second element unused after vectorizing)
				# MB key: base probabilities and initial experience (second element unused after vectorizing)
				# ---------------------------------------------------------------------
			# 1. helper -----------------------------------------------------------
			# ---------------------------------------------------------------------

			def update_probability_planning_success(num_successes, total, draws):
				"""
				Vectorised probability of obtaining ≥1 success after *draws*
				(without replacement) from an urn with:
					num_successes  – blue balls   (successes)
					total          – total balls (N)

				Parameters
				----------
				num_successes : int
				total         : int
				draws         : ndarray (float allowed; will be ceil-ed to int)

				Returns
				-------
				p_success : ndarray of float, same shape as draws
				"""
				# d = np.ceil(draws).astype(int)              # round up partial draws
				failures = total - num_successes            # red balls

				p_no_success = 0

				if draws <= failures:                        # comb() only defined here
			
					p_no_success= (
						comb(failures, draws, exact=False) /
						comb(total,    draws, exact=False))

				# If draws exceed all red balls, probability of zero success is 0
				return 1.0 - p_no_success
	

			def compute_mbmc_values_vectorized(key, mb_breadth_arr,mb_breadth_arr2, exp_arr,exp_arr2,last_choice_one,last_choice_two):
				# change function so that it does all decision points at the same time.
				num_success1, total1 = mb_key[key]
				num_success2, total2 = mb_key2[key]

				# -----------------------------------------------------------------
				# update the running "experience" counters (= cumulative draws)
				goal, decision, _ = key
				if num_success1 > 0:
					exp_arr  += mb_breadth_arr     # add breadth this visit
				if num_success2 > 0:
					exp_arr2 += mb_breadth_arr2

				# -----------------------------------------------------------------
				# NEW: exact success probabilities with the threshold property
				


				if total1 > 0 and num_success1 > 0:
					p_one = update_probability_planning_success(num_success1, total1, exp_arr)
				else:
					p_one = np.zeros_like(exp_arr)

				if total2 > 0 and num_success2 > 0:
					p_two = update_probability_planning_success(num_success2, total2, exp_arr2)

				else:
					p_two = np.zeros_like(exp_arr2)

				p_two_real=p_one*p_two
				P_two_real_fail=1-p_two_real
				p_one_real = p_one*(1-p_two)
				p_one_real_fail=1-p_one_real
				


				# value arrays
				v_take = 0
				v_rel  = 0
			


				
				One_Succeeded =  np.random.choice([0,1], p=[p_one_real_fail,p_one_real])
				Two_Succeeded =  np.random.choice([0,1], p=[P_two_real_fail,p_two_real])
				Succeed=1 #assume planning success unless failure
				if not One_Succeeded:
					if not Two_Succeeded:
						Succeed=0 #failure
					
	



				if goal == 3:
					if One_Succeeded:
						v_take  = 4*(discount_rate**(3-decision)); 
						v_rel  = 1
					else:
						v_rel   = 1

				elif goal == 2:
					if decision == 1:
						if Two_Succeeded:
							v_take  = 4*(discount_rate**(3-decision))
							v_rel  = 1+4*(discount_rate**(3-decision))
						elif One_Succeeded:
							v_take  = 4*(discount_rate**(3-decision)); 
							v_rel  = 1
						else:
							v_rel   = 1

					else:
						
						if One_Succeeded:
							v_take  = 4*(discount_rate**(3-decision)); 
							v_rel  = 1
						else:
							v_rel   = 1


				elif goal == 1:
					if decision < 3:
						if Two_Succeeded:
							v_take  = 4*(discount_rate**(3-decision))
							v_rel  = 1+4*(discount_rate**(3-decision))
						elif One_Succeeded:
							v_take  = 4*(discount_rate**(3-decision)); 
							v_rel  = 1
						else:
							v_rel   = 1

						
					else:
						if One_Succeeded:
							v_take  = 4*(discount_rate**(3-decision)); 
							v_rel  = 1
						else:
							v_rel   = 1

				return v_take, v_rel, exp_arr,exp_arr2,Two_Succeeded+(1-One_Succeeded),last_choice_two,Succeed
			
			def push_recent_key(recent_keys, key):
				"""
				Move `key` to the end of `recent_keys` (newest position).
				Ensures each key appears at most once.
				"""
				try:
					recent_keys.remove(key)   # O(N) but N is small in WM context
				except ValueError:
					pass                      # key not yet in list
				recent_keys.append(key)       # newest item is last
				return recent_keys
			
			# loop over trials
			trials = np.sort(data['trial_num'].unique())
			recent_keys1=[]
			recent_keys2=[]
			recent_keys3=[]
			
			for trial in trials:
				df_temp = data[data['trial_num'] == trial].reset_index(drop=True)
				RT = df_temp['RT'].values
				planning_depth_val = int(df_temp['planning_depth'].values[0])
				current_states_orig = df_temp['current_state'].values
				trial_goal=df_temp['trial_num_within_goal'].values[0]
				# reward from subsequent choices (as in original)
				last_key=(planning_depth_val, 1, current_states_orig[0])
				last_outcome_a1[last_key]=0
				last_outcome_a2[last_key]=0
				imm_rewards=0
				orig_goal_outcome=df_temp['got_to_goal'].values[0]
				actions={'a1':0,'a2':0,'a3':0}
				keys_recent=[]
				current_state='start'
				match_state=0
				for decision in (1, 2, 3):
					j+=1

					sim_data.append({
						'sub':subject,
						'goal':planning_depth_val,
						'trial_num_within_goal':trial_goal,
						'trial_num':trial,
						'trial':trial_goal,
						'current_state':current_state,
						'planning_depth':planning_depth_val,
						'decision':decision
						})

					key = (planning_depth_val, decision, current_state)
					key_plan = (planning_depth_val, decision)
					keys_recent.append(key)
					# vectorized MBMC computation
					
					vt, vr, experiences_action1[key],experiences_action2[key],la1,la2,plan_success = \
						compute_mbmc_values_vectorized(key,mb_breadth,mb_breadth2,experiences_action1[key],experiences_action2[key],last_outcome_a1[last_key],last_outcome_a2[last_key])
					
					last_key=key
					last_outcome_a1[last_key]=la1
					last_outcome_a2[last_key]=la2
					
					optimal_policy_1[key]    = [vt, vr]
				
					# integrated Q-values
					Q_both = np.multiply(optimal_policy_1[key],mb_control) \
							+ choice_biases[key] \
							+ cached_policy[key] \
							+ cache_plans[key_plan]
					#update learned policy
					
					action_probs = softmax(Q_both)
					chosen_action = np.random.choice([0,1], p=action_probs)
					
					act=chosen_action

					keya = (planning_depth_val, decision, current_state,act)
					if decision==1:
						recent_keys1=push_recent_key(recent_keys1,keya)
					elif decision==2:
						recent_keys2=push_recent_key(recent_keys2,keya)
					elif decision==3:
						recent_keys3=push_recent_key(recent_keys3,keya)
					
					if plan_success:
						success_plan=True
					else:
						success_plan=False

					if decision<3:
						if act==1:
							imm_rewards+=1
							if basename_without_ext(current_states_orig[decision]) in transitions[current_state][1:3]:
								current_state=basename_without_ext(current_states_orig[decision])
							else:
								current_state=sample(transitions[current_state][1:3],1)[0]
						else:
							if basename_without_ext(current_states_orig[decision]) in transitions[current_state][1:3]:
								current_state=basename_without_ext(current_states_orig[decision])
							else:
								if success_plan:
									current_state=sample(optimal_key[key],1)[0]
								else:
									current_state=sample(transitions[current_state][1:3],1)[0]

					if decision==3:
						if 1 in optimal_key[key]:	
							goal_outcome=1
						else:
							goal_outcome=0
						


						# if current_state==basename_without_ext(current_states_orig[2]):
						# 	goal_outcome=orig_goal_outcome
						# else:
						

					actions['a{}'.format(decision)]=act
					if decision<3:
						key_plan_next = (planning_depth_val, decision+1)
						if act==0:
							cache_plans[key_plan_next][0]=cache_plan
						else:
							cache_plans[key_plan_next][0]=0

					

					
					# 'choice_numeric':act,
					# 	'control choice':(chosen_action-1)*-1,
					sim_data[j-1]['choice_numeric']=act
					sim_data[j-1]['control choice']=(chosen_action-1)*-1
					
				act1=recent_keys1[-1][-1]
				act2=recent_keys2[-1][-1]
				act3=recent_keys3[-1][-1]
				key1=recent_keys1[-1][:-1]
				key2=recent_keys2[-1][:-1]
				key3=recent_keys3[-1][:-1]
				for i in range(3):
					sim_data[j-3+i]['got_to_goal']=goal_outcome
				if goal_outcome==0:
					goal_outcome=-1

				cached_policy[key1][act1]=mb_cache+effect_reward*goal_outcome
				cached_policy[key2][act2]=mb_cache+effect_reward*goal_outcome
				cached_policy[key3][act3]=mb_cache+effect_reward*goal_outcome
				
				# Recency index: 0 = newest, 1 = 2nd-newest, …
				rec_idx = {k: r for r, k in enumerate(reversed(recent_keys1))}
				far = len(recent_keys1) + 1      # “never seen” sentinel

				rec_idx2 = {k: r for r, k in enumerate(reversed(recent_keys2))}
				far2 = len(recent_keys2) + 1      # “never seen” sentinel

				rec_idx3 = {k: r for r, k in enumerate(reversed(recent_keys3))}
				far3 = len(recent_keys3) + 1      # “never seen” sentinel

				for key in keys_caching.keys():
					reduced_key=key[:-1]
					action=key[3]
					if key[1]==1:
						rec = rec_idx.get(key, far)               # scalar
						decay = np.exp(-forgetting_cache * rec)         # shape (S,)
						cached_policy[reduced_key][action] *= decay
					elif key[1]==2:
						rec = rec_idx2.get(key, far2)               # scalar
						decay = np.exp(-forgetting_cache * rec)         # shape (S,)
						cached_policy[reduced_key][action] *= decay
					elif key[1]==3:
						rec = rec_idx3.get(key, far3)               # scalar
						decay = np.exp(-forgetting_cache * rec)         # shape (S,)
						cached_policy[reduced_key][action]       *= decay		

			

	return sim_data
	
	# mb_control=parameters[0][i]
	# 		discount_rate = parameters[1][i]
	# 		mb_breadth =parameters[2][i]
	# 		choice_bias = parameters[3][i]
	# 		mb_breadth2 = parameters[4][i]
	# 		caching_wins = parameters[5][i]
	# 		cache_beta = parameters[6][i]
	# 		caching_wins = parameters[7][i]
	# 		caching_wins = parameters[8][i]



MB_model = np.load('MB_B_exec.npy')
MB_depth = np.load('MB_depth_exec.npy')
MB_breadth2 = np.load('breadth2_exec.npy') * 4
MB_breadth1 = np.load('MB_breadth_exec.npy') * 8
cb = np.load('cb_exec.npy')
forgetting_cache = np.load('forget_exec.npy')
caching_rwd = np.load('mbcache_exec.npy')
caching_no_rwd = np.load('cache_reward_exec.npy')
plan_exec = np.load('cache_plan_exec.npy')

# parameter_list=[MB_model,MB_depth,MB_breadth1,MB_breadth2,caching_rwd,cb,forgetting_cache,caching_no_rwd,plan_exec]
# df=pd.read_csv('lmm_fixed.csv')
# dfs=[df[df['sub']==sub].reset_index(drop=True) for sub in pd.read_csv('lmm_fixed.csv')['sub'].unique()]
# print(len(dfs))
# sub_ID_names=[x['sub'][10] for x in dfs]
# subj_dfs=dfs

# sim_data=MF_ChoiceBias_MB_Breadth_Depth_simulate(parameter_list,subj_dfs)

# sim_df = pd.DataFrame(sim_data)
# sim_df.to_csv('simulated_data.csv')
# # sim_df=pd.read_csv('simulated_data.csv')


# # # ################### PLOTTTING ###############################################
# # sim_df.to_csv('simulated_data.csv', index=False)
# sns.set(style='white', font_scale=2.5, palette='Set2')
# custom_palette1 = [ (0.5208627450980392, 0.6399215686274509, 0.602392156862745),
# 				  (0.460070588235294, 0.7007137254901961, 0.6248588235294118),
# 				  (0.4, 0.7607843137254902, 0.6470588235294118)]
# custom_palette2 = [  (0.785921568627451, 0.6422745098039215, 0.5866274509803922),
# (0.8876823529411766, 0.5973411764705883, 0.48486666666666656),
# (0.9882352941176471, 0.5529411764705883, 0.3843137254901961)]
# custom_palette3 = [
# 				  (0.6343921568627452, 0.6589803921568628, 0.7146274509803922),
# (0.5934235294117648, 0.643121568627451, 0.7555960784313726),
# (0.5529411764705883, 0.6274509803921569, 0.796078431372549)]
# # Plot the lines on two facets
# ax=sns.lmplot(
# 	data=sim_df[sim_df['planning_depth']==1],
# 	x="trial", y="control choice",scatter=False,
# 	hue="decision", palette=custom_palette1,logistic=True,legend=False)

# for axs in ax.axes.flat: 
# 	axs.set_xticks([1, 5, 10, 15, 20]) 
# 	axs.set_yticks([0,0.5,1])
# plt.savefig('controlTaking_by_time_depth1_SIM_BFP.png', dpi=300,bbox_inches='tight')

# plt.show()

# # Plot the lines on two facets
# ax=sns.lmplot(
# 	data=sim_df[sim_df['planning_depth']==2],
# 	x="trial", y="control choice",logistic=True,scatter=False,
# 	hue="decision", palette=custom_palette2,legend=False)

# for axs in ax.axes.flat: 
# 	axs.set_xticks([1, 5, 10, 15, 20])
# 	axs.set_yticks([0,0.5,1])
# plt.savefig('controlTaking_by_time_depth2_SIM_BFP.png', dpi=300,bbox_inches='tight')

# plt.show()

# # Plot the lines on two facets
# ax=sns.lmplot(
# 	data=sim_df[sim_df['planning_depth']==3],
# 	x="trial", y="control choice",logistic=True,scatter=False,
# 	hue="decision", palette=custom_palette3,legend=False)

# for axs in ax.axes.flat: 
# 	axs.set_xticks([1, 5, 10, 15, 20])
# 	axs.set_yticks([0,0.5,1])
# plt.savefig('controlTaking_by_time_depth3_SIM_BFP.png', dpi=300,bbox_inches='tight')

# plt.show()


# # Plot mean control taken over trials
# sim_df['planning depth']=sim_df['planning_depth']
# ax = sns.barplot(x="planning depth", y="control choice", hue="decision",data=sim_df)
# for bar_group, desaturate_value in zip(ax.containers, [0.33,0.667,1]):
# 		for bar, color in zip(bar_group, plt.cm.Set2.colors):
# 			bar.set_facecolor(sns.desaturate(color, desaturate_value))
# labels=[bar_group.get_label() for bar_group in ax.containers]
# ax.legend(handles=[tuple(bar_group) for bar_group in ax.containers],loc='lower left',
# 	labels=['decision=1' if '0' in x else 'decision=2' if '1' in x else 'decision=3' for x in labels],
# 	prop={'size': 14},
# 	handlelength=9, handler_map={tuple: HandlerTuple(ndivide=None, pad=0.1)})


# plt.yticks([0,0.5,1])

# # Saving the plot
# plt.tight_layout()
# plt.savefig('MODELsimulated_BestFittingParams_optimal_Control_by_planningdepth.png', dpi=300)
# plt.show()



from scipy.special import expit
import scipy
# ─── 1) Load the ground‐truth parameter arrays ──────────────────────────────────
# df=sim_df
# dfs=[df[df['sub']==sub].reset_index(drop=True) for sub in pd.read_csv('simulated_data.csv')['sub'].unique()]
# sim_df=dfs
# print(sim_df[0].head())


# number_subjects=len(MB_model)
# num_subjects=number_subjects
# num_trials=len(sim_df[0]['trial_num'].unique())
##### Fit model to simulated data

def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution(samples, data, rng_samples):
	from scipy.special import logsumexp, expit 
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	
	
	mb_breadth2 =samples[3][rng_samples]*4

	mb_cache =samples[4][rng_samples]

	choice_bias =samples[5][rng_samples]

	forgetting_cache =samples[6][rng_samples]

	cache_reward =samples[7][rng_samples]
	cache_plan=samples[8][rng_samples]


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
				(3, 1, 'start'):           [1, 8], 
				(3, 2, 'toothbrush'): [1,4], 
				(3, 2, 'baby'):        [0,    0],
				(3, 3, 'car'):        [1,2], 
				(3, 3, 'backpack'):   [0,    0],
				(3, 3, 'bowtie'):     [0,    0],
				(2, 1, 'start'):           [2,8], 
				(2, 2, 'toothbrush'): [1,4], 
				(2, 2, 'baby'):        [1,4], 
				(2, 3, 'backpack'):   [1,2], 
				(2, 3, 'bowtie'):     [0,    0],
				(2, 3, 'car'):        [0,    0],
				(1, 1, 'start'):           [4,8], 
				(1, 2, 'toothbrush'): [2,4], 
				(1, 2, 'baby'):        [2,4], 
				(1, 3, 'backpack'):   [1,2], 
				(1, 3, 'bowtie'):     [1,2], 
				(1, 3, 'car'):        [1,2], 
			}
			
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'toothbrush'): [0.0, 0],
		(3, 2, 'baby'):        [0.0,    0],
		(3, 3, 'car'):        [0.0,  0],
		(3, 3, 'backpack'):   [0,    0],
		(3, 3, 'bowtie'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'toothbrush'): [0.0, 0],
		(2, 2, 'baby'):        [0.0, 0],
		(2, 3, 'backpack'):   [0.0,  0],
		(2, 3, 'bowtie'):     [0,    0],
		(2, 3, 'car'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'toothbrush'): [1,2], 
		(1, 2, 'baby'):        [1,2], 
		(1, 3, 'backpack'):   [0,  0],
		(1, 3, 'bowtie'):     [0,  0],
		(1, 3, 'car'):        [0,  0],
	}
	optimal_key = {
		(3, 1, 'start'):['toothbrush'],
		(3, 2, 'toothbrush'): ['car'],
		(3, 2, 'baby'):['backpack'],
		(3, 3, 'car'):        [0,1],
		(3, 3, 'backpack'):   [0,0],
		(3, 3, 'bowtie'):     [0,1],
		(2, 1, 'start'):['toothbrush','baby'],
		(2, 2, 'toothbrush'): ['backpack'],
		(2, 2, 'baby'): ['backpack'],
		(2, 3, 'backpack'):   [0,1],
		(2, 3, 'bowtie'):    [0,0],
		(2, 3, 'car'):        [0,0],
		(1, 1, 'start'):           ['toothbrush','baby'],
		(1, 2, 'toothbrush'): ['backpack','bowtie','car'],
		(1, 2, 'baby'):       ['backpack','bowtie','car'],
		(1, 3, 'backpack'):  [0,1],
		(1, 3, 'bowtie'):     [0,1],
		(1, 3, 'car'):        [0,1],
	}

	cache_plans={(3, 1):np.zeros((sample_size,2)),
		(3, 2): np.zeros((sample_size,2)),
		(3, 3): np.zeros((sample_size,2)),
		(2, 1):np.zeros((sample_size,2)), 
		(2, 2):np.zeros((sample_size,2)),
		(2, 3): np.zeros((sample_size,2)),
	
		(1, 1): np.zeros((sample_size,2)), 
		(1, 2): np.zeros((sample_size,2)), 
		(1, 3):   np.zeros((sample_size,2))
		}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = choice_bias
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}

	probability_mb1 = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_1 = {key: np.zeros((sample_size, 2)) for key in keys}
	probability_mb2 = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_2 = {key: np.zeros((sample_size, 2)) for key in keys}
	probability_mb_none = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_3 = {key: np.zeros((sample_size, 2)) for key in keys}

	# MB key: base probabilities and initial experience (second element unused after vectorizing)
		# MB key: base probabilities and initial experience (second element unused after vectorizing)
		# ---------------------------------------------------------------------
	# 1. helper -----------------------------------------------------------
	# ---------------------------------------------------------------------

	def update_probability_planning_success(num_successes, total, draws):
		"""
		Vectorised probability of obtaining ≥1 success after *draws*
		(without replacement) from an urn with:
			num_successes  – blue balls   (successes)
			total          – total balls (N)

		Parameters
		----------
		num_successes : int
		total         : int
		draws         : ndarray (float allowed; will be ceil-ed to int)

		Returns
		-------
		p_success : ndarray of float, same shape as draws
		"""
		# d = np.ceil(draws).astype(int)              # round up partial draws
		failures = total - num_successes            # red balls

		p_no_success = np.zeros_like(draws, dtype=float)

		mask = draws <= failures                        # comb() only defined here
		if np.any(mask):
			# SciPy’s comb is vectorised when exact=False
			p_no_success[mask] = (
				comb(failures, draws[mask], exact=False) /
				comb(total,    draws[mask], exact=False)
			)

		# If draws exceed all red balls, probability of zero success is 0
		return 1.0 - p_no_success
	

	# ---------------------------------------------------------------------
	# 2. replacement for compute_mbmc_values_vectorized -------------------
	#    (only the parts that compute p_two, p_one, p_fail are changed)
	# ---------------------------------------------------------------------
	def compute_mbmc_values_vectorized(
			key, mb_depth_array, mb_breadth_arr, mb_breadth_arr2,
			exp_arr, exp_arr2):

		# --- unpack dictionary entries -----------------------------------
		# mb_key[key]    = [num_successes, total_rollouts]
		# mb_key2[key]   = [num_successes, total_rollouts]   (2-step success)
		num_success1, total1 = mb_key[key]
		num_success2, total2 = mb_key2[key]

		# -----------------------------------------------------------------
		# update the running "experience" counters (= cumulative draws)
		goal, decision, _ = key
		if num_success1 > 0:
			exp_arr  += mb_breadth_arr     # add breadth this visit
		if num_success2 > 0:
			exp_arr2 += mb_breadth_arr2

		# -----------------------------------------------------------------
		# NEW: exact success probabilities with the threshold property
		


		if total1 > 0 and num_success1 > 0:
			p_one = update_probability_planning_success(num_success1, total1, exp_arr)
		else:
			p_one = np.zeros_like(exp_arr)

		if total2 > 0 and num_success2 > 0:
			p_two = update_probability_planning_success(num_success2, total2, exp_arr2)

		else:
			p_two = np.zeros_like(exp_arr2)

		
		p_one  = np.minimum(p_one, 1)
		p_two  = np.minimum(p_two, 1)
		p_two=p_one*p_two
		p_one=p_one*(1-p_two)
		p_fail=1-(p_one+p_two)



	

		# value arrays
		v2_take = np.zeros_like(p_one)
		v2_rel  = np.zeros_like(p_one)
		v1_take = np.zeros_like(p_one)
		v1_rel  = np.zeros_like(p_one)
		v0_take = np.zeros_like(p_one)
		v0_rel  = np.zeros_like(p_one)

		
		# degenerate: depth too shallow → always fail
		# failure, relinquish value
		remainder=np.zeros_like(p_one)

	

		# non-degenerate mask
		

		if goal == 3:
			v2_take = 4*(discount_rate**(3-decision)); v2_rel += 1
			v1_take = 4*(discount_rate**(3-decision)); v1_rel += 1
			v0_rel  += 1
			

		elif goal == 2:
			if decision == 1:
				v2_take  = 4*(discount_rate**(3-decision)); v2_rel  = 1+4*(discount_rate**(3-decision))								
				v1_take  = 4*(discount_rate**(3-decision)); v1_rel  += 1
				v0_rel   += 1

			else:
				v2_take = 4*(discount_rate**(3-decision)); v2_rel += 1
				v1_take = 4*(discount_rate**(3-decision)); v1_rel += 1
				v0_rel  += 1

		elif goal == 1:
			if decision < 3:
				#initiate a recursive function call that allows people to tkae control if control was taken
				v2_take  = 4*(discount_rate**(3-decision)); v2_rel  = 1+4*(discount_rate**(3-decision))
				v1_take  = 4*(discount_rate**(3-decision)); v1_rel  += 1
				v0_rel   += 1
		
				 
			elif decision==3:
				v2_take = 4*(discount_rate**(3-decision)); v2_rel += 1
				v1_take = 4*(discount_rate**(3-decision)); v1_rel += 1
				v0_rel  += 1

			

		return p_two, v2_take, v2_rel, p_one, v1_take, v1_rel, p_fail, v0_take, v0_rel, exp_arr,exp_arr2
	def push_recent_key(recent_keys, key):
		"""
		Move `key` to the end of `recent_keys` (newest position).
		Ensures each key appears at most once.
		"""
		try:
			recent_keys.remove(key)   # O(N) but N is small in WM context
		except ValueError:
			pass                      # key not yet in list
		recent_keys.append(key)       # newest item is last
		return recent_keys
	# loop over trials
	trials = np.sort(data['trial_num'].unique())
	recent_keys1=[]
	recent_keys2=[]
	recent_keys3=[]
	for trial in trials:
		df_temp = data[data['trial_num'] == trial].reset_index(drop=True)
		actions = df_temp['choice_numeric'].values
		
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			key_plan = (planning_depth_val, decision)
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
		
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key] \
					+choice_biases[key] \
					+cache_plans[key_plan]
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key] \
					+choice_biases[key] \
					+cache_plans[key_plan]
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key] \
					+cache_plans[key_plan]
					  )
			
			logp_none = Q_none[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_none, axis=1)
			
			#check to make all probabilities above exact 0 point
			eps2=1e-20
			z2 = p2 <=0
			p2[z2]=eps2
		
			z1 = p1 <=0
			p1[z1]=eps2
	
			z0 = p0 <=0
			p0[z0]=eps2

			log_succ1 = np.log(p2) + logp_both
			log_succ2 = np.log(p1) + logp_one
			log_fail  = np.log(p0) + logp_none



			# mixture log-likelihood
			log_mix = np.logaddexp(np.logaddexp(log_succ1, log_succ2), log_fail)
			
			lik += log_mix

			# update learned policy
			idx = np.arange(sample_size)
			act = actions[decision - 1]

			
			recent_acts.append(act)
			other_act=int((act-1)*-1)
			recent_other_acts.append(other_act)
			

		
			
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect
			if decision<3:
				key_plan_next = (planning_depth_val, decision+1)
				if act==0:
					cache_plans[key_plan_next][:,0]=cache_plan
				else:
					cache_plans[key_plan_next][:,0]=0


		
			key = (planning_depth_val, decision, current_states[decision - 1],act)
			if decision==1:
				recent_keys1=push_recent_key(recent_keys1,key)
			elif decision==2:
				recent_keys2=push_recent_key(recent_keys2,key)
			elif decision==3:
				recent_keys3=push_recent_key(recent_keys3,key)

		# Recency index: 0 = newest, 1 = 2nd-newest, …
		rec_idx = {k: r for r, k in enumerate(reversed(recent_keys1))}
		far = len(recent_keys1) + 1      # “never seen” sentinel

		rec_idx2 = {k: r for r, k in enumerate(reversed(recent_keys2))}
		far2 = len(recent_keys2) + 1      # “never seen” sentinel

		rec_idx3 = {k: r for r, k in enumerate(reversed(recent_keys3))}
		far3 = len(recent_keys3) + 1      # “never seen” sentinel

		for key in keys_caching.keys():
			reduced_key=key[:-1]
			action=key[3]
			if key[1]==1:
				rec = rec_idx.get(key, far)               # scalar
				decay = np.exp(-forgetting_cache * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==2:
				rec = rec_idx2.get(key, far2)               # scalar
				decay = np.exp(-forgetting_cache * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==3:
				rec = rec_idx3.get(key, far3)               # scalar
				decay = np.exp(-forgetting_cache * rec)         # shape (S,)
				cached_policy[reduced_key][:, action]       *= decay		


		# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
				
	

	return lik


# ############################################### DEFINE FUNCTIONS TO BE USED IN HIERARCHICAL MODELLING ###############################################################


#function to sample parameters within a model

def sample_parameters(distribution_type,hyperparameter_list,sample_size):
	from numpy.random import beta,gamma,chisquare,poisson,uniform,logistic,multinomial,binomial
	from numpy.random import normal as norm
	counter=1
	for num in hyperparameter_list:
		exec("global hp_{}; hp_{}={}".format(counter,counter,num))
		counter+=1
	exec("global sample; sample={}({},{},{})".format(distribution_type,hp_1,hp_2,sample_size))

	return sample
	
# MODEL CLASS: assumes a hierarchical model 
# population parameters and subject level parameters 
# are jointly fit

#  The structure of the model class:
#         GROUP LEVEL:
#              Name - E.g., Standard Q Learning
#              Sample Size - How many samples for each parameter
#              Lik - Likelihood function
#              iBIC - Total evidence accounting for model complexity
#              Total_Evidence: Sum of Subject-Level Evidences (sum b/c in log-space)
#              Parameters (entries below x #parameters):
#                     Hyperparameters - e.g., [mu,sigma]
#                     Distribution Type - e.g., Beta
#                     Name - e.g., Lrate-Value
#
#        SUBJECT LEVEL: 
#           Evidence (i.e., log mean likelihood)
#           Parameters (entries below x #parameters):       
#                 posterior mean
#                 credible interval (95%)
#                 samples
#                 num_good_samples (not non or inf samples)

   # import the types



class model:
	
	def __init__(self):
		self.name=0
		self.num_subjects=0
		self.params=self.groupParams()
		self.subjfit=self.subjFit()
		self.subj_level_info=self.subjFit.subjParams()
		self.sample_size=0
		self.model_evidence_group=0
		self.bic=10**10 #arbitrarily high starting iBIC
		self.lik_func=0 #likelihood function
		
	
	class groupParams:
		
		def __init__(self):
			self.name='eta'
			self.distribution='beta'
			self.hyperparameters=[1,2]
							
	class subjFit:
		def __init__(self):
			self.model_evidence_subject=0
			self.subj_level_info=self.subjParams()
			
		class subjParams:
			def __init__(self):
				self.posterior_mean=0
				self.credible_interval=0
				self.samples=[]
				self.num_good_samples=[] #not nan or inf
				

#retrieve list of parameters from model
def get_parameters_for_model(model):
	parameters=[]
	parameter_dict={}
	for var in vars(model):
		exec('global x; x={}.{}'.format(model.name,var))
		if type(x)==model.groupParams:
			if var!='params':
				parameters.append(var)

	return parameters

def get_parameters_for_model_parallel(model):
	parameters=[]

	for var in vars(model):
		exec('global x; x={}.{}'.format(model.name,var))
		if type(x)==model.groupParams:
			if var!='params':
				param_info=[]
				param_info.append(var)
				exec('param_info.append({}.{}.distribution)'.format(model.name,var))
				exec('param_info.append({}.{}.hyperparameters)'.format(model.name,var))
				parameters.append(param_info)

	return parameters

def build_model(name,likelihood,group_parameters_info,number_subjects,sample_size):
	from scipy.stats import beta,gamma,norm,poisson,uniform,logistic,multinomial
	#  INPUTS:
	#     name = name of model
	#     likelihood = likelihood function
	#     group_parameter_info = *Python dictionary* 
	#       defining parameter names, distributions and hyperparameters
	#       EXAMPLE: {'eta':['beta',[1,1]]}
	#     sample_size = number of samples from prior over group parameters
	
	#  OUTPUTS:
	#     model class (see above)
	
	exec('{}=model()'.format(name,name),globals())
	exec('{}.name="{}"'.format(name,name))
	exec('{}.num_subjects={}'.format(name,number_subjects))
	exec('{}.lik_func={}'.format(name,likelihood))
	exec('{}.sample_size={}'.format(name,sample_size))
	
	#encode in model the number of subjects and parameters in one's data
	for parameter in group_parameters_info:
		exec('{}.{}={}.groupParams()'.format(name,parameter,name))
		exec('{}.{}.name="{}"'.format(name,parameter,parameter))
		exec('{}.{}.distribution="{}"'.format(name,parameter,group_parameters_info[parameter][0]))
		exec('{}.{}.hyperparameters={}'.format(name,parameter,group_parameters_info[parameter][1]))
		exec('{}.{}.sample_size={}'.format(name,parameter,sample_size))
		exec('{}.{}.samples=sample_parameters("{}",{},{})'.format(name,parameter,group_parameters_info[parameter][0],group_parameters_info[parameter][1],sample_size))

	for sub in range(number_subjects):
		exec('{}.subject{}={}.subjFit()'.format(name,sub,name))
		for parameter in group_parameters_info:
			exec('{}.subject{}.{}={}.subject{}.subjParams()'.format(name,sub,parameter,name,sub))

def each_param(parameter,model,valid_parameter_indices,weights,subject,good_samples):
	exec('global parameter_samples; parameter_samples={}.{}.samples'.format(model.name,parameter))
	parameter_samps=np.reshape(parameter_samples,(model.sample_size,1))
	good_parameters=parameter_samps[valid_parameter_indices]

	mean,ci,sample=compute_samples(good_parameters,weights)
	exec('{}.subject{}.{}.posterior_mean={}'.format(model.name,subject,parameter,mean))
	exec('{}.subject{}.{}.credible_interval={}'.format(model.name,subject,parameter,ci))
	exec('{}.subject{}.{}.samples={}'.format(model.name,subject,parameter,sample))
	exec('{}.subject{}.{}.num_good_samples={}'.format(model.name,subject,parameter,good_samples))

from numpy.random import choice
import random
def each_param_parallel(parameter_samples,valid_parameter_indices,weights):
	# print('param_indices:{}'.format(valid_parameter_indices))
	# print('params:{}'.format(parameter_samples))
	parameter_samps=np.array(parameter_samples)
	good_parameters=parameter_samps[valid_parameter_indices]
	df=pd.DataFrame()
	weights=np.divide(weights,np.sum(weights))
	df['weights']=weights
	df['parameter_samples']=parameter_samps    
	df2=df.sort_values('parameter_samples')
	df2=df2.reset_index(drop=True)
	mean=np.sum(df['weights']*df['parameter_samples'])
	cdf=df2.weights.cumsum()
	cdf=np.array(cdf)
	samples_unweighted=list(df2['parameter_samples'])
	likelihood_weights=list(df2['weights'])
	samples = random.choices(samples_unweighted,cum_weights=list(cdf),k=1000)
	samples=list(samples)
	index_5=next(x[0] for x in enumerate(cdf) if x[1] > 0.0499999)
	index_95=next(x[0] for x in enumerate(cdf) if x[1] > 0.9499999) 
	ci_lower=df2['parameter_samples'][index_5]
	ci_higher=df2['parameter_samples'][index_95]
	ci=[ci_lower,ci_higher]
	results=[mean,ci,samples]
	return results


##from numba import vectorize, float64
def derive_posterior_samples(likelihood_vector,subject):    
	not_infs= ~np.isinf(likelihood_vector)
	not_nans= ~np.isnan(likelihood_vector)
	valid_parameter_indices=not_infs==not_nans     

	likelihood_vector_noinf=likelihood_vector[~np.isinf(likelihood_vector)] 
	likelihood_vector_cleaned=likelihood_vector_noinf[~np.isnan(likelihood_vector_noinf)] 
	good_samples=len(likelihood_vector_cleaned) 

	weights=np.exp(likelihood_vector_cleaned) 
	
	return likelihood_vector_cleaned,valid_parameter_indices,weights,good_samples
	
		


def compute_samples(parameter_samples,weights):
	import time
	import pandas as pd
	
	indices=np.array(indices)
	samples=df2['parameter_samples'][indices]
	samples=list(samples)
	index_5=next(x[0] for x in enumerate(cdf) if x[1] > 0.0499999) 
	index_95=next(x[0] for x in enumerate(cdf) if x[1] > 0.9499999) 
	ci_lower=df2['parameter_samples'][index_5]
	ci_higher=df2['parameter_samples'][index_95]
	ci=[ci_lower,ci_higher]
	
	return val,ci,samples


#fit hyperparameters to group sampled values from posterior. Be sure that you make sure output
# is appropriately handled for non-traditional (i.e., not beta, gamma, normal) distribution


def fit_hyperparameters(model):
	from scipy.stats import beta,gamma,norm,poisson,uniform,logistic
	parameters=get_parameters_for_model(model)
	number_subjects=model.num_subjects
	model_name=model.name
	for parameter in parameters:
		parameter_full_sample=[]
		exec('global distribution; distribution={}.{}.distribution'.format(model_name,parameter))
		for subject in range(number_subjects):
			exec('parameter_full_sample+={}.subject{}.{}.samples'.format(model_name,subject,parameter))
		# parameter_full_sample = np.clip(parameter_full_sample, 0.00000000000001, 0.99999999999999999999999)
		exec('global hyperparameters; hyperparameters={}.fit(parameter_full_sample)'.format(distribution))
		if distribution=='gamma':
			h1=hyperparameters[0]
			h2=hyperparameters[2]
		elif distribution=='uniform':
			h1=hyperparameters[0]
			h2=hyperparameters[1]+hyperparameters[0]
		else:
			h1=hyperparameters[0]
			h2=hyperparameters[1]
		exec('{}.{}.hyperparameters={}'.format(model.name,parameter,[h1,h2]))



def fit_hyperparameters_parallel(model,parameter_info,all_results,number_subjects):
	from scipy.stats import beta,gamma,norm,poisson,uniform,logistic,multinomial
	for parameter in parameter_info:
		parameter_full_sample=[]
		for item in all_results:
			for items in item:
				if parameter[0] in items:
					parameter_full_sample+=items[3]
		
		
		if parameter[1]=='gamma':
			hyperparameters=gamma.fit(parameter_full_sample,floc=0)
			h1=hyperparameters[0]
			h2=hyperparameters[2]
		elif parameter[1]=='uniform':
			hyperparameters=uniform.fit(parameter_full_sample)
			h1=hyperparameters[0]
			h2=hyperparameters[1]+hyperparameters[0]
		elif parameter[1]=='norm':
			hyperparameters=norm.fit(parameter_full_sample)
			h1=hyperparameters[0]
			h2=hyperparameters[1]
		elif parameter[1]=='multinomial':
			hyperparameters=multinomial.fit(parameter_full_sample,floc=0,fscale=1)
			h1=1
			mean_counts = np.mean(parameter_full_sample, axis=0)
			total_counts = np.sum(mean_counts)
			p_est = (mean_counts / total_counts).tolist()
			h2=p_est
		else:
			parameter_full_sample = np.clip(parameter_full_sample, 0.00001, 0.99999)
			hyperparameters=beta.fit(parameter_full_sample,floc=0,fscale=1)
			h1=hyperparameters[0]
			h2=hyperparameters[1]
		exec('{}.{}.hyperparameters={}'.format(model.name,parameter[0],[h1,h2]))


def sample_group_distributions(model):

	parameters=get_parameters_for_model(model)
	number_subjects=model.num_subjects
	model_name=model.name
	for parameter in parameters:
		exec('global distribution; distribution={}.{}.distribution'.format(model_name,parameter))
		exec('global hyperparameters; hyperparameters={}.{}.hyperparameters'.format(model_name,parameter))
		exec('{}.{}.samples=sample_parameters("{}",{},{})'.format(model_name,parameter,distribution,hyperparameters,model.sample_size))


def sample_group_distributions_parallel(params,sample_size):
	all_parameter_samples=[]
	for parameter in params:
		param=parameter[0]
		distribution=parameter[1]
		hyperparameters=parameter[2]
		samples=sample_parameters(distribution,hyperparameters,sample_size)
		all_parameter_samples.append(samples)
	return all_parameter_samples



def get_total_evidence(model):
	number_subjects=model.num_subjects
	model_name=model.name
	group_model_evidence=0
	for subject in range(number_subjects):
		exec('global subjEvidence; subjEvidence={}.subject{}.model_evidence_subject'.format(model_name,subject))
		group_model_evidence+=subjEvidence
	return group_model_evidence



def process_subject(subject,parameter_info,all_data,lik_func,parameter_sample_size):
		data=all_data[subject]

		data=data.reset_index()
		parameter_names=[x[0] for x in parameter_info]
		samples_a=sample_group_distributions_parallel(parameter_info,parameter_sample_size)

		rng=np.arange(0,parameter_sample_size,1)
		
		# compute likelihood
		likelihood=lik_func(samples_a,data,rng)
		likelihood=np.array(likelihood)

		#get cleaned likelihood vector
		likelihood_vector_cleaned,valid_parameter_indices,weights,good_samples=derive_posterior_samples(likelihood,subject)
		 
		# log mean likelihood
		model_evidence=scipy.special.logsumexp(likelihood_vector_cleaned,axis=0)-np.log(good_samples)
		
		#save  data
		subject_name='subject_{}'.format(subject)
		return_dict_info=[[subject]]
		return_dict_info.append([model_evidence])
		
		counter=0
		#resampling
		for param in parameter_names:
			new_samples=each_param_parallel(samples_a[counter],valid_parameter_indices,weights)
			ep=[]
			ep.append(param)
			ep.append(new_samples[0])
			ep.append(new_samples[1])
			ep.append(new_samples[2])
			
			return_dict_info.append(ep)
			counter+=1

		return return_dict_info





############################################################# BUILD MODELS TO BE FIT #########################################################

# parameter_sample_size=8000

# all_models=[]
# # 10. ChoiceBias + full caching
# name_6 = 'MBMC_Breadth2_Depth_mbCache_CB_forget'
# group_parameters_info_m = {
#     'MB_B':       ['gamma', [1, 1]],
#     'MB_depth':   ['beta',  [1, 1]],
#     'MB_breadth': ['beta',  [1, 1]],
#     'breadth2':   ['beta',  [1, 1]],
# 	'mbcache':   ['gamma',  [1, 1]],
# 	'CB':   ['norm',  [0, 5]],
# 	'forget':   ['gamma',  [1, 1]],
# 	'mbcache_noreward':   ['norm',  [0, 5]],
# 	'cache_plan':   ['gamma',  [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution'
# build_model(name_6, likelihood, group_parameters_info_m, number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_mbCache_CB_forget)



# cores_subs=12

# # ############################################################### FIT MODELS #############################################################

# import concurrent.futures
# from multiprocessing.dummy import Pool
# import multiprocessing
# from itertools import repeat,starmap
# import numpy as np
# import time
# import numpy as np
# import pandas as pd
# from scipy.optimize import minimize



# #current_dataset=all_data_input #make sure dataset is correct before running model fitting!!
# current_dataset=sim_df
# models_BICs_record={}
# models_Results_record={}

# #iterate over models
# counter=0
# for model in all_models:
# 	print(model.name)
# 	print('here')
# 	improvement=100 #arbitrary start to ensure while loop starts

# 	#keep sampling until no improvement in iBIC
# 	while improvement>0:
		
# 		#store old_bic for comparison to new_bic
# 		old_bic=model.bic

		
# 		#generate log likelihood for each subject and compute new samples
# 		procs = []
# 		parameter_info=get_parameters_for_model_parallel(model)
# 		print('current_hyperparms:')
# 		print(parameter_info)
# 		parameter_names=[x[0] for x in parameter_info]
# 		parameter_disributions=[x[1] for x in parameter_info]
# 		parameter_sample_size=model.sample_size
# 		subjects=list(np.arange(0,number_subjects,1))
	   
# 		lik_func=model.lik_func
# 		return_dict={}
# 		inputs=zip(subjects,repeat(parameter_info),repeat(current_dataset),
# 			repeat(lik_func),repeat(parameter_sample_size))
# 		start_time = time.time()
# 		if __name__=='__main__':    
# 				pool = Pool(processes=cores_subs)
# 				results=pool.starmap(process_subject, inputs)
# 				pool.close()
# 				pool.join()
				
# 				print('total time: {}'.format(time.time()-start_time))
# 				exec('all_results_{} = [item for item in results]'.format(model.name))
				
# 		print('total time: {}'.format(time.time()-start_time))

# 		exec('all_results=all_results_{}'.format(model.name))
# 		#fit new hyperparameters from full posterior


# 		fit_hyperparameters_parallel(model,parameter_info,all_results,num_subjects)
# 		#compute iBIC
# 		Nparams = 2*len(parameter_names)
# 		print(Nparams)
# 		Ndatapoints = float(number_subjects*num_trials) #total number of datapoints
# 		exec('total_evidence=sum([x[1][0] for x in all_results_{}])'.format(model.name))
# 		print(total_evidence)
# 		new_bic = -2.0*float(total_evidence) + Nparams*np.log(Ndatapoints) # Bayesian Information Criterion
# 		improvement = old_bic - new_bic # compute improvement of fit
		
# 		#only retain evidence and BIC if they improve
# 		if improvement > 0:
# 			model.model_evidence_group=total_evidence
# 			model.bic=new_bic
# 			model.results=all_results
		
# 		# read out latest iteration
# 		print('{}- iBIC old:{}, new: {}\n'.format(model.name, old_bic, new_bic))
# 	models_BICs_record[model.name]=model.bic
# 	models_Results_record[model.name]=model.results
# 	print(models_BICs_record)


# print('current_hyperparms:')
# print(parameter_info)
# print('final param info:')
# print(models_BICs_record)
# print('')




# ################################################### PRINT OUT FITTED PARAMETERS #########################################################################
# # subs=[]
# # zero=[]
# # one=[]
# # two=[]
# sns.set(style='white', font_scale=2.0, palette='Set2')



# # import matplotlib.pyplot as plt
# # import seaborn as sns

# group_parameters_info_m = {
#     'MB_model_sim':       ['gamma', [1, 1]],
#     'MB_depth_sim':   ['beta',  [1, 1]],
#     'MB_breadth1_sim': ['beta',  [1, 1]],
#     'MB_breadth2_sim':   ['beta',  [1, 1]],
# 	'cache_reward_sim':   ['gamma',  [1, 1]],
# 	'cb_sim':   ['norm',  [0, 5]],
# 	'forgetting_cache_sim':   ['gamma',  [1, 1]],
# 	'effect_reward_sim':   ['norm',  [0, 5]],
# 	'cache_plan_sim':   ['gamma',  [1, 1]]
# }


# fitted_df = pd.DataFrame()
# current_results=models_Results_record['MBMC_Breadth2_Depth_mbCache_CB_forget']
# counter=2
# for key in group_parameters_info_m.keys():
# 	group_parameters_info_m[key].append([])
# 	for subject in range(number_subjects):
# 		group_parameters_info_m[key][2].append(current_results[subject][counter][1])
# 	counter+=1
# 	fitted_df['{}'.format(key)]=group_parameters_info_m[key][2]
# 	print(fitted_df)
# fitted_df.to_csv('fitted_sim_data.csv')

fitted_df=pd.read_csv('fitted_sim_data.csv')
fitted_df['sub']= np.arange(1, len(MB_model) + 1).tolist()

# Build a DataFrame of ground‐truths, one row per subject
# (Make sure the order matches the subject‐index in sim_df)
gt_df = pd.DataFrame({
    'sub': np.arange(1, len(MB_model) + 1),   # assume subjects are labeled 1..N
    'MB_model_true': MB_model,
    'MB_depth_true': MB_depth,
    'MB_breadth1_true': MB_breadth1,
	'MB_breadth2_true': MB_breadth2,
	'cache_reward_true': caching_rwd,
	'cb_true': cb,
	'forgetting_cache_true': forgetting_cache,
    'effect_reward_true': caching_no_rwd,
    'cache_plan_true': plan_exec
})

# ─── 2) Extract your fitted‐parameter columns from sim_df ────────────────────────
# Here we assume sim_df has one row per trial. We first compute each subject’s average fitted parameters,
# so that we end up with exactly one row per subject in `fitted_df`. Adjust “fitted_*” names to whatever
# your actual columns are called. For example, if you fitted MB_model to sim_df and named that column "MB_model_fit", etc.
# If your column names differ, just swap them out below.


# ─── 3) Merge ground‐truth and fitted‐→ one DataFrame, keyed on “sub” ────────────
merged = pd.merge(gt_df,
                  fitted_df,
                  on='sub',
                  how='inner')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', font_scale=2.5, palette='Set2')

# … your code to load & merge into `merged` …

# 1) full corr
corr = merged.drop(columns='sub').corr(method='pearson').round(2)

# 2) pick out true vs. fitted block
true_cols   = [c for c in corr.index   if c.endswith('_true')]
fitted_cols = [c for c in corr.columns if c.endswith('_sim')]
subcorr     = corr.loc[true_cols, fitted_cols]

# 3) rename rows & columns to LaTeX labels
label_map = {
    'MB_model':         r"$\beta_{\mathrm{MBMC}}$",
    'MB_depth':         r"$\gamma_{d}$",
    'MB_breadth1':      r"$\tilde{b}_{1}$",
    'MB_breadth2':      r"$\tilde{b}_{2}$",
    'cb':               r"$\beta_{\mathrm{CB}}$",
    'cache_reward': r"$\kappa_{C}$",
    'forgetting_cache':   r"$\gamma_{C}$",
    'effect_reward':       r"$\kappa_{R}$",
    'cache_plan':       r"$\omega_{P}$"
}

def rename_param(name):
    key = name.replace('_true','').replace('_sim','')
    return label_map.get(key, name)

subcorr.index   = [rename_param(n) for n in subcorr.index]
subcorr.columns = [rename_param(n) for n in subcorr.columns]

# 4) strip leading zero in annotations
def fmt(x):
    s = f"{x:.2f}"
    if s.startswith("0"):    return s[1:]
    if s.startswith("-0"):   return "-" + s[2:]
    return s

annot = subcorr.applymap(fmt)

# 5) plot
plt.figure(figsize=(10, 8))
ax=sns.heatmap(
    subcorr,
    annot=annot,
    fmt="",
    cmap='coolwarm',
    vmin=-1, vmax=1,
    linewidths=0.5
)

ax.tick_params(axis='x', rotation=45)  # adjust labelsize if needed
ax.tick_params(axis='y', rotation=45)  # adjust labelsize if needed

plt.xlabel('Fitted parameters')
plt.ylabel('True parameters')
plt.title('Parameter recovery')
plt.tight_layout()
plt.savefig('param_recovery_pearson.png', dpi=300,bbox_inches='tight')
plt.show()
