#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("survey_results_public.csv");

df=df[['Gender','JobSatisfaction','CareerSatisfaction']];
df=df[df.Gender==df.Gender];
df=df[df.JobSatisfaction==df.JobSatisfaction];
df=df[df.CareerSatisfaction==df.CareerSatisfaction];
df=df.values;

satisfied=['Extremely satisfied','Moderately satisfied','Slightly satisfied'];

gen_job={};
gen_career={};
gen_total={};

for row in df:
	genders=row[0];
	genders=genders.split(";");
	for gender in genders:
		if(not gender in gen_job):
			gen_total[gender]=1;
			if row[1] in satisfied:
				gen_job[gender]=1;
			if row[2] in satisfied:
				gen_career[gender]=1;
		else:
			gen_total[gender]+=1;
			if row[1] in satisfied:
				gen_job[gender]+=1;
			if row[2] in satisfied:
				gen_career[gender]+=1;
			
		
job_map={};
career_map={};
for gender in gen_total:
	print(gender+":","Job Satisfaction:",100*round(gen_career[gender]/gen_total[gender],2),", Career Satisfaction:",100*round(gen_job[gender]/gen_total[gender],2));
	job_map[gender]=100*round(gen_career[gender]/gen_total[gender],2);
	career_map[gender]=100*round(gen_job[gender]/gen_total[gender],2);

plt.figure();	
#ax=plt.subplot(1,1,1);
x=list(job_map.keys());
y=list(job_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percent Satisfaction");
plt.title("Job Satisfaction");

plt.figure();	
#ax=plt.subplot(1,1,1);
x=list(career_map.keys());
y=list(career_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percent Satisfaction");
plt.title("Career Satisfaction");

plt.show();

# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# df=pd.read_csv("survey_results_public.csv");

# df=df[['Gender','JobSatisfaction','CareerSatisfaction']];
# df=df[df.Gender==df.Gender];
# df=df[df.JobSatisfaction==df.JobSatisfaction];
# df=df[df.CareerSatisfaction==df.CareerSatisfaction];
# df=df.values;

# satisfied=['Extremely satisfied','Moderately satisfied','Slightly satisfied'];

# gen_job={};
# gen_career={};
# gen_total={};

# for row in df:
	# genders=row[0];
	# genders=genders.split(";");
	# for gender in genders:
		# if(not gender in gen_job):
			# gen_total[gender]=1;
			# if row[1] in satisfied:
				# gen_job[gender]=1;
			# if row[2] in satisfied:
				# gen_career[gender]=1;
		# else:
			# gen_total[gender]+=1;
			# if row[1] in satisfied:
				# gen_job[gender]+=1;
			# if row[2] in satisfied:
				# gen_career[gender]+=1;
			
		

# for gender in gen_total:
	# print(gender+":","Job Satisfaction:",100*round(gen_career[gender]/gen_total[gender],2),", Career Satisfaction:",100*round(gen_job[gender]/gen_total[gender],2));


# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
