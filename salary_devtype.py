#<<<<<<< HEAD
import numpy as np;
import pandas as pd;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","ConvertedSalary"]];
df=df[df.DevType==df.DevType];
df=df[df.ConvertedSalary==df.ConvertedSalary];

df=df.values;


num_devs={};
salary_dev={};

#print(df);

for row in df:
	devtype=row[0];
	devtype=devtype.split(";");
	salary=row[1];
	
	for dev in devtype:
		#print(dev);
		#print(salary_dev);
		if dev in salary_dev:
			salary_dev[dev]+=salary;
			num_devs[dev]+=1;
		else:
			salary_dev[dev]=salary;
			num_devs[dev]=1;
map={};
for key in salary_dev:
	print(key,round(salary_dev[key]/num_devs[key],2));
	map[key]=round(salary_dev[key]/num_devs[key],2);
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90);
plt.ylabel("Salary USD");
plt.title("Salary based on language of devtype");

plt.show();

		
# =======
# import numpy as np;
# import pandas as pd;

# df=pd.read_csv("survey_results_public.csv");
# df=df[["DevType","ConvertedSalary"]];
# df=df[df.DevType==df.DevType];
# df=df[df.ConvertedSalary==df.ConvertedSalary];

# df=df.values;


# num_devs={};
# salary_dev={};

# print(df);

# for row in df:
	# devtype=row[0];
	# devtype=devtype.split(";");
	# salary=row[1];
	
	# for dev in devtype:
		# print(dev);
		# if dev in salary_dev:
			# salary_dev[dev]+=salary;
			# num_devs[dev]+=1;
		# else:
			# salary_dev=salary;
			# num_devs[dev]=1;

# for key in salary_dev:
	# print(key,salary_dev[key]/num_devs[key]);
		
		
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
