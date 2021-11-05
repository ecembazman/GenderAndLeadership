import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize

df_org = pd.read_csv("../data/Success_Technology vs. Health.csv")
df_org.hist(figsize=(9,7), grid=False);
plt.savefig("SuccesDataBeforeGroup")
#plt.show()

data_var = ['Age', 'Group1(Competent)', 'Group2(Friendly)', 'Group3(Hateful)', 'Group4(Admiring)', 'Group5(Jealous)', 'Group6(Uneasy)', 'Leadersex']
df = pd.read_csv("../data/Corr_Success_Technology vs. Health.csv", usecols=data_var)
data = df.copy()

df.hist(figsize=(9,7), grid=False);
plt.savefig("SuccesDataAfterGroup")
#plt.show()
print(data.describe())

sns.pairplot(data, kind="reg", hue="Leadersex", palette={1:"blue", 2:"pink"})
plt.suptitle('reg of succes data')
plt.savefig('reg of success data')
#plt.show()

g=sns.FacetGrid(df,hue="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Group2(Friendly)", "Age", edgecolor="w").add_legend();
plt.savefig('scatter of Group2(Friendly)')
#plt.show()

g=sns.FacetGrid(df,hue="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Group6(Uneasy)", "Age", edgecolor="w").add_legend();
plt.savefig('scatter of Group6(Uneasy)')
#plt.show()

sns.pairplot(data, kind="reg")
plt.suptitle('reg of variables in data')
plt.savefig('reg of variables in data')
#plt.show()

data.drop('Leadersex', axis=1).plot(kind='box', layout=(5,5), sharex=False, sharey=False, figsize=(3,3), title='Leadersex box plot')
plt.savefig('Leadersex box plot')
#plt.show()

#####################################################################################
# Display classes
sns.countplot(data['Group2(Friendly)'], label="count")
plt.savefig('Group2(Friendly) Count')
#plt.show()

sns.countplot(data['Group6(Uneasy)'], label="count")
plt.savefig('Group6(Uneasy) Count')
#plt.show()

import pylab as pl
data.drop('Leadersex', axis=1).hist(bins=30, figsize=(12,12))
plt.suptitle("Histogram for emotion grous")
plt.savefig('GenderLeadership_hist')
#plt.show()