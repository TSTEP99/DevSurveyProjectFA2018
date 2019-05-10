#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def add_job(Job_Salary,satisfaction,salary):
	if satisfaction in Job_Salary:
		Job_Salary[satisfaction]+=salary;
	else:
		Job_Salary[satisfaction]=salary;
def add_career(Career_Salary,satisfaction,salary):
	if satisfaction in Career_Salary:
		Career_Salary[satisfaction]+=salary;
	else:
		Career_Salary[satisfaction]=salary;

def add_people(Num_People,satisfaction):
	if satisfaction in Num_People:
		Num_People[satisfaction]+=1;
	else:
		Num_People[satisfaction]=1;


df=pd.read_csv("survey_results_public.csv");

df=df[["JobSatisfaction","CareerSatisfaction","ConvertedSalary"]];

df=df[df.JobSatisfaction==df.JobSatisfaction];
df=df[df.CareerSatisfaction==df.CareerSatisfaction];
df=df[df.ConvertedSalary==df.ConvertedSalary];
df=df.values;

Job_Salary={};
Career_Salary={};
Num_People1={};
Num_People2={};

for row in df:
	job=row[0];
	career=row[1];
	
	salary=row[2];
	add_job(Job_Salary,job,salary);
	add_career(Career_Salary,career,salary);
	add_people(Num_People1,job);
	add_people(Num_People2,career);

print("\nJob Satifaction");
job_map={};
for level in Job_Salary:
	print(level, round(Job_Salary[level]/Num_People1[level],2));
	job_map[level]= round(Job_Salary[level]/Num_People1[level],2);

print("\nCareer Satisfaction");
career_map={};
for level in Career_Salary:
	print(level, round(Career_Salary[level]/Num_People2[level],2));
	career_map[level]=round(Career_Salary[level]/Num_People2[level],2);

plt.figure();	
x=list(job_map.keys());
y=list(job_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Salary in USD");
plt.title("Salary based on level of job satisfaction");

plt.figure();	
x=list(career_map.keys());
y=list(career_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Salary in USD");
plt.title("Salary based on level of career satisfaction");

plt.show();



# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# def add_job(Job_Salary,satisfaction,salary):
	# if satisfaction in Job_Salary:
		# Job_Salary[satisfaction]+=salary;
	# else:
		# Job_Salary[satisfaction]=salary;
# def add_career(Career_Salary,satisfaction,salary):
	# if satisfaction in Career_Salary:
		# Career_Salary[satisfaction]+=salary;
	# else:
		# Career_Salary[satisfaction]=salary;

# def add_people(Num_People,satisfaction):
	# if satisfaction in Num_People:
		# Num_People[satisfaction]+=1;
	# else:
		# Num_People[satisfaction]=1;


# df=pd.read_csv("survey_results_public.csv");

# df=df[["JobSatisfaction","CareerSatisfaction","ConvertedSalary"]];

# df=df[df.JobSatisfaction==df.JobSatisfaction];
# df=df[df.CareerSatisfaction==df.CareerSatisfaction];
# df=df[df.ConvertedSalary==df.ConvertedSalary];
# df=df.values;

# Job_Salary={};
# Career_Salary={};
# Num_People1={};
# Num_People2={};

# for row in df:
	# job=row[0];
	# career=row[1];
	# salary=row[2];
	# add_job(Job_Salary,job,salary);
	# add_career(Career_Salary,career,salary);
	# add_people(Num_People1,job);
	# add_people(Num_People2,career);

# print("\nJob Satifaction");
# for level in Job_Salary:
	# print(level, round(Job_Salary[level]/Num_People1[level],2));

# print("\nCareer Satisfaction");
# for level in Career_Salary:
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
	# print(level, round(Career_Salary[level]/Num_People2[level],2));