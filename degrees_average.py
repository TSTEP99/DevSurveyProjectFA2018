import pandas as pd;
import csv;

import math as m

data=pd.read_csv("survey_results_2017.csv");

#looks at formal education and slary
degrees=data.FormalEducation;

num_of_degrees={}

print("Number of people in each education level\n")

#finds the number of people in each degree categoriy
for i in range( len(degrees)):
	if degrees[i] in num_of_degrees:
		num_of_degrees[degrees[i]]+=1;
	else:
		num_of_degrees[degrees[i]]=1;

#prints category and corresponding number
for key in num_of_degrees:
	print(key+":", num_of_degrees[key]);
	
print("\n");

salaried_developers={key:0 for key in num_of_degrees};

salary=data.Salary;

salary_of_developers={key : 0 for key in num_of_degrees};

print("Average Salary of Developers based on level of education\n")

#finds all developers who have a salary and tracks salary
for i in range(len(degrees)):
	num=salary[i];
	if(not m.isnan(num)):
		salary_of_developers[degrees[i]]+=salary[i];
		salaried_developers[degrees[i]]+=1;

#prints value of salary		
for key in salary_of_developers:
	print(key+":",round(salary_of_developers[key]/salaried_developers[key],2));