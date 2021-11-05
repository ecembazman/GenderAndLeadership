import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from numpy import random
import numpy as np
from scipy import stats

corrData = pd.read_csv("../data/Corr_Success_Technology vs. Health.csv")
df = corrData.copy()
df = df.drop(columns="Unnamed: 0", axis=1)
df = df.drop(columns="Unnamed: 0.1", axis=1)

dfData = {"Participantsex", "Leadersex", "Age", "Maritalstatus", "Typeofcompany",
              "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
          "Group1(Competent)", "Group2(Friendly)", "Group3(Hateful)",
          "Group4(Admiring)", "Group5(Jealous)", "Group6(Uneasy)"}

dfDataObj = {"Participantsex", "Leadersex", "Maritalstatus", "Typeofcompany",
              "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
          "Group1(Competent)", "Group2(Friendly)", "Group3(Hateful)",
          "Group4(Admiring)", "Group5(Jealous)", "Group6(Uneasy)"}

print(df.dtypes)
df = df.astype('int64')
for obj in dfDataObj:
    df[obj] = df[obj].astype('object')
print(df.dtypes)

######################## Örneklem Oluşturma ##########################################

dfSample = corrData.copy()
dfSample = dfSample.drop(columns="Unnamed: 0", axis=1)
dfSample = dfSample.drop(columns="Unnamed: 0.1", axis=1)
dfSample = dfSample[200:401]

for data in dfData:
    np.random.seed(380)
    dfSampleData = pd.DataFrame(np.random.randint(1,7,201))
    dfSampleData = np.random.choice(a=df[data].astype('object'), size=201)
    dfSample[data] = dfSampleData
    #print(rp.summary_cat(dfSample[data]))
print(dfSample['Age'].std())
print(dfSample['Age'].mean())
######################## Örneklem Oluşturma ##########################################
dfSample.to_csv(path_or_buf="../../success/data/Sample_Success_Technology vs. Health.csv")
