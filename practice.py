# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:56:31 2022

@author: shiva
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
read_csv_data = pd.read_csv('income.csv')
data = read_csv_data.copy()
data.info()
data.isnull().sum()
summery_num = data.describe()
print(summery_num)
summery_cate = data.describe(include='object')
print(summery_cate)
summery_cate.columns
for i in summery_cate.columns:
    print(data[str(i)].value_counts())
print(data['JobType'].value_counts())
print(data['occupation'].value_counts())
read_csv_again = pd.read_csv('income.csv', na_values=[' ?'])
data2 = read_csv_again.copy()
missing1 = data2.isnull().any(axis=0)
missing2 = data2.isnull().any(axis=1)
data3 = data2.dropna()
correlation = data3.corr()
corr1 = data.corr()
data3['SalStat'] = data3['SalStat'].map({' less than or equal to 50,000':0, ' greater than 50,000': 1})
new_data = pd.get_dummies(data3, drop_first=True)
column_list = list(new_data.columns)
features = list(set(column_list)-set('SalStat'))
y = new_data['SalStat'].values
x = new_data[features].values
train_x, test_x, train_y, test_y = train_test_split(x, y, train_size=0.01, random_state=0)
logistic = LogisticRegression()
logistic.fit(train_x, train_y)
logistic.coef_
logistic.intercept_
predict = logistic.predict(test_x)
acc = accuracy_score(test_y, predict)
print(acc)
print('Misclassified samples: %d' % (test_y != predict).sum())
