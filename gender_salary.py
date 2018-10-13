import csv;
import pandas as pd;
import numpy as np;


df=pd.read_csv("survey_results_public.csv");

df=df[['ConvertedSalary','Gender']];
df=df[df.ConvertedSalary==df.ConvertedSalary];
df=df[df.Gender==df.Gender];
df=df.values;

diff_genders=['Female','Male','Transgender','Non-binary, genderqueer, or gender non-conforming'];

gender_salary={key:0 for key in diff_genders};
gender_num={key:0 for key in diff_genders};


for i in range(len(df)):
	genders=df[i][1];
	genders=genders.split(";");
	for j in range(len(genders)):
		gender_salary[genders[j]]+=df[i][0];
		gender_num[genders[j]]+=1;

			
			
for key in gender_num:
	print(key,":",round(gender_salary[key]/gender_num[key],2));

	

