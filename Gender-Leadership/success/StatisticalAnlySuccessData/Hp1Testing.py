import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from numpy import random
import numpy as np
from scipy import stats
from  scipy.stats import f_oneway
from  scipy.stats import shapiro
df = pd.read_csv("../data/Corr_Success_Technology vs. Health.csv")
dfSample = pd.read_csv("../data/Sample_Success_Technology vs. Health.csv")
dfSample = dfSample.drop(columns="Unnamed: 0", axis=1)

dfData = {"Participantsex", "Leadersex", "Age", "Maritalstatus", "Typeofcompany",
              "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
          "Group1(Competent)", "Group2(Friendly)", "Group3(Hateful)",
          "Group4(Admiring)", "Group5(Jealous)", "Group6(Uneasy)"}

dfDataObj = {"Participantsex", "Leadersex", "Maritalstatus", "Typeofcompany",
              "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
          "Group1(Competent)", "Group2(Friendly)", "Group3(Hateful)",
          "Group4(Admiring)", "Group5(Jealous)", "Group6(Uneasy)"}

dfSample = dfSample.astype('int64')

ExpGrup1 = pd.DataFrame(dfSample[0:66])    #Leadersex = 1
ExpGrup2 = pd.DataFrame(dfSample[66:133])  #Leadersex = 2
ExpGrup3 = pd.DataFrame(dfSample[133:201])  #Leadersex = 3
#
ExpGrup1['Leadersex'] = ExpGrup1['Leadersex'].replace({2:1}, inplace=True)
ExpGrup2['Leadersex'] = ExpGrup2['Leadersex'].replace({1:2}, inplace=True)
ExpGrup3['Leadersex'] = ExpGrup3['Leadersex'].replace({1:3, 2:3}, inplace=True)

# ############# VARSAYIM TESTİ ##########################

# HOMOJENLIK TESTI LEVENE
maleLeader = dfSample[(dfSample['Leadersex'] == 1)]
maleLeader.reset_index(inplace=True)

femaleLeader = dfSample[(dfSample['Leadersex'] == 2)]
femaleLeader.reset_index(inplace=True)

generalLeader = dfSample[(dfSample['Leadersex'] == 3)]
generalLeader.reset_index(inplace=True)

homojen = False
levenetest = stats.levene(ExpGrup1['Group6(Uneasy)'], ExpGrup2['Group6(Uneasy)'], ExpGrup3['Group6(Uneasy)'])
print(levenetest)
if levenetest[1] > 0.05:
    print("Varyanslar homojendir")
    homojen = True

print(ExpGrup1.groupby("Participantsex") ['Group6(Uneasy)'].describe())

# Normallik testi Görsel
diff = dfSample['Group6(Uneasy)']
stats.probplot(diff, dist="norm", plot=plt)
plt.title('Group6(Uneasy) - Erkeksi Özellik')
plt.show()

# # Normallik testi
print(stats.shapiro(dfSample['Group6(Uneasy)']))

# ###################### Hipotez-1 Testi ##############################################################
print(stats.ttest_ind(generalLeader.Leadersex, generalLeader['Group6(Uneasy)'], equal_var=homojen))
print('{:.5f}'.format(stats.ttest_ind(dfSample['Leadersex'], dfSample['Group6(Uneasy)'], equal_var=homojen) [1]))

################################################################################################
