#<<<<<<< HEAD
import pandas as pd;
import csv;

import math as m

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("survey_results_public.csv");

#looks at formal education and slary
majors=data.UndergradMajor;

num_of_majors={}

print("Number of people with each Undergrad Major level\n")

#finds the number of people in each degree categoriy
for i in range( len(majors)):
	if majors[i] in num_of_majors:
		num_of_majors[str(majors[i])]+=1;
	else:
		num_of_majors[str(majors[i])]=1;

#prints category and corresponding number
for key in num_of_majors:
	print(key+":", num_of_majors[key]);
	
print("\n");

salaried_developers={key:0 for key in num_of_majors};

salary=data["ConvertedSalary"];



#print(salary);

salary_of_developers={key : 0 for key in num_of_majors};

print("Average Salary of Developers based on Undergrad Major\n")


#finds all developers who have a salary and tracks salary
for i in range(len(majors)):
	num=salary[i];
	if(m.isnan(num)):
		continue;
	
	
	salary_of_developers[str(majors[i])]+=float(salary[i]);
	salaried_developers[str(majors[i])]+=1.0;
		#print(salary[i],degrees[i]);

#prints value of salary	
map={};	
for key in salary_of_developers:
	print(key+":",round(salary_of_developers[key]/salaried_developers[key],2));
	map[key]=round(salary_of_developers[key]/salaried_developers[key],2);

plt.figure();	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Salary in USD");
plt.title("Salary based on undergraduate major");

plt.figure();
labels=tuple(num_of_majors.keys());
sizes=list(num_of_majors.values());
plt.pie(sizes,labels=labels);
plt.axis('equal');

plt.show();

print(num_of_majors);
