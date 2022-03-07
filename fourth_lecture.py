import pandas as pd
import numpy as np

read_data = pd.read_csv('stock_data.csv', index_col=0, na_values=['???', "????"])
print(read_data.info())
# print(np.unique(read_data['P&L']))
read_data["LTP"] = read_data["LTP"].astype('object')
print(read_data.info())
print('object', read_data['LTP'].nbytes)  #152
print('category', read_data['LTP'].astype('category').nbytes)  #171
# print(read_data['LTP'].nbytes)
print('float', read_data['LTP'].astype('float64').nbytes)  #152


read_data['cost'].replace('three', 3, inplace=True)
read_data['cost'].replace('sixty', 60, inplace=True)
read_data['cost'].replace('five', 5, inplace=True)
read_data['cost'].replace('two', 2, inplace=True)

read_data['cost'] = read_data['cost'].astype('float64')
print(read_data.info())

print(read_data.isnull().sum())

