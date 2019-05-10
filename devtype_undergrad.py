#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt

def add_undergrad(dev_majors,dev_type,major):
	if dev_type in dev_majors:
		if major in dev_majors[dev_type]:
			dev_majors[dev_type][major]+=1;
		else:
			dev_majors[dev_type][major]=1;
	else:
		dev_majors[dev_type]={};
		
dev_majors={};

df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","UndergradMajor"]]; #limits down to DevType and UnderGrad Major
df=df[ df.DevType==df.DevType]; #gets rid of all data with non existent values

df=df.values

for row in df:
	dev_type=row[0];
	major=row[1];
	
	dev_type=dev_type.split(";");
	
	for dev in dev_type:
		add_undergrad(dev_majors,dev,major);

maps={};
for dev_type in dev_majors:
	print("\n"+dev_type+"\n");
	
	for major in dev_majors[dev_type]:
		print(str(major)+":",round(100*dev_majors[dev_type][major]/sum(dev_majors[dev_type].values()),2));
		maps[major]=round(100*dev_majors[dev_type][major]/sum(dev_majors[dev_type].values()),2);

labels=tuple(maps.keys());
z=list(maps.values());

plt.pie(z,labels=labels);

plt.show();

	

# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# def add_undergrad(dev_majors,dev_type,major):
	# if dev_type in dev_majors:
		# if major in dev_majors[dev_type]:
			# dev_majors[dev_type][major]+=1;
		# else:
			# dev_majors[dev_type][major]=1;
	# else:
		# dev_majors[dev_type]={};
		
# dev_majors={};

# df=pd.read_csv("survey_results_public.csv");
# df=df[["DevType","UndergradMajor"]]; #limits down to DevType and UnderGrad Major
# df=df[ df.DevType==df.DevType]; #gets rid of all data with non existent values

# df=df.values

# for row in df:
	# dev_type=row[0];
	# major=row[1];
	
	# dev_type=dev_type.split(";");
	
	# for dev in dev_type:
		# add_undergrad(dev_majors,dev,major);

# for dev_type in dev_majors:
	# print("\n"+dev_type+"\n");
	
	# for major in dev_majors[dev_type]:
		# print(str(major)+":",round(100*dev_majors[dev_type][major]/sum(dev_majors[dev_type].values()),2));
	

# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
