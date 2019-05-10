#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;
import math as m;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def add_language(languages,language):
	if language in languages:
		languages[language]+=1;
	else:
		languages[language]=1;
def add_database(databases,database):
	if database in databases:
		databases[database]+=1;
	else:
		databases[database]=1;
def add_platform(platforms,platform):
	if platform in platforms:
		platforms[platform]+=1
	else:
		platforms[platform]=1;
def add_framework(frameworks,framework):
	if framework in frameworks:
		frameworks[framework]+=1;
	else:
		frameworks[framework]=1;
		
df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","LanguageWorkedWith","DatabaseWorkedWith","PlatformWorkedWith","FrameworkWorkedWith"]]; #limits down to langauges and stuff
df=df[ df.DevType==df.DevType]; #gets rid of all data with non existent values

languages={};
databases={};
platforms={};
frameworks={};

df=df.values;

df=[row for row in df if "Data scientist" in row[0]];
for row in df:
	lang_work=row[1];
	base_work=row[2];
	plat_work=row[3];
	frame_work=row[4];
	if type(lang_work)==str: 
		lang_work=lang_work.split(";");
	else:
		lang_work="0"
	if type(base_work)==str:
		base_work=base_work.split(";");
	else:
		base_work="0"
	if type(plat_work)==str:
		plat_work=plat_work.split(";");
	else:
		plat_work="0"
	if type(frame_work)==str:
		frame_work=frame_work.split(";");
	else:
		frame_work="0"
	
	for lang in lang_work:
		add_language(languages,lang);
	for base in base_work:
		add_database(databases,base);
	for plat in plat_work:
		add_platform(platforms,plat);
	for frame in frame_work:
		add_framework(frameworks,frame);

language_map={};
database_map={};
platform_map={};
framework_map={};		
		
print("Language:\n");
for language in languages:
	print(language,round(100*languages[language]/len(df),2));
	language_map[language]=round(100*languages[language]/len(df),2);
print("\nDatabases:\n");
for database in databases:
	print(database,round(100*databases[database]/len(df),2));
	database_map[database]=round(100*databases[database]/len(df),2);
print("\nPlatforms:\n")
for platform in platforms:
	print(platform,round(100*platforms[platform]/len(df),2));
	platform_map[platform]=round(100*platforms[platform]/len(df),2);
print("\nFrameworks\n");
for framework in frameworks:
	print(framework, round(100*frameworks[framework]/len(df),2));
	framework_map[framework]=round(100*frameworks[framework]/len(df),2);

plt.figure();	
#ax=plt.subplot(1,1,1);
x=list(language_map.keys());
y=list(language_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage of Data Scientists");
plt.title("Languages of Data Scientists");


plt.figure();
#ax=plt.subplot(1,1,1);
x=list(database_map.keys());
y=list(database_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage of Data Scientists");
plt.title("Databases of Data Scientists");

plt.figure();
#ax=plt.subplot(1,1,1);
x=list(platform_map.keys());
y=list(platform_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage of Data Scientists");
plt.title("Platforms of Data Scientists");

plt.figure();
#ax=plt.subplot(1,1,1);
x=list(framework_map.keys());
y=list(framework_map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percentage of Data Scientists");
plt.title("Frameworks of Data Scientists");

plt.show();




	

	
	
# =======
# import csv;
# import pandas as pd;
# import numpy as np;
# import math as m;

# def add_language(languages,language):
	# if language in languages:
		# languages[language]+=1;
	# else:
		# languages[language]=1;
# def add_database(databases,database):
	# if database in databases:
		# databases[database]+=1;
	# else:
		# databases[database]=1;
# def add_platform(platforms,platform):
	# if platform in platforms:
		# platforms[platform]+=1
	# else:
		# platforms[platform]=1;
# def add_framework(frameworks,framework):
	# if framework in frameworks:
		# frameworks[framework]+=1;
	# else:
		# frameworks[framework]=1;
		
# df=pd.read_csv("survey_results_public.csv");
# df=df[["DevType","LanguageWorkedWith","DatabaseWorkedWith","PlatformWorkedWith","FrameworkWorkedWith"]]; #limits down to langauges and stuff
# df=df[ df.DevType==df.DevType]; #gets rid of all data with non existent values

# languages={};
# databases={};
# platforms={};
# frameworks={};

# df=df.values;

# df=[row for row in df if "Data scientist" in row[0]];
# for row in df:
	# lang_work=row[1];
	# base_work=row[2];
	# plat_work=row[3];
	# frame_work=row[4];
	# if type(lang_work)==str: 
		# lang_work=lang_work.split(";");
	# else:
		# lang_work="0"
	# if type(base_work)==str:
		# base_work=base_work.split(";");
	# else:
		# base_work="0"
	# if type(plat_work)==str:
		# plat_work=plat_work.split(";");
	# else:
		# plat_work="0"
	# if type(frame_work)==str:
		# frame_work=frame_work.split(";");
	# else:
		# frame_work="0"
	
	# for lang in lang_work:
		# add_language(languages,lang);
	# for base in base_work:
		# add_database(databases,base);
	# for plat in plat_work:
		# add_platform(platforms,plat);
	# for frame in frame_work:
		# add_framework(frameworks,frame);
		
# print("Language:\n");
# for language in languages:
	# print(language,round(100*languages[language]/len(df),2));
# print("\nDatabases:\n");
# for database in databases:
	# print(database,round(100*databases[database]/len(df),2));
# print("\nPlatforms:\n")
# for platform in platforms:
	# print(platform,round(100*platforms[platform]/len(df),2));
# print("\nFrameworks\n");
# for framework in frameworks:
	# print(framework, round(100*frameworks[framework]/len(df),2));
	
	
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
