import pandas as pd  # To work with data
import numpy as np  # To work with numerical operations
import seaborn as sns  # To Visuakize data
from sklearn.model_selection import train_test_split  # To partitation of data
# Library for logastic regression
from sklearn.linear_model import LogisticRegression  
# Import perofrmance matrix, Accuracy score and confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix  


# Importing Data
data_income = pd.read_csv("income.csv")
# Creating copy of original Data
data = data_income.copy()

# =================================================
# 1. Getting to Know Data
# 2. Data Preprocessing (Missing Values)
# 3. Cross Table and Data Visualization
# =================================================


# 1. Getting to Know Data

print(data.info())

# Checking for Missing Values
# True indicated missing data and False Indicates Presence Data
print('Data Columns with null Values:\n\b', data.isnull().sum())
print(np.unique(data['JobType']))
# Summery of numerical Variable
summery_num = data.describe()
print(summery_num)

# Summery of Categorical variable
summery_cate = data.describe(include='O')
print(summery_cate)

# Getting Frequency of Each Category
data['JobType'].value_counts()
data['occupation'].value_counts()
data['EdType'].value_counts()
data['maritalstatus'].value_counts()
data['relationship'].value_counts()
data['race'].value_counts()
data['gender'].value_counts()
data['nativecountry'].value_counts()
# Missing values present only in JobType and occupation


# Checking For Unique Classes
print(np.unique(data['JobType']))
print(np.unique(data['occupation']))
# There is ' ?' presents insted of nan, so read data again

# read data and add nan to missing values
data = pd.read_csv('income.csv', na_values=[" ?"])
# ==============================================================
# Getting to know missing values
print(data.isnull().sum())

# Show rows with missing at least one column values
missing = data[data.isnull().any(axis=1)]
print(missing)

# Now drop all rows with missing values by setting axis=0
data2 = data.dropna(axis=0)
print(data2.isnull().sum())

correlation = data2.corr()

# =============================================================
# Cross Tables and Data Visualization

# Extracting columns names

data2.columns


# Gender Proportion Table
gender = pd.crosstab(index=data2['gender'],
                     columns='count',
                     normalize=True)
print(gender)

# Gender Vs Salary Status
gender_salstat = pd.crosstab(index=data2['gender'],
                             columns=data2['SalStat'],
                             margins=True,
                             normalize='index')
# ============================================================================
# Frequency Distribution of Salary Status
SalStat = sns.countplot(data2['SalStat'])
"""Based on observation, 75% people salary is greater than 50K"""

# Histogram of age
sns.distplot(data2['age'], bins=10, kde=False)

# Box Plot Age Vs Salary
sns.boxplot('SalStat', 'age', data=data2)
data2.groupby('SalStat')['age'].median

# ======================================================
# Frequency Distribution of Salary Status
SalStat = sns.catplot(y='JobType', kind='count', data=data2)
"""Based on observation, 75% people salary is greater than 50K"""

# Histogram of age
# sns.distplot(data2['JobType'], x='count', bins=10, kde=False)


# =====================================================================
# Logistic Regression
data2['SalStat'] = data2['SalStat'].map({' less than or equal to 50,000':0, ' greater than 50,000:': 1})
print(data['SalStat'])


new_data = pd.get_dummies(data2, drop_first=True)

# Storing the column Names
columns_list = list(new_data.columns)
print(columns_list)

features = list(set(columns_list)-set(['SalStat']))
print(features)

y = new_data['SalStat'].values
print(y)


x = new_data[features].values
print(x)

train_x, text_x, train_y, test_y = train_test_split(x,y, test_size=0.3, random_state=0)

logistic = LogisticRegression()
 
logistic.fit(train_x, train_y)
