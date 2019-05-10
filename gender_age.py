#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df=pd.read_csv("survey_results_public.csv");
df=df[ df.Gender==df.Gender];
df=df[df.Age==df.Age];
df=df[['Gender','Age']];
df=df.values;

gender_map={};
gender_total={}

for i in range(len(df)):
	gender=df[i][0];
	age=df[i][1];
	gender=gender.split(";");
	for sex in gender:
		if(not sex in gender_map):
			gender_map[sex]={};
		else:
			if age in gender_map[sex]:
				gender_map[sex][age]+=1;
			else:
				gender_map[sex][age]=1;

gender2array={};

for key in gender_map:
	print(key);
	
	array={};
	for age in gender_map[key]:
		print(age,round(100*gender_map[key][age]/sum(gender_map[key].values()),2));
		array[age]=round(100*gender_map[key][age]/sum(gender_map[key].values()),2);
	gender2array[key]=array;

diff_genders=['Male','Female','Transgender','Non-binary, genderqueer, or gender non-conforming'];
ages=("Under 18 years old","18 - 24 years old","25 - 34 years old","35 - 44 years old","45 - 54 years old","55 - 64 years old","65 years or older");

female_array=[gender2array["Female"][age] for age in ages];
male_array= [gender2array["Male"][age] for age in ages];
transgender_array= [gender2array["Transgender"][age] for age in ages];
non_binary_array= [gender2array["Non-binary, genderqueer, or gender non-conforming"][age] for age in ages];

x=[i/2 for i in range(1,len(ages)+1)];

ax = plt.subplot(111);
ax.bar(x,[0 for i in x],align="center",tick_label=ages)
ax.bar([i - 0.15 for i in x],male_array,width=0.1,color="c",align="center");
ax.bar([i - 0.05 for i in x], female_array, width=0.1, color='b', align='center')
ax.bar([i + 0.05 for i in x], transgender_array, width=0.1, color='g', align='center')
ax.bar([i + 0.15 for i in x], non_binary_array, width=0.1, color='r', align='center')
ax.autoscale(tight=True);

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.ylabel('Percentage of Gender');
plt.legend(handles=[mpatches.Patch(color='c', label='Male'),mpatches.Patch(color='b', label='Female'),mpatches.Patch(color='g', label='Transgender'),
mpatches.Patch(color='r', label='Non-binary, genderqueer, or gender non-conforming')]);

plt.show();



		
# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches

# df=pd.read_csv("survey_results_public.csv");
# df=df[ df.Gender==df.Gender];
# df=df[df.Age==df.Age];
# df=df[['Gender','Age']];
# df=df.values;

# gender_map={};
# gender_total={}

# for i in range(len(df)):
	# gender=df[i][0];
	# age=df[i][1];
	# gender=gender.split(";");
	# for sex in gender:
		# if(not sex in gender_map):
			# gender_map[sex]={};
		# else:
			# if age in gender_map[sex]:
				# gender_map[sex][age]+=1;
			# else:
				# gender_map[sex][age]=1;

# gender2array={};

# for key in gender_map:
	# print(key);
	
	# array={};
	# for age in gender_map[key]:
		# print(age,round(100*gender_map[key][age]/sum(gender_map[key].values()),2));
		# array[age]=round(100*gender_map[key][age]/sum(gender_map[key].values()),2);
	# gender2array[key]=array;

# diff_genders=['Male','Female','Transgender','Non-binary, genderqueer, or gender non-conforming'];
# ages=("Under 18 years old","18 - 24 years old","25 - 34 years old","35 - 44 years old","45 - 54 years old","55 - 64 years old","65 years or older");

# female_array=[gender2array["Female"][age] for age in ages];
# male_array= [gender2array["Male"][age] for age in ages];
# transgender_array= [gender2array["Transgender"][age] for age in ages];
# non_binary_array= [gender2array["Non-binary, genderqueer, or gender non-conforming"][age] for age in ages];

# x=[i/2 for i in range(1,len(ages)+1)];

# ax = plt.subplot(111);
# ax.bar(x,[0 for i in x],align="center",tick_label=ages)
# ax.bar([i - 0.15 for i in x],male_array,width=0.1,color="c",align="center");
# ax.bar([i - 0.05 for i in x], female_array, width=0.1, color='b', align='center')
# ax.bar([i + 0.05 for i in x], transgender_array, width=0.1, color='g', align='center')
# ax.bar([i + 0.15 for i in x], non_binary_array, width=0.1, color='r', align='center')
# ax.autoscale(tight=True);

# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels)

# plt.ylabel('Percentage of Gender');
# plt.legend(handles=[mpatches.Patch(color='c', label='Male'),mpatches.Patch(color='b', label='Female'),mpatches.Patch(color='g', label='Transgender'),
# mpatches.Patch(color='r', label='Non-binary, genderqueer, or gender non-conforming')]);

# plt.show();



		
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
