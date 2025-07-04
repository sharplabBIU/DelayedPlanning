#!/usr/bin/env 
# coding: utf-8

# Scripts used to fit models to Multigoal RL task
# Structure of meta script

#    1. Likelihood functions
#    2. Hierarchical model fitting functions
#    3. Loading in empirical data
#    4. Build models to be fit to empirical data
#    5. Fit each model to the empirical data
#    6. Save all fitted parameters and iBICs

# We used a hierarchical Expectation-Maximization procedure called iterative importance sampling to fit the data
# 
# This algorithm iteratively computes iBIC via a sampling procedure. Each iteration of the loop a posterior sample for each subject is derived by 
# weighting the distribution of parameters by their likelihood. These samples at the subject level are concatenated, and then hyperparameters are fit 
# to these distributions. Model evidence at the group level is a sum of subject-level evidence (given that is in log space). 
# Once model evidence (defined by iBIC) does not improve, the iterations terminate. 
# 
# For each subject
# 
# 1. Sample from a prior distribution over $\forall i$ paramters $\theta_{i}$
# 
# 2. Gennerate likelihoods $p(data|\theta_i)$
# 
# 3. Compute posterior distribution over parameters at individual level by $p(\theta)\cdot p(data|\theta) via likelihood-weighted resampling$

# For group:
# 
# 4. Fit new hyperparameters to the full sample (concatenate all individual-level posteriors) then go back to (1) unless iBIC hasn't improved



import os





# ####################################################################### GENERATE SYNTHETIC DATA #########################################################

# #### import pandas as pd
import numpy as np
from numpy.random import beta as betarnd
from numpy.random import gamma as gammarnd
from numpy.random import normal as normalrnd
from random import sample
from random import shuffle
import pandas as pd
import seaborn as sns

#load in empirical data
df=pd.read_csv('lmm_fixed.csv')
print(len(df['sub'].unique()))


dfs=[df[df['sub']==sub].reset_index(drop=True) for sub in pd.read_csv('lmm_fixed.csv')['sub'].unique()]
num_subjects=len(dfs)

lr=list(normalrnd(0, 5,num_subjects))
f=list(normalrnd(0, 5,num_subjects))

MB=list(gammarnd(2, 1,num_subjects))
MF=list(gammarnd(2, 1,num_subjects))



#CREATE SYNTHETIC DATA


# In[10]:
import pandas as pd
from itertools import repeat,starmap
import numpy as np
import time
import scipy
from numpy.random import beta,gamma,chisquare,normal,poisson,uniform,logistic,multinomial,binomial
from scipy.special import logsumexp

#################################################### GET SUBJECT DATA ####################################################################

import pickle

#load in empirical data
df=pd.read_csv('lmm_fixed.csv')
print(len(df['sub'].unique()))


dfs=[df[df['sub']==sub].reset_index(drop=True) for sub in pd.read_csv('lmm_fixed.csv')['sub'].unique()]

sub_ID_names=[x['sub'][10] for x in dfs]
subj_dfs=dfs
all_models=[] #(dfs,num_trials,MB_beta,MF_beta,lr,fr):


number_subjects=len(sub_ID_names)

num_subjects=number_subjects
num_trials=len(df['trial_num'].unique())



# def compute_mbmc_values_vectorized(
# 			key, mb_depth_array, mb_breadth_arr, mb_breadth_arr2,
# 			exp_arr, exp_arr2):

# 		# --- unpack dictionary entries -----------------------------------
# 		# mb_key[key]    = [num_successes, total_rollouts]
# 		# mb_key2[key]   = [num_successes, total_rollouts]   (2-step success)
# 		num_success1, total1 = mb_key[key]
# 		num_success2, total2 = mb_key2[key]

# 		# -----------------------------------------------------------------
# 		# update the running "experience" counters (= cumulative draws)
# 		goal, decision, _ = key
# 		if num_success1 > 0:
# 			exp_arr  += mb_breadth_arr     # add breadth this visit
# 		if num_success2 > 0:
# 			exp_arr2 += mb_breadth_arr2

# 		# -----------------------------------------------------------------
# 		# NEW: exact success probabilities with the threshold property
		





####################################################################### LIKELIHOOD FUNCTIONS #########################################################################
import numpy as np

def MB_actionSeparation(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = np.zeros(len(mb_control))+1

	
	mb_breadth =np.zeros(len(mb_control))+8
	
	
	mb_breadth2 =np.zeros(len(mb_control))+4


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik


def MB_Depth_actionSeparation(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =np.zeros(len(mb_control))+8
	
	
	mb_breadth2 =np.zeros(len(mb_control))+4


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik



def MB_Breadth_actionSeparation(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = np.zeros(len(mb_control))+1

	
	mb_breadth =samples[1][rng_samples]*8
	
	
	mb_breadth2 =samples[2][rng_samples]*4


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik


def MB_oneBreadth_Depth_actionSeparation(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	mb_breadth2=samples[2][rng_samples]*8
	
	


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik


def MB_Breadth_Depth_actionSeparation(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	
	
	mb_breadth2 =samples[3][rng_samples]*4


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
			if decision<2:
				exp_arr2 += mb_breadth_arr2

		# -----------------------------------------------------------------
		# NEW: exact success probabilities with the threshold property
		


		if total1 > 0 and num_success1 > 0:
			p_one = update_probability_planning_success(num_success1, total1, exp_arr)
		else:
			p_one = np.zeros_like(exp_arr)

		if total2 > 0 and num_success2 > 0:
			if decision==2:
				last_exp_c=experiences_action2[(1, 1, 'start')]
				p_prior_success=update_probability_planning_success(2, 4, last_exp_c)
				second_action_threshold = p_prior_success == 1
				exp_arr2[second_action_threshold]+=mb_breadth_arr2[second_action_threshold]
				p_two = update_probability_planning_success(num_success2, total2, exp_arr2)
			else:
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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache1_fullmemory(samples, data, rng_samples):
	from scipy.special import expit
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


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
				for k in keys
				for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]


		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
						)
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key]
						)
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			if goal_outcome==1:
				cached_policy[key][idx, act]=mb_cache
			else:
				cached_policy[key][idx, act]=mb_cache
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
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==2:
				rec = rec_idx2.get(key, far2)               # scalar
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==3:
				rec = rec_idx3.get(key, far3)               # scalar
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action]       *= decay		


			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
		

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory(samples, data, rng_samples):
	from scipy.special import expit
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

	cache_reward=samples[5][rng_samples]


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
				for k in keys
				for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]


		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
						)
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key]
						)
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect
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
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==2:
				rec = rec_idx2.get(key, far2)               # scalar
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action] *= decay
			elif key[1]==3:
				rec = rec_idx3.get(key, far3)               # scalar
				decay = np.exp(-0 * rec)         # shape (S,)
				cached_policy[reduced_key][:, action]       *= decay		

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache2_limitedmemory(samples, data, rng_samples):
	from scipy.special import expit
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

	cache_reward=samples[5][rng_samples]
	forgetting_cache=samples[6][rng_samples]

	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
				for k in keys
				for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]


		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
						)
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key]
						)
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key]
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect
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

	return lik

def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting(samples, data, rng_samples):
	from scipy.special import expit
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


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key] \
					+choice_biases[key]
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect

		
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


def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution(samples, data, rng_samples):
	from scipy.special import expit
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
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}

	cache_plans={(3, 1):np.zeros((sample_size, 2)),
		(3, 2): np.zeros((sample_size, 2)),
		(3, 3): np.zeros((sample_size, 2)),
		(2, 1):np.zeros((sample_size, 2)), 
		(2, 2):np.zeros((sample_size, 2)),
		(2, 3): np.zeros((sample_size, 2)),
	
		(1, 1): np.zeros((sample_size, 2)), 
		(1, 2): np.zeros((sample_size, 2)), 
		(1, 3):   np.zeros((sample_size, 2))
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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			key_plan = (planning_depth_val, decision)
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
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


def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgettingRoutesAndCache(samples, data, rng_samples):
	from scipy.special import expit
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

	forgetting_routes=samples[8][rng_samples]


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		trial_keys=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			trial_keys.append(key)
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key] \
					+choice_biases[key]
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect
		
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

		for key in mb_key.keys():
			if key not in trial_keys:
				experiences_action1[key]*= forgetting_routes
				experiences_action2[key]*= forgetting_routes

		# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
				
	

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_replacement_execution(samples, data, rng_samples):
	from scipy.special import expit
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

	cache_plan =samples[8][rng_samples]




	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	cache_plans={(3, 1):np.zeros((sample_size, 2)),
		(3, 2): np.zeros((sample_size, 2)),
		(3, 3): np.zeros((sample_size, 2)),
		(2, 1):np.zeros((sample_size, 2)), 
		(2, 2):np.zeros((sample_size, 2)),
		(2, 3): np.zeros((sample_size, 2)),
	
		(1, 1): np.zeros((sample_size, 2)), 
		(1, 2): np.zeros((sample_size, 2)), 
		(1, 3):   np.zeros((sample_size, 2))
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		if total1>0:
			mb_breadth_arr_current=mb_breadth_arr/total1
			mb_breadth_arr_current=np.clip(mb_breadth_arr_current, 0.0, 1.0)
			exp_arr=exp_arr/total1
			if num_success1 > 0:
				exp_arr  = 1-(1-exp_arr)*(1-mb_breadth_arr_current)     # add breadth this visit
				exp_arr = exp_arr*total1
				p_one = update_probability_planning_success(num_success1,total1,exp_arr)
		else:
			p_one = np.zeros_like(exp_arr)


		if total2>0:
			mb_breadth_arr_current2=mb_breadth_arr2/total2
			mb_breadth_arr_current2=np.clip(mb_breadth_arr_current2, 0.0, 1.0)
			threshold2=(total2-(num_success2-1))/total2

			exp_arr2=exp_arr2/total2
		
			if num_success2 > 0:
				exp_arr2  = 1-(1-exp_arr2)*(1-mb_breadth_arr_current2)     # add breadth this visit
				exp_arr2 = exp_arr2*total2
				p_two = update_probability_planning_success(num_success2,total2,exp_arr2)

	
			
				
				
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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			key_plan = (planning_depth_val, decision)
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
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


def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_sequentialactionsearch(samples, data, rng_samples):
	from scipy.special import expit
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


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		goal, decision, state = key
		if num_success1 > 0:
			exp_arr  += mb_breadth_arr     # add breadth this visit
		# if num_success2 > 0:
		# 	if decision<2:
		# 		exp_arr2 += mb_breadth_arr2

		# -----------------------------------------------------------------
		# NEW: exact success probabilities with the threshold property
		


		if total1 > 0 and num_success1 > 0:
			p_one = update_probability_planning_success(num_success1, total1, exp_arr)
		else:
			p_one = np.zeros_like(exp_arr)

		if total2 > 0 and num_success2 > 0:
			initial_state_first_action=(goal, decision, state)
			last_exp_c=experiences_action1[initial_state_first_action]
			n_succ_past,n_total=mb_key[(goal, decision, state)]
			p_prior_success=update_probability_planning_success(n_succ_past, n_total, last_exp_c)
			first_action_threshold = p_prior_success == 1
			exp_arr2[first_action_threshold]+=mb_breadth_arr2[first_action_threshold]
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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					+cached_policy[key] \
					+choice_biases[key]
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						+cached_policy[key] \
					+choice_biases[key]
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect

		
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

def MB_Breadth_Depth_actionSeparation_noMBLearn(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	
	
	mb_breadth2 =samples[3][rng_samples]*4


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}


	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
			exp_arr  = mb_breadth_arr     # add breadth this visit
		if num_success2 > 0:
			exp_arr2 = mb_breadth_arr2

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

	# loop over trials
	trials = np.sort(data['trial_num'].unique())
	for trial in trials:
		df_temp = data[data['trial_num'] == trial].reset_index(drop=True)
		actions = df_temp['choice_numeric'].values
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		recent_keys=[]

		for decision in (1, 2, 3):
			key = (planning_depth_val, decision, current_states[decision - 1])
			

			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
					  )
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					 )
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
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
			other_act=int((act-1)*-1)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			if goal_outcome==0:
				goal_outcome=-1
			

			# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
			
	

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_MF(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	
	
	mb_breadth2 =samples[3][rng_samples]*4


	choice_bias =samples[4][rng_samples]


	mf_learning_rate=samples[5][rng_samples]
	mf_beta=samples[6][rng_samples]


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						
					+choice_biases[key] \
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					
					+choice_biases[key] \
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					 
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						
					+choice_biases[key] \
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					  
			
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

			# cache_effect=mb_cache+(cache_reward*goal_outcome)
			# cached_policy[key][idx, act]=cache_effect

			if goal_outcome == -1:
				pe = reward - learned_policy[key][idx, act]
				learned_policy[key][idx, act] += mf_learning_rate * pe
			else:
				pe = (reward+4) - learned_policy[key][idx, act]
				learned_policy[key][idx, act] += mf_learning_rate * pe 

		
			key = (planning_depth_val, decision, current_states[decision - 1],act)
			if decision==1:
				recent_keys1=push_recent_key(recent_keys1,key)
			elif decision==2:
				recent_keys2=push_recent_key(recent_keys2,key)
			elif decision==3:
				recent_keys3=push_recent_key(recent_keys3,key)

		# # Recency index: 0 = newest, 1 = 2nd-newest, …
		# rec_idx = {k: r for r, k in enumerate(reversed(recent_keys1))}
		# far = len(recent_keys1) + 1      # “never seen” sentinel

		# rec_idx2 = {k: r for r, k in enumerate(reversed(recent_keys2))}
		# far2 = len(recent_keys2) + 1      # “never seen” sentinel

		# rec_idx3 = {k: r for r, k in enumerate(reversed(recent_keys3))}
		# far3 = len(recent_keys3) + 1      # “never seen” sentinel

		# for key in keys_caching.keys():
		# 	reduced_key=key[:-1]
		# 	action=key[3]
		# 	if key[1]==1:
		# 		rec = rec_idx.get(key, far)               # scalar
		# 		decay = np.exp(-forgetting_cache * rec)         # shape (S,)
		# 		cached_policy[reduced_key][:, action] *= decay
		# 	elif key[1]==2:
		# 		rec = rec_idx2.get(key, far2)               # scalar
		# 		decay = np.exp(-forgetting_cache * rec)         # shape (S,)
		# 		cached_policy[reduced_key][:, action] *= decay
		# 	elif key[1]==3:
		# 		rec = rec_idx3.get(key, far3)               # scalar
		# 		decay = np.exp(-forgetting_cache * rec)         # shape (S,)
		# 		cached_policy[reduced_key][:, action]       *= decay		


		# lr_current=np.multiply(lr_start,np.exp(-1*lr_decay*cache_experiences[key]))
				
	

	return lik


def MB_Breadth_Depth_actionSeparation_MBcache_forgetting_MF(samples, data, rng_samples):
	from scipy.special import expit
	import numpy as np
	from scipy.special import comb
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	mb_control=samples[0][rng_samples]
	discount_rate = samples[1][rng_samples]

	
	mb_breadth =samples[2][rng_samples]*8
	
	
	mb_breadth2 =samples[3][rng_samples]*4




	mf_learning_rate=samples[4][rng_samples]
	mf_beta=samples[5][rng_samples]


	# initialize likelihood
	lik = np.zeros(sample_size)
	
	# prepare dictionaries for all possible (goal, decision, state) combos
	# prepare dictionaries for all possible (goal, decision, state) combos
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			p2, v2t, v2r, p1, v1t, v1r, p0, v0t, v0r, experiences_action1[key],experiences_action2[key] = \
				compute_mbmc_values_vectorized(key,  5,mb_breadth, mb_breadth2,experiences_action1[key],experiences_action2[key])
			
			last_key=key
			last_exp=experiences_action2[key]
			probability_mb1[key]     = p2
			optimal_policy_1[key]    = np.stack([v2t, v2r], axis=1)
			probability_mb2[key]     = p1
			optimal_policy_2[key]    = np.stack([v1t, v1r], axis=1)
			probability_mb_none[key] = p0
			optimal_policy_3[key]    = np.stack([v0t, v0r], axis=1)

			# integrated Q-values
			Q_both = (optimal_policy_1[key]*mb_control.reshape(sample_size,1) \
						
					
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			Q_one = (optimal_policy_2[key]*mb_control.reshape(sample_size,1) \
					
					
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					 
			
			logp_one = Q_one[np.arange(sample_size), actions[decision - 1]] \
					   - logsumexp(Q_one, axis=1)

			Q_none = (optimal_policy_3[key]*mb_control.reshape(sample_size,1) \
						
					
					+ learned_policy[key]*mf_beta.reshape(sample_size,1))
					  
			
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
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

			# cache_effect=mb_cache+(cache_reward*goal_outcome)
			# cached_policy[key][idx, act]=cache_effect

			if goal_outcome == -1:
				pe = reward - learned_policy[key][idx, act]
				learned_policy[key][idx, act] += mf_learning_rate * pe
			else:
				pe = (reward+4) - learned_policy[key][idx, act]
				learned_policy[key][idx, act] += mf_learning_rate * pe 

		
			key = (planning_depth_val, decision, current_states[decision - 1],act)
			if decision==1:
				recent_keys1=push_recent_key(recent_keys1,key)
			elif decision==2:
				recent_keys2=push_recent_key(recent_keys2,key)
			elif decision==3:
				recent_keys3=push_recent_key(recent_keys3,key)


	return lik

def CacheR_CB(samples, data, rng_samples):
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	# mb_control=samples[0][rng_samples]
	
	
	# mb_depth = samples[1][rng_samples] * 4
	# mb_breadth =samples[2][rng_samples]* 9
	choice_bias = samples[0][rng_samples]
	mb_cache = samples[1][rng_samples]
	forgetting_cache = samples[2][rng_samples]
	cache_reward = samples[3][rng_samples]
	# initialize likelihood
	lik = np.zeros(sample_size)
	# prepare dictionaries for all possible (goal, decision, state) combos
	# MB key: base probabilities and initial experience (second element unused after vectorizing)
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}


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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			

			# integrated Q-values
			Q_both = (cached_policy[key] \
					+choice_biases[key])
					
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			
			lik += logp_both

			# update learned policy
			idx = np.arange(sample_size)
			act = actions[decision - 1]

			
			recent_acts.append(act)
			other_act=int((act-1)*-1)
			recent_other_acts.append(other_act)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect

		
		
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
	return lik

def CacheR_CB(samples, data, rng_samples):
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	# mb_control=samples[0][rng_samples]
	
	
	# mb_depth = samples[1][rng_samples] * 4
	# mb_breadth =samples[2][rng_samples]* 9
	mb_cache = samples[0][rng_samples]
	forgetting_cache = samples[1][rng_samples]
	cache_reward = samples[2][rng_samples]
	# initialize likelihood
	lik = np.zeros(sample_size)
	# prepare dictionaries for all possible (goal, decision, state) combos
	# MB key: base probabilities and initial experience (second element unused after vectorizing)
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
	}
	
	
	
	keys = list(mb_key.keys())
	learned_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	cached_policy = {key: np.zeros((sample_size, 2)) for key in keys}
	keys_caching = {(*k, s): np.zeros((sample_size, 2))
                  for k in keys
                  for s in (0, 1)}

	choice_biases = {key: np.zeros((sample_size, 2)) for key in keys}
	for key in keys:
		choice_biases[key][:, 0] = 1
	
	transitions = {
	'start': ['space','toothbrush', 'baby'],
	'baby': ['space','bowtie','backpack'],
	'toothbrush': ['space','backpack', 'car'],
	'backpack': ['space','lamp', 'zebra'],
	'bowtie': ['space','knight', 'lamp'],
	'car': ['space','lamp', 'cat']}


	experiences_action1 = {key: np.zeros(sample_size) for key in keys}
	experiences_action2 = {key: np.zeros(sample_size) for key in keys}
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			

			# integrated Q-values
			Q_both = (cached_policy[key])
					
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)


			# mixture log-likelihood
			
			lik += logp_both

			# update learned policy
			idx = np.arange(sample_size)
			act = actions[decision - 1]

			
			recent_acts.append(act)
			other_act=int((act-1)*-1)
			recent_other_acts.append(other_act)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

			cache_effect=mb_cache+(cache_reward*goal_outcome)
			cached_policy[key][idx, act]=cache_effect

		
		
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
	return lik


def CacheR_CB(samples, data, rng_samples):
	np.seterr(divide='ignore')
	sample_size = len(rng_samples)

	# extract parameters
	# mb_control=samples[0][rng_samples]
	
	
	# mb_depth = samples[1][rng_samples] * 4
	# mb_breadth =samples[2][rng_samples]* 9
	choice_bias = samples[0][rng_samples]

	# initialize likelihood
	lik = np.zeros(sample_size)
	# prepare dictionaries for all possible (goal, decision, state) combos
	# MB key: base probabilities and initial experience (second element unused after vectorizing)
	mb_key = {
		(3, 1, 'start'):           [1, 8], 
		(3, 2, 'images/toothbrush.png'): [1,4], 
		(3, 2, 'images/baby.png'):        [0,    0],
		(3, 3, 'images/car.png'):        [1,2], 
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [2,8], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [4,8], 
		(1, 2, 'images/toothbrush.png'): [2,4], 
		(1, 2, 'images/baby.png'):        [2,4], 
		(1, 3, 'images/backpack.png'):   [1,2], 
		(1, 3, 'images/bowtie.png'):     [1,2], 
		(1, 3, 'images/car.png'):        [1,2], 
	}
	
	mb_key2 = {
		(3, 1, 'start'):           [0, 0],
		(3, 2, 'images/toothbrush.png'): [0.0, 0],
		(3, 2, 'images/baby.png'):        [0.0,    0],
		(3, 3, 'images/car.png'):        [0.0,  0],
		(3, 3, 'images/backpack.png'):   [0,    0],
		(3, 3, 'images/bowtie.png'):     [0,    0],
		(2, 1, 'start'):           [1,4], 
		(2, 2, 'images/toothbrush.png'): [0.0, 0],
		(2, 2, 'images/baby.png'):        [0.0, 0],
		(2, 3, 'images/backpack.png'):   [0.0,  0],
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'):           [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'):        [1,2], 
		(1, 3, 'images/backpack.png'):   [0,  0],
		(1, 3, 'images/bowtie.png'):     [0,  0],
		(1, 3, 'images/car.png'):        [0,  0],
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
	cache_experiences = {key: np.zeros(sample_size) for key in keys}

	probability_mb1 = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_1 = {key: np.zeros((sample_size, 2)) for key in keys}
	probability_mb2 = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_2 = {key: np.zeros((sample_size, 2)) for key in keys}
	probability_mb_none = {key: np.zeros(sample_size) for key in keys}
	optimal_policy_3 = {key: np.zeros((sample_size, 2)) for key in keys}


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
		trial_within_goal=df_temp['trial_num_within_goal'].values[0]
		last_actions = df_temp['choice_numeric_last'].values
		RT = df_temp['RT'].values
		goal_outcome = df_temp['got_to_goal'].values[0]
		planning_depth_val = int(df_temp['planning_depth'].values[0])
		current_states = df_temp['current_state'].values

		# reward from subsequent choices (as in original)
		sum_reward = (df_temp['choice_numeric'][0:] == 2).sum()
		reward = sum_reward
		last_key=(planning_depth_val, 1, current_states[1 - 1])
		last_exp=experiences_action2[last_key]
		
		recent_acts=[]
		recent_other_acts=[]
		for decision in (1, 2, 3):
			

			key = (planning_depth_val, decision, current_states[decision - 1])
			# vectorized MBMC computation
			
			

			# integrated Q-values
			Q_both = (choice_biases[key])
					
			
			logp_both = Q_both[np.arange(sample_size), actions[decision - 1]] \
						- logsumexp(Q_both, axis=1)

			

			
			lik += logp_both

			# update learned policy
			idx = np.arange(sample_size)
			act = actions[decision - 1]

			
			recent_acts.append(act)
			other_act=int((act-1)*-1)
			recent_other_acts.append(other_act)
			

			sum_reward = (df_temp['choices_numeric'][:] == 2).sum()
			reward = sum_reward
			
			if goal_outcome==0:
				goal_outcome=-1

		
		
			key = (planning_depth_val, decision, current_states[decision - 1],act)
			if decision==1:
				recent_keys1=push_recent_key(recent_keys1,key)
			elif decision==2:
				recent_keys2=push_recent_key(recent_keys2,key)
			elif decision==3:	
				recent_keys3=push_recent_key(recent_keys3,key)
	return lik

############################################### DEFINE FUNCTIONS TO BE USED IN HIERARCHICAL MODELLING ###############################################################


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





def get_parameters_for_model_parallel_MLE(model):
	parameters=[]

	for var in vars(model):
		exec('global x; x={}.{}'.format(model.name,var))
		if type(x)==model.groupParams:
			if var!='params':
				param_info=[]
				param_info.append(var)
				exec('param_info.append({}.{}.initial_value)'.format(model.name,var))
				exec('param_info.append({}.{}.bounds)'.format(model.name,var))
				parameters.append(param_info)

	return parameters


def build_model_MLE(name,likelihood,group_parameters_info,number_subjects,sample_size):
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
		exec('{}.{}.bounds={}'.format(name,parameter,group_parameters_info[parameter][2]))
		exec('{}.{}.initial_value={}'.format(name,parameter,group_parameters_info[parameter][1]))

	for sub in range(number_subjects):
		exec('{}.subject{}={}.subjFit()'.format(name,sub,name))
		for parameter in group_parameters_info:
			exec('{}.subject{}.{}={}.subject{}.subjParams()'.format(name,sub,parameter,name,sub))


def process_subject_MLE(subject, parameter_info, all_data, lik_func, parameter_sample_size):
	import numpy as np
	import pandas as pd
	from scipy.optimize import minimize

	# Data preprocessing
	data = all_data[subject]
	data = data.reset_index()

	# Define the objective function to minimize (negative log likelihood)
	def objective(params):
		# Assuming lik_func returns the log likelihood
		neg_log_likelihood = -lik_func(params, data)
		return neg_log_likelihood

	# Initial parameter estimates
	initial_params = [x[1] for x in parameter_info]  # Assuming the second element is the initial estimate

	# Bounds for parameters (if any)
	bounds = [x[2] if len(x) > 2 else None for x in parameter_info]  # Assuming the third element are the bounds

	# Perform the optimization
	result = minimize(objective, initial_params, bounds=bounds)

	# Extract the best fitting parameters
	best_params = result.x

	# Compute the log likelihood with the best-fitting parameters
	log_likelihood_at_best_params = lik_func(best_params, data)

	# Assuming you have a way to compute the model evidence (if needed, not shown here)
	# model_evidence = ...

	return_dict_info = [[subject], [log_likelihood_at_best_params]]

	# Add best-fitting values for each parameter
	for param_value in best_params:
		return_dict_info.append([param_value])

	return return_dict_info





############################################################# BUILD MODELS TO BE FIT #########################################################

#General parameters for fitting
parameter_sample_size=8000
import multiprocessing

cores_total = multiprocessing.cpu_count()
cores_subs = max(1, cores_total - 2)  # leave 2 cores for OS / overhead

# ========== 1. MB_actionSeparation =====================================
# name_1 = 'MBMC_optimal'
# group_parameters_info_1 = {
#     'MB_B': ['gamma', [1, 1]]              # mb_control
# }
# likelihood = 'MB_actionSeparation'
# build_model(name_1, likelihood, group_parameters_info_1,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_optimal)


# # ========== 2. MB_Depth_actionSeparation ==============================
# name_2 = 'MBMC_Depth'
# group_parameters_info_2 = {
#     'MB_B':     ['gamma', [1, 1]],
#     'MB_depth': ['beta',  [1, 1]]          # discount_rate
# }
# likelihood = 'MB_Depth_actionSeparation'
# build_model(name_2, likelihood, group_parameters_info_2,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Depth)


# # ========== 3. MB_Breadth_actionSeparation ============================
# name_3 = 'MBMC_Breadth2'
# group_parameters_info_3 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]],
#     'breadth2':    ['beta',  [1, 1]]
# }
# likelihood = 'MB_Breadth_actionSeparation'
# build_model(name_3, likelihood, group_parameters_info_3,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2)


# # ========== 4. MB_oneBreadth_Depth_actionSeparation ===================
# name_4 = 'MBMC_Breadth1'
# group_parameters_info_4 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_depth':    ['beta',  [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]]       # same breadth for both steps
# }
# likelihood = 'MB_oneBreadth_Depth_actionSeparation'
# build_model(name_4, likelihood, group_parameters_info_4,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth1)


# # ========== 5. MB_Breadth_Depth_actionSeparation ======================
# name_5 = 'MBMC_Breadth2_Depth'
# group_parameters_info_5 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_depth':    ['beta',  [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]],
#     'breadth2':    ['beta',  [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation'
# build_model(name_5, likelihood, group_parameters_info_5,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth)


# # ========== 6. MB_Breadth_Depth_actionSeparation_MBcache1_fullmemory ==
# name_6 = 'MBMC_Breadth2_Depth_CC'
# group_parameters_info_6 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_depth':    ['beta',  [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]],
#     'breadth2':    ['beta',  [1, 1]],
#     'mbcache':     ['gamma', [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache1_fullmemory'
# build_model(name_6, likelihood, group_parameters_info_6,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CC)


# # ========== 7. MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory ==
# name_7 = 'MBMC_Breadth2_Depth_CCR'
# group_parameters_info_7 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_depth':    ['beta',  [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]],
#     'breadth2':    ['beta',  [1, 1]],
#     'mbcache':     ['gamma', [1, 1]],
#     'cache_reward':['norm',  [0, 5]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory'
# build_model(name_7, likelihood, group_parameters_info_7,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CCR)

# # ========== 7. MB_Breadth_Depth_actionSeparation_MBcache2_fullmemory ==
# name_7 = 'MBMC_Breadth2_Depth_CCRF'
# group_parameters_info_7 = {
#     'MB_B':        ['gamma', [1, 1]],
#     'MB_depth':    ['beta',  [1, 1]],
#     'MB_breadth':  ['beta',  [1, 1]],
#     'breadth2':    ['beta',  [1, 1]],
#     'mbcache':     ['gamma', [1, 1]],
#     'cache_reward':['norm',  [0, 5]],
# 	'forget':['gamma',  [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache2_limitedmemory'
# build_model(name_7, likelihood, group_parameters_info_7,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CCRF)



# # ========== 8. MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting =
# name_8 = 'MBMC_Breadth2_Depth_CCRF_CB'
# group_parameters_info_8 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting'
# build_model(name_8, likelihood, group_parameters_info_8,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CCRF_CB)



# # ========== win. MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_Exec=

# name_X = 'MBMC_Breadth2_Depth_CCRF_CB_PE'
# group_parameters_info_8 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]],
# 	'cache_plan': ['gamma',  [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_execution'
# build_model(name_X, likelihood, group_parameters_info_8,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CCRF_CB_PE)


# # ========== 9. MBcache + CB + forgetR ================================
# name_9 = 'MBMCF_Breadth2_Depth_CCRF_CB'
# group_parameters_info_9 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]],
#     'forgetR':      ['gamma', [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgettingRoutesAndCache'
# build_model(name_9, likelihood, group_parameters_info_9,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMCF_Breadth2_Depth_CCRF_CB)


# ==========10. cache replacement variant =============================
# name_10 = 'MBMCreplace_Breadth2_Depth_CCRF_CB_PE'
# group_parameters_info_10 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]],
#     'cache_plan':      ['gamma', [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_replacement_execution'
# build_model(name_10, likelihood, group_parameters_info_10,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMCreplace_Breadth2_Depth_CCRF_CB_PE)


# # ==========11. sequential-action-search variant ======================
# name_11 = 'MBMCsequential_Breadth2_Depth_CCRF_CB'
# group_parameters_info_11 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_sequentialactionsearch'
# build_model(name_11, likelihood, group_parameters_info_11,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMCsequential_Breadth2_Depth_CCRF_CB)

# # ==========11. sequential-action-search variant ======================
# name_12 = 'MBMC_Breadth2_Depth_CB_MF'
# group_parameters_info_11 = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'CB':           ['norm',  [0, 5]],
# 	'lr': ['beta',  [1, 1]],
# 	'mf_beta': ['gamma',  [1, 1]]
# }
# likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_CB_forgetting_MF'
# build_model(name_12, likelihood, group_parameters_info_11,
#             number_subjects, parameter_sample_size)
# all_models.append(MBMC_Breadth2_Depth_CB_MF)

# ==========11. sequential-action-search variant ======================
name_12 = 'MBMC_Breadth2_Depth_MF'
group_parameters_info_11 = {
    'MB_B':         ['gamma', [1, 1]],
    'MB_depth':     ['beta',  [1, 1]],
    'MB_breadth':   ['beta',  [1, 1]],
    'breadth2':     ['beta',  [1, 1]],
	'lr': ['beta',  [1, 1]],
	'mf_beta': ['gamma',  [1, 1]]
}
likelihood = 'MB_Breadth_Depth_actionSeparation_MBcache_forgetting_MF'
build_model(name_12, likelihood, group_parameters_info_11,
            number_subjects, parameter_sample_size)
all_models.append(MBMC_Breadth2_Depth_MF)

# # ==========13. CacheR_CB (CB + cache + forgetting) ===================
# # NOTE: ensure the four-parameter function is named uniquely
# name_13 = 'CCRF_CB'
# group_parameters_info_13 = {
#     'CB':           ['norm',  [0, 5]],
#     'mbcache':      ['gamma', [1, 1]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]]
# }
# likelihood = 'CacheR_CB'   # 4-parameter version
# build_model(name_13, likelihood, group_parameters_info_13,
#             number_subjects, parameter_sample_size)
# all_models.append(CCRF_CB)


# # ==========14. CacheR_CB (cache only) ================================
# # rename the 3-parameter function if needed
# name_14 = 'CCRF'
# group_parameters_info_14 = {
#     'mbcache':      ['gamma', [1, 1]],
#     'forgetC':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]]
# }
# likelihood = 'CacheR_CB'   # 3-parameter version
# build_model(name_14, likelihood, group_parameters_info_14,
#             number_subjects, parameter_sample_size)
# all_models.append(CCRF)


# # ==========15. CacheR_CB (CB only baseline) ==========================
# # rename the 1-parameter function if needed
# name_15 = 'CB'
# group_parameters_info_15 = {
#     'CB': ['norm', [0, 5]]
# }
# likelihood = 'CacheR_CB'   # 1-parameter version
# build_model(name_15, likelihood, group_parameters_info_15,
#             number_subjects, parameter_sample_size)
# all_models.append(CB)

# 
############################################################### FIT MODELS #############################################################

import concurrent.futures
from multiprocessing.dummy import Pool
import multiprocessing
from itertools import repeat,starmap
import numpy as np
import time
import numpy as np
import pandas as pd
from scipy.optimize import minimize



#current_dataset=all_data_input #make sure dataset is correct before running model fitting!!
current_dataset=subj_dfs

models_BICs_record={}
models_Results_record={}
#iterate over models
counter=0

for model in all_models:
	print(model.name)
	improvement=100 #arbitrary start to ensure while loop starts

	#keep sampling until no improvement in iBIC
	while improvement>0:
		
		#store old_bic for comparison to new_bic
		old_bic=model.bic

		
		#generate log likelihood for each subject and compute new samples
		procs = []
		parameter_info=get_parameters_for_model_parallel(model)
		print('current_hyperparms:')
		print(parameter_info)
		parameter_names=[x[0] for x in parameter_info]
		parameter_disributions=[x[1] for x in parameter_info]
		parameter_sample_size=model.sample_size
		subjects=list(np.arange(0,number_subjects,1))
	   
		lik_func=model.lik_func
		return_dict={}
		inputs=zip(subjects,repeat(parameter_info),repeat(current_dataset),
			repeat(lik_func),repeat(parameter_sample_size))
		start_time = time.time()
		if __name__=='__main__':    
				pool = Pool(processes=cores_subs)
				results=pool.starmap(process_subject, inputs)
				pool.close()
				pool.join()
				
				print('total time: {}'.format(time.time()-start_time))
				exec('all_results_{} = [item for item in results]'.format(model.name))
				
		print('total time: {}'.format(time.time()-start_time))

		exec('all_results=all_results_{}'.format(model.name))
		#fit new hyperparameters from full posterior


		fit_hyperparameters_parallel(model,parameter_info,all_results,num_subjects)
		#compute iBIC
		Nparams = 2*len(parameter_names)
		print(Nparams)
		Ndatapoints = float(number_subjects*num_trials) #total number of datapoints
		exec('total_evidence=sum([x[1][0] for x in all_results_{}])'.format(model.name))
		print(total_evidence)
		new_bic = -2.0*float(total_evidence) + Nparams*np.log(Ndatapoints) # Bayesian Information Criterion
		improvement = old_bic - new_bic # compute improvement of fit
		
		#only retain evidence and BIC if they improve
		if improvement > 0:
			model.model_evidence_group=total_evidence
			model.bic=new_bic
			model.results=all_results
		
		# read out latest iteration
		print('{}- iBIC old:{}, new: {}\n'.format(model.name, old_bic, new_bic))
	models_BICs_record[model.name]=model.bic
	models_Results_record[model.name]=model.results
	print(models_BICs_record)


#save results
import pickle

# with open('model_BICs_final.pkl', 'wb') as f:
# 	pickle.dump(models_BICs_record, f)
# with open('model_results.pkl', 'wb') as f:
#     pickle.dump(models_Results_record, f)

print('current_hyperparms:')
print(parameter_info)
print('final param info:')
print(models_BICs_record)
print('')




################################################### PRINT OUT FITTED PARAMETERS #########################################################################
subs=[]
zero=[]
one=[]
two=[]

# import matplotlib.pyplot as plt
# import seaborn as sns

# group_parameters_info_m = {
#     'MB_B':         ['gamma', [1, 1]],
#     'MB_depth':     ['beta',  [1, 1]],
#     'MB_breadth':   ['beta',  [1, 1]],
#     'breadth2':     ['beta',  [1, 1]],
#     'mbcache':      ['gamma', [1, 1]],
#     'CB':           ['norm',  [0, 5]],
#     'forget':      ['gamma', [1, 1]],
#     'cache_reward': ['norm',  [0, 5]],
# 	'cache_plan': ['gamma',  [1, 1]]
# }

# # with open('model_results.pkl', 'rb') as f:
# #     models_Results_record = pickle.load(f)
# d = pd.DataFrame()
# current_results=models_Results_record['MBMC_Breadth2_Depth_CCRF_CB_PE']
# counter=2
# for key in group_parameters_info_m.keys():
# 	group_parameters_info_m[key].append([])
# 	for subject in range(number_subjects):
# 		group_parameters_info_m[key][2].append(current_results[subject][counter][1])
# 	counter+=1 
# 	np.save('{}_exec'.format(key),group_parameters_info_m[key][2])
# 	d['{}'.format(key)]=group_parameters_info_m[key][2]

