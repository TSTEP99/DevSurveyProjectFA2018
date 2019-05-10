#<<<<<<< HEAD
import pandas as pd;
import csv;
import numpy;
import matplotlib.pyplot as plt


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
map={};		
for key in tot_satisfaction:
	print("\n"+str(key));
	for level in tot_satisfaction[key]:
		print(level+":",round(100*tot_satisfaction[key][level]/num_respondents[key],2));
		
	print("Total satisfied is",round(100*tot_satisfaction[key]['Extremely satisfied']/num_respondents[key],2)+
	round(100*tot_satisfaction[key]['Moderately satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Slightly satisfied']/num_respondents[key],2));
	map[key]=round(100*tot_satisfaction[key]['Extremely satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Moderately satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Slightly satisfied']/num_respondents[key],2);
	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage of satisfaction");
plt.title("Percent satisfaction based on  education level");
	
plt.show();

# =======
# <<<<<<< HEAD
# import pandas as pd;
# import csv;
# import numpy;



# data=pd.read_csv("survey_results_public.csv");

# data=data[data.JobSatisfaction==data.JobSatisfaction];

# data=data[['FormalEducation','JobSatisfaction']];

# data=data.values;

# satisfactionLevels=['Extremely dissatisfied','Moderately dissatisfied','Slightly dissatisfied','Neither satisfied nor dissatisfied'
# ,'Slightly satisfied','Moderately satisfied','Extremely satisfied'];

# tot_satisfaction={};

# num_respondents={};

# for row in data:
	# if row[0] in tot_satisfaction:
		# tot_satisfaction[row[0]][row[1]]+=1;
		# num_respondents[row[0]]+=1;
	# else:
		# tot_satisfaction[row[0]]={key: 0 for key in satisfactionLevels};
		# tot_satisfaction[row[0]][row[1]]+=1;
		# num_respondents[row[0]]=1;
		
# for key in tot_satisfaction:
	# print("\n"+str(key));
	# for level in tot_satisfaction[key]:
		# print(level+":",round(100*tot_satisfaction[key][level]/num_respondents[key],2));
		
	# print("Total satisfied is",round(100*tot_satisfaction[key]['Extremely satisfied']/num_respondents[key],2)+
	# round(100*tot_satisfaction[key]['Moderately satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Slightly satisfied']/num_respondents[key],2));
	


# =======
# import pandas as pd;
# import csv;
# import numpy;



# data=pd.read_csv("survey_results_public.csv");

# data=data[data.JobSatisfaction==data.JobSatisfaction];

# data=data[['FormalEducation','JobSatisfaction']];

# data=data.values;

# satisfactionLevels=['Extremely dissatisfied','Moderately dissatisfied','Slightly dissatisfied','Neither satisfied nor dissatisfied'
# ,'Slightly satisfied','Moderately satisfied','Extremely satisfied'];

# tot_satisfaction={};

# num_respondents={};

# for row in data:
	# if row[0] in tot_satisfaction:
		# tot_satisfaction[row[0]][row[1]]+=1;
		# num_respondents[row[0]]+=1;
	# else:
		# tot_satisfaction[row[0]]={key: 0 for key in satisfactionLevels};
		# tot_satisfaction[row[0]][row[1]]+=1;
		# num_respondents[row[0]]=1;
		
# for key in tot_satisfaction:
	# print("\n"+str(key));
	# for level in tot_satisfaction[key]:
		# print(level+":",round(100*tot_satisfaction[key][level]/num_respondents[key],2));
		
	# print("Total satisfied is",round(100*tot_satisfaction[key]['Extremely satisfied']/num_respondents[key],2)+
	# round(100*tot_satisfaction[key]['Moderately satisfied']/num_respondents[key],2)+round(100*tot_satisfaction[key]['Slightly satisfied']/num_respondents[key],2));
	


# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
# >>>>>>> c70096e21339c9e0d368344df34a54a05bf6e49a
