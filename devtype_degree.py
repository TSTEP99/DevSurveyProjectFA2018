import pandas as pd;
import numpy as np;
import csv;

df=pd.read_csv("survey_results_public.csv");

df=df[['FormalEducation','DevType']];

df=df[df.DevType==df.DevType];

df=df[df.FormalEducation==df.FormalEducation];

df=df.values;

dev_educated={}


for i in range(len(df)):
	developers=df[i][1] #gets dev type
	developers=developers.split(";"); # deals with people who identify as multiple developers
	
	for dev in developers:
		if dev in dev_educated:
			if df[i][0] in dev_educated[dev]: #makes sure inside the dictionary
				dev_educated[dev][df[i][0]]+=1;
			else:
				dev_educated[dev][df[i][0]]=1;
		else:
			dev_educated[dev]={};

for key in dev_educated:
	
	print("\n"+key+"\n");
	bachelors=100*dev_educated[key]['Bachelor’s degree (BA, BS, B.Eng., etc.)']/sum(dev_educated[key].values());
	masters= 100*dev_educated[key]['Master’s degree (MA, MS, M.Eng., MBA, etc.)']/sum(dev_educated[key].values());
	doctorate=100*dev_educated[key]['Other doctoral degree (Ph.D, Ed.D., etc.)']/sum(dev_educated[key].values());
	otherprof=100*dev_educated[key]['Professional degree (JD, MD, etc.)']/sum(dev_educated[key].values());
	for dev in dev_educated[key]:
		print(dev,":",round(100*dev_educated[key][dev]/sum(dev_educated[key].values()),2));
	print("Total percentage with bachelor's or higher:",round(bachelors+masters+doctorate+otherprof,2));

	
	
	
		


	