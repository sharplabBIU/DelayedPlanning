import pandas as pd
import numpy as np
import numpy
import csv
import os
import random
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import sem
import itertools
# from statsmodels.tsa.api import SimpleExpSmoothing
# from scipy.optimize import curve_fit


num_decisions_to_consider=20
q_cols=['key_resp_3.keys','key_resp_13.keys','key_resp_14.keys','key_resp_15.keys','key_resp_16.keys','key_resp_25.keys','key_resp_26.keys','key_resp_27.keys','key_resp_28.keys','key_resp_29.keys','key_resp_30.keys','key_resp_31.keys','key_resp_32.keys','key_resp_33.keys','key_resp_34.keys','key_resp_35.keys']
trial_type='r2'
reverse_counters=[1,3,8,10,11]

csv_lines=[['depth3_score','depth2_score','depth1_score']]

reverse_dict={1:5,2:4,3:3,4:2,5:1}
subs=[x for x in os.listdir(os.curdir) if x.startswith('5') or x.startswith('6')]

timepoints_tracker=[['1']*num_decisions_to_consider+['2']*num_decisions_to_consider+['3']*num_decisions_to_consider]
timepoints_tracker=list(itertools.chain.from_iterable(timepoints_tracker))


csv_final=[['subject','optimal_delayed_score','score_depth1','score_depth2','score_depth3','worry']]

zebra_dict={1:'right',2:'left',3:'left'}
decision_answers=['plan1_response.keys',
'plan2_response.keys',
'plan3_response.keys']

accepted_responses=['left','right','space']

for i in range(1000):
	score_depth3=0
	score_depth2=0
	score_depth1=0

	for sub in subs:

		df=pd.read_csv(sub)
		df=df[df['plan2_response.keys'].isin(accepted_responses)]
		
		plan_depth_col=df['r2']
		df = df[decision_answers]	# Shuffle each row

		for idx, row in df.iterrows():
		    df.loc[idx] = np.random.permutation(row)

		# Shuffle each column
		for col in df.columns:
		    df[col] = np.random.permutation(df[col])
	

		df[trial_type]=plan_depth_col
		df=df.reset_index(drop=True)

		zebra_correct_mean=[]
		zebra_labels_correct=[]
		zebra_labels_incorrect=[]
		zebra_correct_std=[]
		zebra_incorrect_mean=[]
		zebra_incorrect_std=[]
		zebra_correct_num=[]
		zebra_incorrect_num=[]

		decisions_zebra=[]
		decisions_cat=[]
		decisions_lamp=[]
		decisions_bending=[]
		
			

		timepoints_short=[*range(num_decisions_to_consider)]
		
		cat_count=1
		bending_count=1
		zebra_count=1
		lamp_count=1

		

		planning_trial_num=0

		for row in range(len(df)):
			if planning_trial_num<60:

				try:
					if 'cat' in df[trial_type][row]:


						goal='depth=3'
						optimal_delayed_score=0


						if df[decision_answers[0]][row]!='space':
							if df[decision_answers[1]][row]!='space':
								if df[decision_answers[2]][row]!='space':
									optimal_delayed_score+=1

									
						score_depth3+=optimal_delayed_score
						trial_number=cat_count
						cat_count+=1
						planning_trial_num+=1
		
				

					elif 'zebra' in df[trial_type][row]:
						goal='depth=2'
						optimal_delayed_score=0
			
						if df[decision_answers[0]][row]=='space':
							if df[decision_answers[1]][row]!='space':
								if df[decision_answers[2]][row]!='space':
									optimal_delayed_score+=1
						score_depth2+=optimal_delayed_score
						trial_number=zebra_count
						zebra_count+=1
						planning_trial_num+=1
				
				
					elif 'lamp' in df[trial_type][row]:
						goal='depth=1'
						optimal_delayed_score=0
						
						if df[decision_answers[0]][row]=='space':
							if df[decision_answers[1]][row]=='space':
								if df[decision_answers[2]][row]!='space':
									optimal_delayed_score+=1
						score_depth1+=optimal_delayed_score
						trial_number=lamp_count
						lamp_count+=1
						planning_trial_num+=1
						if optimal_delayed_score<0:
							optimal_delayed_score=0
					
				except:
					nan_found=1
	print([score_depth1/len(subs),score_depth2/len(subs),score_depth3/len(subs)])
	csv_lines.append([score_depth1/len(subs),score_depth2/len(subs),score_depth3/len(subs)])

with open('permutations_optimal_score.csv'.format(num_decisions_to_consider), 'w') as f:
	writer=csv.writer(f)
	writer.writerows(csv_lines)
