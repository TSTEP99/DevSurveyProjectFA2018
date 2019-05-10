import pandas as pd
import numpy as np
import csv

df=pd.read_csv("survey_results_public.csv");

df=df[["FormalEducation","Gender"]];
df=df[df.Gender==df.Gender];
df=df[df.FormalEducation==df.FormalEducation];
df=df.values;

gen_degrees={};

for  row in df:
	genders=row[1];
	education=row[0];
	genders=genders.split(";");
	
	for gender in genders:
			if gender in gen_degrees:
				if education in gen_degrees[gender]:
					gen_degrees[gender][education]+=1;
				else:
					gen_degrees[gender][education]=1;
			else:
				gen_degrees[gender]={};

print("Percentage with a bachelor's or higher");				
				
for gender in gen_degrees:
	
	bachelors=100*gen_degrees[gender]['Bachelor’s degree (BA, BS, B.Eng., etc.)']/sum(gen_degrees[gender].values());
	masters= 100*gen_degrees[gender]['Master’s degree (MA, MS, M.Eng., MBA, etc.)']/sum(gen_degrees[gender].values());
	doctorate=100*gen_degrees[gender]['Other doctoral degree (Ph.D, Ed.D., etc.)']/sum(gen_degrees[gender].values());
	otherprof=100*gen_degrees[gender]['Professional degree (JD, MD, etc.)']/sum(gen_degrees[gender].values());
	
	print(gender+":",round(bachelors+masters+doctorate+otherprof,2));




