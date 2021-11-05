import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

filteredData = pd.read_csv("../data/Filtered_Success_Technology vs. Health.csv")
df = filteredData.copy()
print(df.shape)
#print(df.info())

emotions_data = {"Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful",
              "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere",
              "Jealous", "Envious",
              "Admiring","Proud","Respectful","Inspired",
              "Uneasy", "Simpaty",
              "Angry", "Desprecio", "Resentful","Molestia","Disgusted", "Hateful","Frustrated",
              "Ashamed","Pity"}

other_data = {"Participantsex", "Leadersex", "Age", "Maritalstatus", "Typeofcompany",
              "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
              "Nationality"}

##################### DUYGU-GRUP-1  #################################
# "Uneasy", "Simpaty"
g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Simpaty", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Uneasy", "Age", edgecolor="w").add_legend();

##################### DUYGU-GRUP-2  #################################
# "Jealous", "Envious"
g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Jealous", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Envious", "Age", edgecolor="w").add_legend();

plt.show()

##################### DUYGU-GRUP-3  #################################
# "Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful",
g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Competent", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Confident", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Capable", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Efficient", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Intelligent", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Skilful", "Age", edgecolor="w").add_legend();

##################### DUYGU-GRUP-4  #################################
# "Admiring","Proud","Respectful","Inspired"

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Admiring", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Proud", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Respectful", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Leadersex", col="Participantsex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Inspired", "Age", edgecolor="w").add_legend();

##################### DUYGU-GRUP-5  #################################
# "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere"
g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Ashamed", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Pity", "Age", edgecolor="w").add_legend();

##################### DUYGU-GRUP-6  #################################
# "Angry", "Desprecio", "Resentful", "Molestia", "Disgusted", "Hateful", "Frustrated"
g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Angry", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Desprecio", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Resentful", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Molestia", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Disgusted", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Hateful", "Age", edgecolor="w").add_legend();

g=sns.FacetGrid(df,hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Frustrated", "Age", edgecolor="w").add_legend();

##################### OTHER LEADERS  #################################

other_leader = {"Assessmentleader", "Responsaatribu", "Replacementleader"}

g=sns.FacetGrid(df, hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Simpaty", "Assessmentleader", edgecolor="w").add_legend();

g=sns.FacetGrid(df, hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Simpaty", "Responsaatribu", edgecolor="w").add_legend();

g=sns.FacetGrid(df, hue="Participantsex", col="Leadersex", margin_titles=True, palette={1:"blue", 2:"pink"})
g=g.map(plt.scatter, "Simpaty", "Replacementleader", edgecolor="w").add_legend();


