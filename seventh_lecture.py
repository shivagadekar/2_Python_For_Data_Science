# plotting basic plots using seaborm library
# it provides high level interface for drawings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

read_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])
read_data.dropna(axis=0, inplace=True)

sns.set(style='darkgrid')
sns.regplot(x=read_data['Age'], y=read_data['Price'], fit_reg=True)
plt.show()