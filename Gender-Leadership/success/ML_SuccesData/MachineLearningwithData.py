import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.svm import SVC

data_var = ['Group1(Competent)', 'Group2(Friendly)', 'Group3(Hateful)', 'Group4(Admiring)', 'Group5(Jealous)', 'Group6(Uneasy)', 'Leadersex']
df = pd.read_csv("../data/Corr_Success_Technology vs. Health.csv") #, usecols=data_var)
data = df.copy()
data = data.drop(columns="Unnamed: 0", axis=1)
data = data.drop(columns="Unnamed: 0.1", axis=1)

#print(data.describe())

# print(data['Leadersex'].unique())
# print(data['Participantsex'].unique())
# print(data['Group2(Friendly)'].unique())
# print(data['Group6(Uneasy)'].unique())

print(data.groupby('Leadersex').size())
print(data.groupby('Participantsex').size())
print(data.groupby('Group2(Friendly)').size())
print(data.groupby('Group6(Uneasy)').size())

data['Group6(Uneasy)'] = data['Group6(Uneasy)'].astype('category')
data['Group5(Jealous)'] = data['Group5(Jealous)'].astype('category')
data['Group4(Admiring)'] = data['Group4(Admiring)'].astype('category')
data['Group3(Hateful)'] = data['Group3(Hateful)'].astype('category')
data['Group2(Friendly)'] = data['Group2(Friendly)'].astype('category')
data['Group1(Competent)'] = data['Group1(Competent)'].astype('category')
data['Leadersex'] = data['Leadersex'].astype('category')

data['Group6(Uneasy)'] = data['Group6(Uneasy)'].cat.codes
data['Group5(Jealous)'] = data['Group5(Jealous)'].cat.codes
data['Group4(Admiring)'] = data['Group4(Admiring)'].cat.codes
data['Group3(Hateful)'] = data['Group3(Hateful)'].cat.codes
data['Group2(Friendly)'] = data['Group2(Friendly)'].cat.codes
data['Group1(Competent)'] = data['Group1(Competent)'].cat.codes
data['Leadersex'] = data['Leadersex'].cat.codes

#print(data.corr())

############################ MACHINE LEARNING #####################################################
y=pd.DataFrame(data["Leadersex"])
X=pd.DataFrame(data.drop(["Leadersex"], axis=1))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
													test_size=0.2,
													random_state=50)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

############################ KNN #####################################################
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
						   metric_params=None, n_jobs=None, n_neighbors=5,
						   p=2, weights='uniform')
knn_model = knn.fit(X_train, y_train)
print(knn_model)
print('Accuracy of KNN on training set: {:.2f}'
	.format(knn.score(X_train, y_train)))
print('Accuracy of KNN on test set: {:.2f}'
	.format(knn.score(X_test, y_test)))

y_pred = knn_model.predict(X_test)
print(y_pred)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg = logreg.fit(X_train, y_train)
print('Accuracy of logistic regression classifier on training set: {:.2f}'
	.format(logreg.score(X_train, y_train)))

print('Accuracy of logistic regression classifier on test set: {:.2f}'
	.format(logreg.score(X_test, y_test)))

y_pred = logreg.predict(X_test)
print(y_pred)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

############################ SVM #####################################################
#support vektor model
# svm_model = SVC(kernel="linear").fit(X_train, y_train)
# y_pred = svm_model.predict(X_test)
# print(y_pred)
# print(accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))

############################ Regression Linear #####################################################
# import statsmodels.api as sm
# lm = sm.regression.linear_model.OLS(y_train, X_train)
# lm = lm.fit()
# print(lm.summary())

# ############################ sciklit learn ####################
# from sklearn.linear_model import LogisticRegression
# loj = LogisticRegression(solver='liblinear')
# loj_model = loj.fit(X,y)
# print(loj_model)

################## stats models #############################
# genderLoj = sm.Logit(y, X)
# loj_model = genderLoj.fit()
# print(loj_model.summary())