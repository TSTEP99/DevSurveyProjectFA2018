import numpy as np;
import pandas as pd;

df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","ConvertedSalary"]];
df=df[df.DevType==df.DevType];
df=df[df.ConvertedSalary==df.ConvertedSalary];

df=df.values;


num_devs={};
salary_dev={};

print(df);

for row in df:
	devtype=row[0];
	devtype=devtype.split(";");
	salary=row[1];
	
	for dev in devtype:
		print(dev);
		if dev in salary_dev:
			salary_dev[dev]+=salary;
			num_devs[dev]+=1;
		else:
			salary_dev=salary;
			num_devs[dev]=1;

for key in salary_dev:
	print(key,salary_dev[key]/num_devs[key]);
		
		
