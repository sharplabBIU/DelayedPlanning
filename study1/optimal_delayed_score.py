import pandas as pd
import numpy as np
import numpy
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import sem
import itertools
# from statsmodels.tsa.api import SimpleExpSmoothing
# from scipy.optimize import curve_fit


num_decisions_to_consider=20
threshold=20-num_decisions_to_consider
q_cols=['key_resp_3.keys','key_resp_13.keys','key_resp_14.keys','key_resp_15.keys','key_resp_16.keys','key_resp_25.keys','key_resp_26.keys','key_resp_27.keys','key_resp_28.keys','key_resp_29.keys','key_resp_30.keys','key_resp_31.keys','key_resp_32.keys','key_resp_33.keys','key_resp_34.keys','key_resp_35.keys']

reverse_counters=[1,3,8,10,11]

reverse_dict={1:5,2:4,3:3,4:2,5:1}
subs_df=pd.read_csv('lmm_fixed.csv')
subs=subs_df['sub'].unique()
timepoints_tracker=[['1']*num_decisions_to_consider+['2']*num_decisions_to_consider+['3']*num_decisions_to_consider]
timepoints_tracker=list(itertools.chain.from_iterable(timepoints_tracker))


csv_final=[['sub','optimal_delayed_score','worry']]

zebra_dict={1:'right',2:'left',3:'left'}
decision_answers=['plan1_response.keys',
'plan2_response.keys',
'plan3_response.keys',
'plan4_response.keys']

for sub in subs:
	df=pd.read_csv(sub)

	counter=1
	sum_pswq=0
	for col in q_cols:
		if counter in reverse_counters:
			sum_pswq+=reverse_dict[int(df[col][0])]
		else:

			sum_pswq+=int(df[col][0])
	
		counter+=1
	

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
	
		
	trial_type='r2'
	df=pd.read_csv(sub)

	timepoints_short=[*range(num_decisions_to_consider)]
	
	cat_count=1
	bending_count=1
	zebra_count=1
	lamp_count=1

	

	planning_trial_num=0
	optimal_delayed_score_yes=0
	optimal_delayed_score_no=0

	for row in range(len(df)):
		if planning_trial_num<60:

			try:
				if 'cat' in df[trial_type][row]:
					goal='cat'
					for decision_time in range(1,4):
						decision_col=decision_answers[decision_time-1]
						decisions_cat.append(df[decision_col][row])
						if cat_count>threshold:
							if df[decision_col][row]!='space':
								optimal_delayed_score_yes+=1
							else:
								optimal_delayed_score_yes-=1

					cat_count+=1
					planning_trial_num+=1


				elif 'zebra' in df[trial_type][row]:
					goal='zebra'
					for decision_time in range(1,4):
						decision_col=decision_answers[decision_time-1]
						decisions_zebra.append(df[decision_col][row])
						if zebra_count>threshold:
							if decision_time>1:
								if df[decision_col][row]!='space':
									optimal_delayed_score_yes+=1
								else:
									optimal_delayed_score_yes-=1
							else:
								if df[decision_col][row]!='space':
									optimal_delayed_score_no-=1
								else:
									optimal_delayed_score_no+=1
					zebra_count+=1
					planning_trial_num+=1

				elif 'lamp' in df[trial_type][row]:
					goal='lamp'
					for decision_time in range(1,4):
						decision_col=decision_answers[decision_time-1]
						if lamp_count>threshold:
							if decision_time>2:
								if df[decision_col][row]!='space':
									optimal_delayed_score_yes+=1
								else:
									optimal_delayed_score_yes-=1
							else:
								if df[decision_col][row]!='space':
									optimal_delayed_score_no-=1
								else:
									optimal_delayed_score_no+=1
					lamp_count+=1
					planning_trial_num+=1
				
				
			except:
				nan_found=1
	optimal_delayed_score_sum=((optimal_delayed_score_yes*(1/3)+optimal_delayed_score_no*(2/3))/160.0)+0.5
	csv_final.append([sub,optimal_delayed_score_sum,sum_pswq])


with open('optimal_delayed_scores.csv'.format(num_decisions_to_consider), 'w') as f:
	writer=csv.writer(f)
	writer.writerows(csv_final)

