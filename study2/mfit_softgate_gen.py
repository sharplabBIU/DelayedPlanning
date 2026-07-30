import numpy as np
from scipy.special import comb, logsumexp, expit
np.seterr(divide='ignore', invalid='ignore')

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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
			_p1n = np.minimum(update_probability_planning_success(num_success1, total1, exp_arr), 1.0)
			exp_arr2 = exp_arr2 + _p1n * mb_breadth_arr2

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

def CacheR_CB_4(samples, data, rng_samples):
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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

def CacheR_CB_3(samples, data, rng_samples):
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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


def CacheR_CB_1(samples, data, rng_samples):
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
		(2, 1, 'start'): [1,4], 
		(2, 2, 'images/toothbrush.png'): [1,4], 
		(2, 2, 'images/baby.png'):        [1,4], 
		(2, 3, 'images/backpack.png'):   [1,2], 
		(2, 3, 'images/bowtie.png'):     [0,    0],
		(2, 3, 'images/car.png'):        [0,    0],
		(1, 1, 'start'): [2,4], 
		(1, 2, 'images/toothbrush.png'): [1,2], 
		(1, 2, 'images/baby.png'): [1,2], 
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

