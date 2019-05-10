#<<<<<<< HEAD
import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("survey_results_public.csv");
df=df[["LanguageWorkedWith","CareerSatisfaction"]];
df=df.dropna(axis="rows");
df=df.values;

languages_satisfaction={};
languages_worked={};
for row in df:
	languages=row[0];
	satisfaction=row[1];
	languages=languages.split(";");
	for language in languages:
		if language in languages_worked:
			languages_worked[language]+=1;
			if satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
					languages_satisfaction[language]+=1;
		else:
			languages_worked[language]=1;
			if satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
				languages_satisfaction[language]=1;
			else:
				languages_satisfaction[language]=0;
				

map={};
for key in languages_worked:
	print(key,":",round(100*languages_satisfaction[key]/languages_worked[key],2));
	map[key]=round(100*languages_satisfaction[key]/languages_worked[key],2);

plt.figure();	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90)
plt.ylabel("Percent satisfied");
plt.title("Percent of people satisfied for each developer language");

plt.show();



				
# =======
# import pandas as pd;
# import numpy as np;

# df=pd.read_csv("survey_results_public.csv");
# df=df[["LanguageWorkedWith","CareerSatisfaction"]];
# df=df.dropna(axis="rows");
# df=df.values;

# languages_satisfaction={};
# languages_worked={};
# for row in df:
	# languages=row[0];
	# satisfaction=row[1];
	# languages=languages.split(";");
	# for language in languages:
		# if language in languages_worked:
			# languages_worked[language]+=1;
			# if satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
					# languages_satisfaction[language]+=1;
		# else:
			# languages_worked[language]=1;
			# if satisfaction in ("Extremely satisfied","Moderately satisfied","Slightly satisfied"):
				# languages_satisfaction[language]=1;
			# else:
				# languages_satisfaction[language]=0;
				


# for key in languages_worked:
	# print(key,":",round(100*languages_satisfaction[key]/languages_worked[key],2));
	

				
# # >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
				