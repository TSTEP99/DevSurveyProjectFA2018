<<<<<<< HEAD
import pandas as pd;
import csv;

import math as m

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
for key in salary_of_developers:
=======
import pandas as pd;
import csv;

import math as m

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
for key in salary_of_developers:
>>>>>>> c70096e21339c9e0d368344df34a54a05bf6e49a
	print(key+":",round(salary_of_developers[key]/salaried_developers[key],2));