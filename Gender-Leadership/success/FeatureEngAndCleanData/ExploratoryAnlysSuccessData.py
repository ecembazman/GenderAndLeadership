import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import researchpy as rp

data_csv = pd.read_csv("../data/Filtered_Success_Technology vs. Health.csv")
df = data_csv.copy()
dfGözlem = data_csv.copy()
df = df.drop(columns="Unnamed: 0", axis=1)
dfGözlem = dfGözlem.drop(columns="Unnamed: 0", axis=1)

# print(df.shape)
# print(df.info())
print(df.describe())

df.hist(bins=10, figsize=(9,7), grid=False)
#plt.show()
################### Katılımcıların kaçı erkek kaçı kadın ###################
dfGözlem["Participantsex"].replace({1: 'male', 2: 'female'}, inplace=True)
print(dfGözlem["Participantsex"].value_counts().count)
################### Katılımcıların yaş ortlaması ###################
print(dfGözlem["Age"].mean())
################### Katılımcıların eğitim durumu ###################
dfGözlem["Levelofeducation"].replace({0: 'okumamış', 1: 'ilkokul', 2: 'orta', 3: 'Lise', 4: 'Üni', 5:'Master', 6:'Doktora'}, inplace=True)
print(dfGözlem["Levelofeducation"].value_counts().count)
################### Katılımcıların şirket türü ###################
dfGözlem["Typeofcompany"].replace({1: 'teknoloji', 2: 'sağlık-hizmet'}, inplace=True)
print(dfGözlem["Typeofcompany"].value_counts().count)

g=sns.FacetGrid(df,col="Participantsex", row="Leadersex", margin_titles=True)
g.map(plt.hist, "Age", color="blue")

g=sns.FacetGrid(df,col="Participantsex", row="Leadersex", margin_titles=True)
g.map(plt.hist, "Levelofeducation", color="blue")

g=sns.FacetGrid(df,col="Participantsex", row="Leadersex", margin_titles=True)
g.map(plt.hist, "Typeofcompany", color="blue")

g=sns.FacetGrid(df,col="Participantsex", row="Leadersex", margin_titles=True)
g.map(plt.hist, "Jealous", color="blue")

plt.show()