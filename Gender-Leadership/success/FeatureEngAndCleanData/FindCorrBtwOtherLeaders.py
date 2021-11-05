import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filteredData = pd.read_csv("../../success/data/Filtered_Success_Technology vs. Health.csv")
df = filteredData.copy()

other_leader = {"Assessmentleader", "Responsaatribu", "Replacementleader"}

corr = df[other_leader].corr()
#print(corr)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(df[other_leader].columns), 1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df[other_leader].columns)
ax.set_yticklabels(df[other_leader].columns)

plt.show()

# Sonuç:
# "Assessmentleader", "Responsaatribu" pozirif korelasyon
# "Replacementleader" negatif korelasyon