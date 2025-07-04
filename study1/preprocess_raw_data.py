import pandas as pd
import numpy as np
import numpy
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import sem
import itertools
# from statsmodels.tsa.api import SimpleExpSmoothing
# from scipy.optimize import curve_fit


num_decisions_to_consider=20

q_cols=['key_resp_3.keys','key_resp_13.keys','key_resp_14.keys','key_resp_15.keys','key_resp_16.keys','key_resp_25.keys','key_resp_26.keys','key_resp_27.keys','key_resp_28.keys','key_resp_29.keys','key_resp_30.keys','key_resp_31.keys','key_resp_32.keys','key_resp_33.keys','key_resp_34.keys','key_resp_35.keys']
# q_cols2=['key_resp_68.keys','key_resp_70.keys','key_resp_71.keys','key_resp_73.keys','key_resp_74.keys','key_resp_75.keys','key_resp_76.keys','key_resp_77.keys']

reverse_counters=[1,3,8,10,11]

reverse_dict={1:5,2:4,3:3,4:2,5:1}

subs=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6') ]

timepoints_tracker=[['1']*num_decisions_to_consider+['2']*num_decisions_to_consider+['3']*num_decisions_to_consider]*3*len(subs)
timepoints_tracker=list(itertools.chain.from_iterable(timepoints_tracker))
print(len(timepoints_tracker))


csv_lines=[['sub','tvalue','pvalue']]

planning_from_map={'bowtie_lamp':'right',
'backpack_lamp':'left',
'car_lamp':'right',
'start_cat':'right',
'toothbrush_cat':'left',
'car_cat':'left',
'backpack_zebra':'right',
'toothbrush_zebra':'right',
'baby_zebra':'left'
}

rts_zebra=[]
rts_lamp=[]
rts_bending=[]
rts_cat=[]
sub_numbers1=[]
sub_numbers2=[]
sub_numbers3=[]

delayed_planning_cats=[]
delayed_planning_lamps=[]
delayed_planning_zebras=[]


optimal_delayed_planning_cats=[]
optimal_delayed_planning_lamps=[]
optimal_delayed_planning_zebras=[]

optimal_control_choice_cats=[]
optimal_control_choice_lamps=[]
optimal_control_choice_zebras=[]

optimal_delayed_planning_cats_last=[]
optimal_delayed_planning_lamps_last=[]
optimal_delayed_planning_zebras_last=[]

cached_or_not_all=[]

control_reg_cats=[]
control_reg_lamps=[]
control_reg_zebras=[]

cached_or_not_cats=[]
cached_or_not_zebras=[]
cached_or_not_lamps=[]

current_state_cats=[]
current_state_zebras=[]
current_state_lamps=[]

goal_switch_cats=[]
goal_switch_lamps=[]
goal_switch_zebras=[]

raw_action_cats=[]
raw_action_zebras=[]
raw_action_lamps=[]

trial_num_cats=[]
trial_num_lamps=[]
trial_num_zebras=[]

eligible_cats=[]
eligible_zebras=[]
eligible_lamps=[]

trial_num_cats_rel=[]
trial_num_lamps_rel=[]
trial_num_zebras_rel=[]

got_to_goal_cats=[]
got_to_goal_zebras=[]
got_to_goal_lamps=[]


got_to_goal_cats_last=[]
got_to_goal_zebras_last=[]
got_to_goal_lamps_last=[]

choices_cats=[]
choices_lamps=[]
choices_zebras=[]

pswq_scores_cats=[]
pswq_scores_zebras=[]
pswq_scores_lamps=[]

zebra_dict={1:'right',2:'left',3:'left',4:'right'}
decision_answers=['plan1_response.keys',
'plan2_response.keys',
'plan3_response.keys',
'plan4_response.keys']
image_arrived='image_arrived3'
sub_num=1

from scipy import stats

# Define data structure to store results
results = {'sub': [], 't-value': [], 'p-value': []}

# Keep track of previous outcomes for each subject
prev_outcome = {sub: {'cat': {1: None, 2: None, 3: None},
					  'lamp': {1: None, 2: None, 3: None},
					  'zebra': {1: None, 2: None, 3: None}} for sub in subs}

# Keep track of whether previous trial was a consecutive trial
prev_trial_consecutive = {sub: {'cat': {1: False, 2: False, 3: False},
								'lamp': {1: False, 2: False, 3: False},
								'zebra': {1: False, 2: False, 3: False}} for sub in subs}

prev_trial_nonconsecutive = {sub: {'cat': {1: False, 2: False, 3: False},
								'lamp': {1: False, 2: False, 3: False},
								'zebra': {1: False, 2: False, 3: False}} for sub in subs}
trial_type='r2'
# x=['55d22025cc2b18000c0b9d9c_thisExp_2023-05-28_10h07.02.505.csv']
for sub in subs:
	print('{} csv file is sub NUM : {}'.format(sub,sub_num))

	


	zebra_correct_mean=[]
	zebra_labels_correct=[]
	zebra_labels_incorrect=[]
	zebra_correct_std=[]
	zebra_incorrect_mean=[]
	zebra_incorrect_std=[]
	zebra_correct_num=[]
	zebra_incorrect_num=[]

	rts_zebra_current=[]
	rts_lamp_current=[]
	rts_bending_current=[]
	rts_cat_current=[]
	delayed_planning_cat=[]
	delayed_planning_lamp=[]
	delayed_planning_zebra=[]

	optimal_delayed_planning_cat=[]
	optimal_delayed_planning_lamp=[]
	optimal_delayed_planning_zebra=[]

	optimal_control_choice_cat=[]
	optimal_control_choice_lamp=[]
	optimal_control_choice_zebra=[]

	cached_or_not=[]

	got_to_goal_cat=[]
	got_to_goal_zebra=[]
	got_to_goal_lamp=[]

	raw_action_cat=[]
	raw_action_zebra=[]
	raw_action_lamp=[]

	got_to_goal_cat_last=[0]
	got_to_goal_zebra_last=[0]
	got_to_goal_lamp_last=[0]

	trial_num_cat=[]
	trial_num_lamp=[]
	trial_num_zebra=[]

	trial_num_cat_rel=[]
	trial_num_lamp_rel=[]
	trial_num_zebra_rel=[]

	current_state_cat=[]
	current_state_zebra=[]
	current_state_lamp=[]
	
	cached_or_not_cat=[]
	cached_or_not_zebra=[]
	cached_or_not_lamp=[]

	eligible_cat=[]
	eligible_zebra=[]
	eligible_lamp=[]
	
	control_reg_cat=[]
	control_reg_lamp=[]
	control_reg_zebra=[]

	goal_switch_cat=[]
	goal_switch_lamp=[]
	goal_switch_zebra=[]

	choices_cat=[]
	choices_lamp=[]
	choices_zebra=[]

	pswq_scores_cat=[]
	pswq_scores_zebra=[]
	pswq_scores_lamp=[]

	


	 # Track RTs for each type of trial
	rt_consecutive_delayed_cat = []
	rt_consecutive_non_delayed_cat = []
	rt_non_consecutive_delayed_cat = []
	rt_non_consecutive_non_delayed_cat = []

	rt_consecutive_delayed_cat = []
	rt_consecutive_non_delayed_cat = []
	rt_non_consecutive_delayed_cat = []
	rt_non_consecutive_non_delayed_cat = []

	rt_consecutive_delayed_cat = []
	rt_consecutive_non_delayed_cat = []
	rt_non_consecutive_delayed_cat = []
	rt_non_consecutive_non_delayed_cat = []
	
	df = pd.read_csv(sub)

	counter=1
	sum_pswq=0

	first_action='plan1_response.keys'
	first_state_image='image_arrived'
	second_action='plan2_response.keys'
	second_state_image='image_arrived2'
	third_action='plan3_response.keys'
	third_state_image='image_arrived3'


	s2_states=df[first_state_image].unique().tolist()
	s3_states=df[second_state_image].unique().tolist()
	goals=df[trial_type].unique().tolist()
	goals = [x for x in goals if str(x) != 'nan']
	print(goals)
	
	all_states=['start']+s2_states+s3_states
	

	cached_actions={}
	for state in all_states:
		cached_actions['{}_{}'.format('images/lamp.png',state)]='0'
		cached_actions['{}_{}'.format('images/cat.png',state)]='0'
		cached_actions['{}_{}'.format('images/zebra.png',state)]='0'
	for col in q_cols:
		# Drop NaN values and reset the index
		df_temp = df[col].dropna().reset_index(drop=True)
		
		# Check if the counter is in reverse_counters
		if counter in reverse_counters:
			sum_pswq += reverse_dict[int(df_temp[0])]
		else:
			sum_pswq += int(df_temp[0])
		
		counter += 1
	sum_stress=0
	counter=0
	# for col in q_cols2:
	# 	# Drop NaN values and reset the index
	# 	df_temp = df[col].dropna().reset_index(drop=True)
	# 	sum_stress += int(df_temp[0])
	# 	counter += 1



	for decision_time in range(1,4):
		# print('decision time: {}'.format(decision_time))
		decision_col='plan{}_response.rt'.format(decision_time)
		choice_col='plan{}_response.keys'.format(decision_time)
		
		

	
		df=pd.read_csv(sub)

		timepoints_short=[*range(num_decisions_to_consider)]
		
		zebra_count=1
		lamp_count=1
		bending_count=1
		cat_count=1

		zebra_correct_current=[]
		zebra_correct_label_current=[]
		zebra_correct_decision_num=[]
		zebra_incorrect_current=[]
		zebra_incorrect_label_current=[]
		zebra_incorrect_decision_num=[]

	
		

		arrived1='image_arrived1'
		arrived2='image_arrived2'



		last_goal='first'
		planning_trial_num_zebra=0
		planning_trial_num_cat=0
		planning_trial_num_lamp=0
		planning_trial_num=0

		#all components of a trajectory
		

		


		for row in range(len(df)):


			
			if planning_trial_num<60:
				try:

					
					




					if 'zebra' in df[trial_type][row]:


						pswq_scores_zebra.append(sum_pswq)
						if zebra_count>20-num_decisions_to_consider:
							
									
							if decision_time==1:
								eligible_zebra.append(0)
								current_action=df[first_action][row]
								current_state_zebra.append('start')
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],'start')]:
									cached_or_not_zebra.append(1)
								else:
									cached_or_not_zebra.append(0)

								cached_actions['{}_{}'.format(df[trial_type][row],'start')]=df[first_action][row]
							elif decision_time==2:
								current_state_zebra.append(df[first_state_image][row])
								eligible_zebra.append(1)
								current_action=df[second_action][row]
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]:
									cached_or_not_zebra.append(1)
								else:
									cached_or_not_zebra.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]=df[second_action][row]
							elif decision_time==3:
								current_state_zebra.append(df[second_state_image][row])
								if df[second_state_image][row]=='images/backpack.png':
									eligible_zebra.append(1)
								else:
									eligible_zebra.append(0)
								current_action=df[third_action][row]
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]:
									cached_or_not_zebra.append(1)
								else:
									cached_or_not_zebra.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]=df[third_action][row]


							choices_zebra.append(df[choice_col][row])
							trial_num_zebra.append(planning_trial_num)
							trial_num_zebra_rel.append(zebra_count)
							planning_trial_num_zebra+=1
							rts_zebra_current.append(df[decision_col][row])

							if df[first_action][row]=='space':
								if df[second_action][row]!='space':
									if df[third_action][row]!='space':
										optimal_delayed_planning_zebra.append(1)
									else:
										optimal_delayed_planning_zebra.append(0)
								else:
									optimal_delayed_planning_zebra.append(0)
							else:
								optimal_delayed_planning_zebra.append(0)
							if decision_time==2:
								delayed_planning_zebra.append(1)
								control_reg_zebra.append(1)
								if df[second_action][row]!='space':
									optimal_control_choice_zebra.append(1)
								else:
									optimal_control_choice_zebra.append(0)
								
								

							elif decision_time==1:
								delayed_planning_zebra.append(0)
								control_reg_zebra.append(0)
								if df[first_action][row]=='space':
									optimal_control_choice_zebra.append(1)
								else:
									optimal_control_choice_zebra.append(0)
								

								
							elif decision_time==3:
								delayed_planning_zebra.append(0)
								control_reg_zebra.append(1)
								if df[third_action][row]!='space':
									optimal_control_choice_zebra.append(1)
								else:
									optimal_control_choice_zebra.append(0)
								
								


							if df[trial_type][row]==df[image_arrived][row]:
								got_to_goal_zebra.append(1)
								got_to_goal_zebra_last.append(1)
							else:
								got_to_goal_zebra.append(0)
								got_to_goal_zebra_last.append(0)
							
							if last_goal!='zebra':
								goal_switch_zebra.append(1)
							else:
								goal_switch_zebra.append(0)

						

							zebra_count+=1
							
							planning_trial_num+=1
							last_goal='zebra'
						



				

					elif 'cat' in df[trial_type][row]:
						
						if cat_count>20-num_decisions_to_consider:

							

							pswq_scores_cat.append(sum_pswq)
							if decision_time==1:
								
								eligible_cat.append(1)


								current_action=df[first_action][row]
								current_state_cat.append('start')
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],'start')]:
									cached_or_not_cat.append(1)
								else:
									cached_or_not_cat.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],'start')]=df[first_action][row]
								


							elif decision_time==2:
								if df[first_state_image][row]=='images/toothbrush.png':
									eligible_cat.append(1)
								else:
									eligible_cat.append(0)

								current_action=df[second_action][row]
								current_state_cat.append(df[first_state_image][row])
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]:
									cached_or_not_cat.append(1)
								else:
									cached_or_not_cat.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]=df[second_action][row]
								

							elif decision_time==3:
								current_state_cat.append(df[second_state_image][row])
								if df[first_state_image][row]=='images/car.png':
									eligible_cat.append(1)
								else:
									eligible_cat.append(0)

								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]:
									cached_or_not_cat.append(1)
								else:
									cached_or_not_cat.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]=df[third_action][row]
								

							choices_cat.append(df[choice_col][row])
							trial_num_cat.append(planning_trial_num)
							trial_num_cat_rel.append(cat_count)
							planning_trial_num_cat+=1

							rts_cat_current.append(df[decision_col][row])
							if df[first_action][row]!='space':
								if df[second_action][row]!='space':
									if df[third_action][row]!='space':
										optimal_delayed_planning_cat.append(1)

									else:
										optimal_delayed_planning_cat.append(0)
								else:
									optimal_delayed_planning_cat.append(0)
							else:
								optimal_delayed_planning_cat.append(0)

							if decision_time==1:
								delayed_planning_cat.append(1)
								control_reg_cat.append(1)
								if df[first_action][row]!='space':
									optimal_control_choice_cat.append(1)
								else:
									optimal_control_choice_cat.append(0)
								
								
							else:
								delayed_planning_cat.append(0)
								control_reg_cat.append(1)
								if decision_time==2:
									if df[second_action][row]!='space':
										optimal_control_choice_cat.append(1)
									else:
										optimal_control_choice_cat.append(0)
								if decision_time==3:
									if df[third_action][row]!='space':
										optimal_control_choice_cat.append(1)
									else:
										optimal_control_choice_cat.append(0)
								
								
							if df[trial_type][row]==df[image_arrived][row]:
								got_to_goal_cat.append(1)
								got_to_goal_cat_last.append(1)
							else:
								got_to_goal_cat.append(0)
								got_to_goal_cat_last.append(0)

							if last_goal!='cat':
								goal_switch_cat.append(1)
							else:
								goal_switch_cat.append(0)

							cat_count+=1
							last_goal='cat'
							planning_trial_num+=1
							

					elif 'lamp' in df[trial_type][row]:
						

						if lamp_count>20-num_decisions_to_consider:
							

							
							
							if decision_time==1:
								eligible_lamp.append(1)
								current_action=df[first_action][row]
								current_state_lamp.append('start')
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],'start')]:
									cached_or_not_lamp.append(1)
								else:
									cached_or_not_lamp.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],'start')]=df[first_action][row]
							elif decision_time==2:
								eligible_lamp.append(1)
								current_action=df[second_action][row]
								current_state_lamp.append(df[first_state_image][row])
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]:
									cached_or_not_lamp.append(1)
								else:
									cached_or_not_lamp.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[first_state_image][row])]=df[second_action][row]
							elif decision_time==3:
								current_state_lamp.append(df[second_state_image][row])
								eligible_lamp.append(1)
								current_action=df[third_action][row]
								if current_action == cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]:
									cached_or_not_lamp.append(1)
								else:
									cached_or_not_lamp.append(0)
								cached_actions['{}_{}'.format(df[trial_type][row],df[second_state_image][row])]=df[third_action][row]

							pswq_scores_lamp.append(sum_pswq)
							trial_num_lamp.append(planning_trial_num)
							trial_num_lamp_rel.append(lamp_count)
							planning_trial_num_lamp+=1

							if lamp_count==1:
								if decision_time==3:
									print('firstentry_decision3_lamp {}\n'.format(cached_or_not_lamp[-1]))
							choices_lamp.append(df[choice_col][row])
							rts_lamp_current.append(df[decision_col][row])
							if df[first_action][row]=='space':
								if df[second_action][row]=='space':
									if df[third_action][row]!='space':
										optimal_delayed_planning_lamp.append(1)
									else:
										optimal_delayed_planning_lamp.append(0)
								else:
									optimal_delayed_planning_lamp.append(0)
							else:
								optimal_delayed_planning_lamp.append(0)
							if decision_time==3:
								delayed_planning_lamp.append(1)
								control_reg_lamp.append(1)
								if df[third_action][row]!='space':
									optimal_control_choice_lamp.append(1)
								else:
									optimal_control_choice_lamp.append(0)
								
								
							else:
								delayed_planning_lamp.append(0)
								control_reg_lamp.append(0)
								if decision_time==1:
									if df[first_action][row]=='space':
										optimal_control_choice_lamp.append(1)
									else:
										optimal_control_choice_lamp.append(0)
								elif decision_time==2:
									if df[second_action][row]=='space':
										optimal_control_choice_lamp.append(1)
									else:
										optimal_control_choice_lamp.append(0)

								
								
							if df[trial_type][row]==df[image_arrived][row]:
								got_to_goal_lamp.append(1)
								got_to_goal_lamp_last.append(1)
							else:
								got_to_goal_lamp.append(0)
								got_to_goal_lamp_last.append(0)
							
							if last_goal!='lamp':
								goal_switch_lamp.append(1)
							else:
								goal_switch_lamp.append(0)

							lamp_count+=1
							last_goal='lamp'
							planning_trial_num+=1
							

					
				except:
					nan_found=1


	# Normalize within subjects
	all_current=rts_lamp_current+rts_zebra_current+rts_cat_current
	rts_zebra_current=[np.log(x) for x in rts_zebra_current]
	rts_lamp_current=[np.log(x) for x in rts_lamp_current]
	rts_cat_current=[np.log(x) for x in rts_cat_current]

	choices_cats+=choices_cat
	choices_zebras+=choices_zebra
	choices_lamps+=choices_lamp

	optimal_delayed_planning_cats+=optimal_delayed_planning_cat
	optimal_delayed_planning_zebras+=optimal_delayed_planning_zebra
	optimal_delayed_planning_lamps+=optimal_delayed_planning_lamp

	optimal_control_choice_cats+=optimal_control_choice_cat
	optimal_control_choice_zebras+=optimal_control_choice_zebra
	optimal_control_choice_lamps+=optimal_control_choice_lamp

	optimal_delayed_planning_cats_last+=[0]+optimal_delayed_planning_cat[:-1]
	optimal_delayed_planning_zebras_last+=[0]+optimal_delayed_planning_zebra[:-1]
	optimal_delayed_planning_lamps_last+=[0]+optimal_delayed_planning_lamp[:-1]

	pswq_scores_cats+=pswq_scores_cat
	pswq_scores_lamps+=pswq_scores_lamp
	pswq_scores_zebras+=pswq_scores_zebra

	rts_zebra+=rts_zebra_current
	rts_lamp+=rts_lamp_current
	rts_cat+=rts_cat_current

	cached_or_not_lamps+=cached_or_not_lamp
	cached_or_not_cats+=cached_or_not_cat
	cached_or_not_zebras+=cached_or_not_zebra

	got_to_goal_cats+=got_to_goal_cat
	got_to_goal_zebras+=got_to_goal_zebra
	got_to_goal_lamps+=got_to_goal_lamp

	got_to_goal_cats_last+=got_to_goal_cat_last[:-1]
	got_to_goal_zebras_last+=got_to_goal_zebra_last[:-1]
	got_to_goal_lamps_last+=got_to_goal_lamp_last[:-1]

	delayed_planning_cats+=delayed_planning_cat
	delayed_planning_lamps+=delayed_planning_lamp
	delayed_planning_zebras+=delayed_planning_zebra

	control_reg_cats+=control_reg_cat
	control_reg_lamps+=control_reg_lamp
	control_reg_zebras+=control_reg_zebra

	eligible_cats+=eligible_cat
	eligible_zebras+=eligible_zebra
	eligible_lamps+=eligible_lamp


	current_state_cats+=current_state_cat
	current_state_zebras+=current_state_zebra
	current_state_lamps+=current_state_lamp

	goal_switch_cats+=goal_switch_cat
	goal_switch_lamps+=goal_switch_lamp
	goal_switch_zebras+=goal_switch_zebra

	raw_action_cats+=raw_action_cat
	raw_action_zebras+=raw_action_zebra
	raw_action_lamps+=raw_action_lamp

	trial_num_cat=[(x-59)/59.0 for x in trial_num_cat]
	trial_num_lamp=[(x-59)/59.0 for x in trial_num_lamp]
	trial_num_zebra=[(x-59)/59.0 for x in trial_num_zebra]

	trial_num_cats+=trial_num_cat
	trial_num_lamps+=trial_num_lamp
	trial_num_zebras+=trial_num_zebra

	trial_num_cats_rel+=trial_num_cat_rel
	trial_num_lamps_rel+=trial_num_lamp_rel
	trial_num_zebras_rel+=trial_num_zebra_rel

	sub_numbers1+=[str(sub)]*3*num_decisions_to_consider
	sub_numbers2+=[str(sub)]*3*num_decisions_to_consider
	sub_numbers3+=[str(sub)]*3*num_decisions_to_consider


	
	sub_num+=1

sub_nums=[]
for i in range(sub_num-1):
	sub_nums+=[i]*60

sub_nums=sub_nums*3

# plot choices over time
sns.set(style='white', palette='mako', font='arial', font_scale=1.5, rc=None)
df_results2=pd.DataFrame()
df_results2['sub']=sub_numbers1+sub_numbers2+sub_numbers3
df_results2['trial_num']=trial_num_cats+trial_num_zebras+trial_num_lamps
df_results2['trial_num_within_goal']=trial_num_cats_rel+trial_num_zebras_rel+trial_num_lamps_rel
df_results2['current_state']=current_state_cats+current_state_zebras+current_state_lamps
df_results2['decision']=timepoints_tracker
df_results2['got_to_goal']=got_to_goal_cats+got_to_goal_zebras+got_to_goal_lamps
df_results2['got_to_goal_last']=got_to_goal_cats_last+got_to_goal_zebras_last+got_to_goal_lamps_last
df_results2['goal_switch']=goal_switch_cats+goal_switch_zebras+goal_switch_lamps
df_results2['control_regressor']=control_reg_cats+control_reg_zebras+control_reg_lamps
df_results2['RT']=rts_cat+rts_zebra+rts_lamp
df_results2['eligible_decisions_accuracy']=eligible_cats+eligible_zebras+eligible_lamps
df_results2['retrieved_cached']=cached_or_not_cats+cached_or_not_zebras+cached_or_not_lamps
df_results2['planning_depth']=[3]*(num_decisions_to_consider*3*len(subs))+[2]*(num_decisions_to_consider*3*len(subs))+[1]*(num_decisions_to_consider*3*len(subs))
df_results2['delayed_planning']=delayed_planning_cats+delayed_planning_zebras+delayed_planning_lamps
df_results2['choices']=choices_cats+choices_zebras+choices_lamps
df_results2['worry']=pswq_scores_cats+pswq_scores_zebras+pswq_scores_lamps
df_results2['optimally_delayed']=optimal_delayed_planning_cats+optimal_delayed_planning_zebras+optimal_delayed_planning_lamps
df_results2['optimally_control_choice']=optimal_control_choice_cats+optimal_control_choice_zebras+optimal_control_choice_lamps
df_results2['optimally_delayed_last']=optimal_delayed_planning_cats_last+optimal_delayed_planning_zebras_last+optimal_delayed_planning_lamps_last 

# sns.heatmap(dfc)
# plt.show()
# dfa=pd.read_csv('all_individual_subs_optimal_delay_by_binarized.csv')

# df_results3=df_results2[df_results2['delayed_planning']==1]
df_results2.to_csv('preprocessed_data.csv')
# df_results3.to_csv('lmm_matrix_only_optimallydelayedtrials.csv')


