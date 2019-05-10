import csv;
import pandas as pd;
import numpy as np;

df=pd.read_csv("survey_results_public.csv");
df=df[["LanguageWorkedWith","ConvertedSalary"]];
df=df[df.LanguageWorkedWith==df.LanguageWorkedWith];
df= df[df.ConvertedSalary==df.ConvertedSalary];
df=df.values

language_salary={};
language_count={};

for row in df:
	languages=row[0];
	languages=languages.split(";");
	for language in languages:
		if language in language_salary:
			language_salary[language]+=row[1];
			language_count[language]+=1;
		else:
			language_salary[language]=row[1];
			language_count[language]=1;
			

for key in language_salary:
	print(key+": ",round(language_salary[key]/language_count[key],2));