import pandas as pd
import os
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# os.chdir("I:\\Github Projects\\2. Python For Data Science")
income_data = pd.read_csv('income.csv')

data = income_data.copy(deep=True)

data.info()