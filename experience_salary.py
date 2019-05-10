import csv;
import pandas as pd;
import numpy as np;

def add_salary(years_salary,years,salary):
	if years in years_salary:
		years_salary[years]+=salary;
	else:
		years_salary[years]=salary;

def add_people(num_people,years):
	if years in num_people:
		num_people[years]+=1;
	else:
		num_people[years]=1;


df=pd.read_csv("survey_results_public.csv");

df=df[["YearsCoding","ConvertedSalary"]];

df=df[df.YearsCoding ==df.YearsCoding];
df=df[df.ConvertedSalary == df.ConvertedSalary];

df=df.values;
years_salary={};
num_people={};

for row in df:
	years=row[0];
	salary=row[1];
	
	add_salary(years_salary,years,salary);
	add_people(num_people,years);


