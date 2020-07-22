import re
import string
import numpy as np
import pandas as pd
df = pd.read_csv("Final.csv")
skillarray=[["aws","gcp","kubernetes","jenkins","devops","docker","ansible","azure","gitlab","linux","unix"],["svm","tensorflow","pandas","matplotlib","flask","nlp","keras","machine learning"]]
freq1=[[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
c=0
def freq(title,text):
    if(title=='Data Scientist and Analyst'):

        for i in range(len(skillarray[1])):
            if text.count(skillarray[1][i])>0:
                freq1[1][i]+=1
        return c
for i in range(len(df)):

    freq(df['Title'][i],df['Description'][i])

print(freq1)