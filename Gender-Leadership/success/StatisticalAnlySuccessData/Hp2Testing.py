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
maleLeader = dfSample[(dfSample['Leadersex'] == 1)]
maleLeader.reset_index(inplace=True)

femaleLeader = dfSample[(dfSample['Leadersex'] == 2)]
femaleLeader.reset_index(inplace=True)

generalLeader = dfSample[(dfSample['Leadersex'] == 3)]
generalLeader.reset_index(inplace=True)

kadinkatilimci = dfSample[(dfSample['Participantsex'] == 2)]
kadinkatilimci.reset_index(inplace=True)

erkekkatilimci = dfSample[(dfSample['Participantsex'] == 1)]
erkekkatilimci.reset_index(inplace=True)

# Normallik testi
print(stats.shapiro(kadinkatilimci['Group2(Friendly)']))
print(stats.shapiro(dfSample['Group2(Friendly)']))

print(ExpGrup2.groupby("Participantsex") ['Group2(Friendly)'].describe())

# Normallik testi Görsel
# Bağımlı değişken kadınsal özellik

print(rp.summary_cat(ExpGrup2['Group2(Friendly)'] , ['Participantsex']))

diff = dfSample['Group2(Friendly)']
#stats.probplot(diff, dist="norm", plot=plt)
diff.plot(kind='hist')
plt.title('Group2(Friendly) - Kadınsı Özellik')
plt.show()

descriptive, result = rp.ttest(ExpGrup2['Group2(Friendly)'] , ExpGrup2['Participantsex'])
print(descriptive)
print(result)

print(stats.f_oneway(ExpGrup2['Group2(Friendly)'] [ExpGrup2['Participantsex'] == 2],
                    ExpGrup2['Group2(Friendly)'] [ExpGrup2['Participantsex'] == 1]))

# HOMOJENLIK TESTI LEVENE
homojen = False
levenetest1 = stats.levene(ExpGrup1['Group2(Friendly)'], ExpGrup2['Group2(Friendly)'], ExpGrup3['Group2(Friendly)'])
print(levenetest1)

if levenetest1[1] > 0 :
    print("Varyanslar homojendir")
    homojen = True


# ###################### Hipotez-2 Testi ##############################################################

print(ExpGrup2['Participantsex'].corr(ExpGrup2['Group2(Friendly)']))
print(ExpGrup2['Participantsex'].corr(ExpGrup2['Group2(Friendly)'], method='spearman'))
print(stats.pearsonr(ExpGrup2['Participantsex'], ExpGrup2['Group2(Friendly)']))
print(stats.kendalltau(ExpGrup2['Participantsex'], ExpGrup2['Group2(Friendly)']))
print(stats.chi2_contingency(pd.crosstab(ExpGrup2['Participantsex'], ExpGrup2['Group2(Friendly)'])))


table, result = rp.crosstab(ExpGrup2['Participantsex'],
                            ExpGrup2['Group2(Friendly)'],
                            prop='col', test='chi-square')
print(table)
print(result)

################################################################################################
