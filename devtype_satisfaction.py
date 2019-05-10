#<<<<<<< HEAD
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt

def add_dev(devs,strings):
	strings=strings.split(";");
	
	for string in strings:
		if string in devs:
			devs[string]+=1;
		else:
			devs[string]=1;

def add_career(careers,strings,satisfaction):
	strings=strings.split(";");
	for string in strings:
		if (string in careers) and satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
			careers[string]+=1;
		elif satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
			careers[string]=1;	


df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","CareerSatisfaction"]];
df=df.dropna(axis="rows");
df=df.values;

careers={};
devs={};

for row in df:
	career=row[1];
	dev=row[0];
	
	add_dev(devs,dev);
	add_career(careers,dev,career);

map={};
for key in devs:
	print(key,":",round(100*careers[key]/devs[key],2));
	map[key]=round(100*careers[key]/devs[key],2);

dev_sum=sum([devs[key] for key in devs]);
career_sum=sum([careers[key] for key in careers]);

print("Total satisfaction is",round(100*career_sum/dev_sum,2));

plt.figure();	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage Satisfied");
plt.title("Percent satisfied for each devtype");
plt.show();
# =======
# import pandas as pd;
# import numpy as np;

# def add_dev(devs,strings):
	# strings=strings.split(";");
	
	# for string in strings:
		# if string in devs:
			# devs[string]+=1;
		# else:
			# devs[string]=1;

# def add_career(careers,strings,satisfaction):
	# strings=strings.split(";");
	# for string in strings:
		# if (string in careers) and satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
			# careers[string]+=1;
		# elif satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
			# careers[string]=1;	


# df=pd.read_csv("survey_results_public.csv");
# df=df[["DevType","CareerSatisfaction"]];
# df=df.dropna(axis="rows");
# df=df.values;

# careers={};
# devs={};

# for row in df:
	# career=row[1];
	# dev=row[0];
	
	# add_dev(devs,dev);
	# add_career(careers,dev,career);

# for key in devs:
	# print(key,":",round(100*careers[key]/devs[key],2));

# dev_sum=sum([devs[key] for key in devs]);
# career_sum=sum([careers[key] for key in careers]);

# print("Total satisfaction is",round(100*career_sum/dev_sum,2));
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
