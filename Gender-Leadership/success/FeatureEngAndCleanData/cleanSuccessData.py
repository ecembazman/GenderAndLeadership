import pandas as pd
import researchpy as rp

# success data temizleme işlemini içerir
# temizlenen data bir csv dosyasına kaydedilecektir:
# Filtered_Success_Technology vs. Health.csv

data_csv = pd.read_csv("../data/Success_Technology vs. Health.csv")
df = data_csv.copy()
dfGözlem = data_csv.copy()
#print(dfGözlem.shape)
#print(dfGözlem.isnull().sum())

other_data = {"Participantsex", "Leadersex", "Age", "Maritalstatus", "Typeofcompany",
               "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation"}

all_data = {"Participantsex", "Leadersex", "Age", "Maritalstatus", "Typeofcompany",
               "Assessmentleader", "Responsaatribu", "Replacementleader", "Levelofeducation",
              "Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful",
              "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere",
              "Jealous", "Envious",
              "Admiring","Proud","Respectful","Inspired",
              "Uneasy", "Simpaty",
              "Angry", "Desprecio", "Resentful","Molestia","Disgusted", "Hateful","Frustrated",
              "Ashamed","Pity"}

################### Katılımcıların kaçı erkek kaçı kadın ###################
dfGözlem["Participantsex"].replace({1: 'male', 2: 'female'}, inplace=True)
print(dfGözlem["Participantsex"].value_counts().count)
################### Katılımcıların yaş ortlaması ###################

print(dfGözlem["Age"].mean())
print(dfGözlem["Age"].min())
print(dfGözlem["Age"].max())

print(rp.summary_cont(dfGözlem["Age"]))

################### Katılımcıların eğitim durumu ###################
dfGözlem["Levelofeducation"].replace({0: 'okumamış', 1: 'ilkokul', 2: 'orta', 3: 'Lise', 4: 'Üni', 5:'Master', 6:'Doktora'}, inplace=True)
print(dfGözlem["Levelofeducation"].value_counts().count)
################### Katılımcıların şirket türü ###################
dfGözlem["Typeofcompany"].replace({1: 'teknoloji', 2: 'sağlık-hizmet'}, inplace=True)
print(dfGözlem["Typeofcompany"].value_counts().count)

##################### FILTER-1  #################################
# VAR ile başlayan bir önceki çalışmanın sonuçlarını datadan çıkarılacaktır
# Profession kolonunda 51 adet eksik var çalışanlardan elde edilen anket sonucunda
# sağlık ve teknoloji TypeofCompanyde var olduğu için. meslek alanına ihtiyaç kalmamıştır bu alanı da silinebilir
# ManiExp1 ve Maniexp2 ne olduğu anlaşılmayan veriler olduğundan silinebilir
# Province - bölgenin bu analiz ile ilgili bir yardımcı veri olmaması nedeniyle silinebilir
df = df.drop(['VARCOMPETENCE', 'VARWARMTH', 'VARADMIRATION', 'VARENVY', 'VARDISGUST', 'VARRECASSESSMENT',
              'VARRECREPLACEMENTLEADER', 'VARRECRESPONSAATRIB', 'Profession', 'Maniexp1', 'Maniexp2', 'Province'], axis=1)
print(df.shape)
##################### FILTER-2  #################################
# İspanyol işçilerden elde edilen veriler olduğunu biliyoruz bu nedenle
# Nationality kolonunu "ispanyol" ile dolduralım
nationality = "ispanyol"
for data in df["Nationality"]:
    df["Nationality"] = df["Nationality"].replace(data, nationality)
print(df.shape)
##################### FILTER-3  #################################
# 18-65 yaş arası filtre / emeklilik yaşı 65 olarak belirlenmiştir
indexList = list
df_age = pd.DataFrame(df["Age"])
indexList = df_age[((df_age< (18)) | (df_age > (65))).any(axis = 1)].index
#print(indexList)
df = df.drop(indexList)
print(df.shape)
##################### FILTER-4  #################################
# Age'de 7 adet boş veriyi mean ile dolduralım
#print(df.Age.mean())
df["Age"] = df.Age.fillna(df.Age.mean())
#print(df.Age.mean())
#print(df.isnull().sum())
#print(df.shape)
##################### FILTER-5  #################################
# duygu alanlarındaki boş datalar ortalama verisi ile doldurulacaktır
emotions_data = {"Competent", "Confident", "Capable", "Efficient", "Intelligent", "Skilful",
              "Friendly", "Wellintentioned", "Trustworthy", "Warm", "Goodnatured", "Sincere",
              "Jealous", "Envious",
              "Admiring","Proud","Respectful","Inspired",
              "Uneasy", "Simpaty",
              "Angry", "Desprecio", "Resentful","Molestia","Disgusted", "Hateful","Frustrated",
              "Ashamed","Pity"}

meanList = list()
for emotion in emotions_data:
    df[emotion] = df[emotion].fillna(df[emotion].mean())

# print(df.isnull().sum())
# print(df.shape)
# print(df.describe())
print(df.dtypes)
df = df[all_data].astype('int64')
print(df.dtypes)

df.to_csv(path_or_buf="../../success/data/Filtered_Success_Technology vs. Health.csv")
