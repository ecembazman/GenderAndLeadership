import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

filteredData = pd.read_csv("../../success/data/Filtered_Success_Technology vs. Health.csv")
df = filteredData.copy()

emotions_data = {"Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful",
              "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere",
              "Jealous", "Envious",
              "Admiring","Proud","Respectful","Inspired",
              "Uneasy", "Simpaty",
              "Angry", "Desprecio", "Resentful","Molestia","Disgusted", "Hateful","Frustrated",
              "Ashamed","Pity"}

corr = df[emotions_data].corr()
#print(corr)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(df[emotions_data].columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df[emotions_data].columns)
ax.set_yticklabels(df[emotions_data].columns)

plt.show()
# pozitif korelasyon sonucu oluşan gruplamalar:
# gruplamalar -> grup1 : "Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful"
# gruplamalar -> grup2 : "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere"
# gruplamalar -> grup3 : "Angry", "Desprecio", "Resentful", "Molestia", "Disgusted", "Hateful", "Frustrated"
# gruplamalar -> grup4 : "Admiring","Proud","Respectful","Inspired"
# gruplamalar -> grup5 : "Jealous", "Envious"
# gruplamalar -> grup6 : "Uneasy", "Simpaty"