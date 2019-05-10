import csv;
import pandas as pd;
import numpy as np;

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
			
		

for gender in gen_total:
	print(gender+":","Job Satisfaction:",100*round(gen_career[gender]/gen_total[gender],2),", Career Satisfaction:",100*round(gen_job[gender]/gen_total[gender],2));


