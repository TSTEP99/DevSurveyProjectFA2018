import csv;
import pandas as pd;
import numpy as np;

df=pd.read_csv("survey_results_public.csv");
df=df[["DevType","UndergradMajor"]]; #limits down to 
df=df[ df.DevType==df.DevType]; #gets rid of all data with non existent values