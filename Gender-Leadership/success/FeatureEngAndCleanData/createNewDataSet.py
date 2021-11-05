import pandas as pd
from numpy import random

filteredData = pd.read_csv("../data/Filtered_Success_Technology vs. Health.csv")
df = filteredData.copy()
#print(df.shape)
################################ POZITIF CORR GRUPLAMASI #############################################################
# pozitif korelasyon sonucu oluşan gruplamalar:
grup1 = {"Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful"}
grup2 = {"Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere"}
grup3 = {"Angry", "Desprecio", "Resentful", "Molestia", "Disgusted", "Hateful", "Frustrated"}
grup4 = {"Admiring","Proud","Respectful","Inspired"}
grup5 = {"Jealous", "Envious"}
grup6 = {"Uneasy", "Simpaty"}

dfsum1 = 0
for data in grup1:
    dfEmotion = df[data]
    dfsum1 = dfsum1 + dfEmotion

dfmeanGroup1 = dfsum1 / len(grup1)

dfsum2 = 0
for data in grup2:
    dfEmotion = df[data]
    dfsum2 = dfsum2 + dfEmotion

dfmeanGroup2 = dfsum2 / len(grup2)

dfsum3 = 0
for data in grup3:
    dfEmotion = df[data]
    dfsum3 = dfsum3 + dfEmotion

dfmeanGroup3 = dfsum3 / len(grup3)

dfsum4 = 0
for data in grup4:
    dfEmotion = df[data]
    dfsum4 = dfsum4 + dfEmotion

dfmeanGroup4 = dfsum4 / len(grup4)

dfsum5 = 0
for data in grup5:
    dfEmotion = df[data]
    dfsum5 = dfsum5 + dfEmotion

dfmeanGroup5 = dfsum5 / len(grup5)

dfsum6 = 0
for data in grup6:
    dfEmotion = df[data]
    dfsum6 = dfsum6 + dfEmotion

dfmeanGroup6 = dfsum6 / len(grup6)

sLength = len(df['Competent'])
df['Group1(Competent)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group1(Competent)'] = dfmeanGroup1

df['Group2(Friendly)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group2(Friendly)'] = dfmeanGroup2

df['Group3(Hateful)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group3(Hateful)'] = dfmeanGroup3

df['Group4(Admiring)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group4(Admiring)'] = dfmeanGroup4

df['Group5(Jealous)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group5(Jealous)'] = dfmeanGroup5

df['Group6(Uneasy)'] = pd.Series(random.randn(sLength), index=df.index)
df['Group6(Uneasy)'] = dfmeanGroup6

################################ STATISTICAL ANALYSIS DATA PREPARING #######################################
# df = df.drop(['Competent', 'Confident', 'Capable', 'Efficient', 'Intelligent', 'Skilful',
#                  'Friendly', 'Wellintentioned', 'Trustworthy', 'Warm', 'Goodnatured', 'Sincere',
#                   'Jealous', 'Envious',
#                   'Admiring','Proud','Respectful','Inspired',
#                   'Uneasy', 'Simpaty',
#                   'Angry', 'Desprecio', 'Resentful','Molestia','Disgusted', 'Hateful','Frustrated',
#                   'Ashamed','Pity', 'Group'], axis=1)

df['Group6(Uneasy)'] = df['Group6(Uneasy)'].round()
df['Group5(Jealous)'] = df['Group5(Jealous)'].round()
df['Group4(Admiring)'] = df['Group4(Admiring)'].round()
df['Group3(Hateful)'] = df['Group3(Hateful)'].round()
df['Group2(Friendly)'] = df['Group2(Friendly)'].round()
df['Group1(Competent)'] = df['Group1(Competent)'].round()

df['Group6(Uneasy)'] = df['Group6(Uneasy)'].astype('object')
df['Group5(Jealous)'] = df['Group5(Jealous)'].astype('object')
df['Group4(Admiring)'] = df['Group4(Admiring)'].astype('object')
df['Group3(Hateful)'] = df['Group3(Hateful)'].astype('object')
df['Group2(Friendly)'] = df['Group2(Friendly)'].astype('object')
df['Group1(Competent)'] = df['Group1(Competent)'].astype('object')

# print(df.head(10))
# print(df.describe())
# print(df.info())

df.to_csv(path_or_buf="../../success/data/Corr_Success_Technology vs. Health.csv")