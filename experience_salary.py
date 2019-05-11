#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

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

map={};
for key in list(years_salary.keys()):
	map[key]=round(years_salary[key]/num_people[key],2);
	print(key, round(years_salary[key]/num_people[key],2));
	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Salary USD");
plt.title("Salary Based on Education level");
	
plt.show();

# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# def add_salary(years_salary,years,salary):
	# if years in years_salary:
		# years_salary[years]+=salary;
	# else:
		# years_salary[years]=salary;

# def add_people(num_people,years):
	# if years in num_people:
		# num_people[years]+=1;
	# else:
		# num_people[years]=1;


# df=pd.read_csv("survey_results_public.csv");

# df=df[["YearsCoding","ConvertedSalary"]];

# df=df[df.YearsCoding ==df.YearsCoding];
# df=df[df.ConvertedSalary == df.ConvertedSalary];

# df=df.values;
# years_salary={};
# num_people={};

# for row in df:
	# years=row[0];
	# salary=row[1];
	
	# add_salary(years_salary,years,salary);
	# add_people(num_people,years);


# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
