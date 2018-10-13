import pandas as pd;
import csv;
import numpy;



data=pd.read_csv("survey_results_public.csv");

data=data[data.JobSatisfaction==data.JobSatisfaction];

data=data[['FormalEducation','JobSatisfaction']];

data=data.values;

satisfactionLevels=['Extremely dissatisfied','Moderately dissatisfied','Slightly dissatisfied','Neither satisfied nor dissatisfied'
,'Slightly satisfied','Moderately satisfied','Extremely satisfied'];

tot_satisfaction={};

num_respondents={};

for row in data:
	if row[0] in tot_satisfaction:
		tot_satisfaction[row[0]][row[1]]+=1;
		num_respondents[row[0]]+=1;
	else:
		tot_satisfaction[row[0]]={key: 0 for key in satisfactionLevels};
		tot_satisfaction[row[0]][row[1]]+=1;
		num_respondents[row[0]]=1;
		
for key in tot_satisfaction:
	print("\n"+str(key));
	for level in tot_satisfaction[key]:
		print(level+":",round(100*tot_satisfaction[key][level]/num_respondents[key],2));
		
	print("Total satisfied is",round(100*tot_satisfaction[key]['Extremely satisfied']/num_respondents[key],2)+
	round(100*tot_satisfaction[key]['Moderately satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Slightly satisfied']/num_respondents[key],2));
	


