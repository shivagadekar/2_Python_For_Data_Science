import pandas as pd

data_read = pd.read_csv('Toyota.csv', na_values=['??', "????"], index_col=0)

data_read2 = data_read.copy()
data_read3 = data_read2.copy()

# to check null values isnull() and isna() are used
# and these function returns True or False, If cell contains Nan then boolean output is Nan

print(data_read2.isnull().sum())

missing = data_read2[data_read2.isnull().any(axis=1)]
print(data_read2.describe())

print('without_filling_na', data_read2['Age'].mean())
print('with_na = ', data_read3['Age'].fillna(data_read2['Age'].mean(), inplace=True)) 
print(data_read2['KM'].median())
print(data_read2['KM'].mean())
data_read2['KM'].fillna(data_read2['KM'].median(), inplace=True)