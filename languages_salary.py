#<<<<<<< HEAD
import csv;
import pandas as pd;
import numpy as np;

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("survey_results_public.csv");
df=df[["LanguageWorkedWith","ConvertedSalary"]];
df=df[df.LanguageWorkedWith==df.LanguageWorkedWith];
df= df[df.ConvertedSalary==df.ConvertedSalary];
df=df.values

language_salary={};
language_count={};

for row in df:
	languages=row[0];
	languages=languages.split(";");
	for language in languages:
		if language in language_salary:
			language_salary[language]+=row[1];
			language_count[language]+=1;
		else:
			language_salary[language]=row[1];
			language_count[language]=1;
			

map={};
for key in language_salary:
	print(key+": ",round(language_salary[key]/language_count[key],2));
	map[key]=round(language_salary[key]/language_count[key],2);
	
x=list(map.keys());
y=list(map.values());

plt.bar(list(range(1,len(x)+1)),y,width=0.2,align="center",tick_label=tuple(x));
plt.xticks(rotation=90);
plt.ylabel("Salary USD");
plt.title("Salary based on language of use");

plt.show();

# =======
# import csv;
# import pandas as pd;
# import numpy as np;

# df=pd.read_csv("survey_results_public.csv");
# df=df[["LanguageWorkedWith","ConvertedSalary"]];
# df=df[df.LanguageWorkedWith==df.LanguageWorkedWith];
# df= df[df.ConvertedSalary==df.ConvertedSalary];
# df=df.values

# language_salary={};
# language_count={};

# for row in df:
	# languages=row[0];
	# languages=languages.split(";");
	# for language in languages:
		# if language in language_salary:
			# language_salary[language]+=row[1];
			# language_count[language]+=1;
		# else:
			# language_salary[language]=row[1];
			# language_count[language]=1;
			

# for key in language_salary:
# >>>>>>> 5eac722042f98a35dc721bdfe513a6deeafad609
	# print(key+": ",round(language_salary[key]/language_count[key],2));