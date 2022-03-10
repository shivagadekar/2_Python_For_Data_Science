# For python data types as int and float
# For pandas data types as int64 and float64, 64 as 8 bytes and it allocates memory
# for that data in data frame
# Converting string variable into categorical variable saves a lot of memory
# All Nan are considered as object

import pandas as pd

read_data = pd.read_csv('stock_data.csv')
# print(read_data.dtypes['LTP'])
# print(read_data.loc[:, 'LTP'])
# print(read_data.select_dtypes(exclude=[float]))
# print(read_data.select_dtypes(exclude=[object]))
# print(read_data.select_dtypes(exclude=[int]))
print(read_data.info())
print(read_data)
import numpy as np

print(np.unique(read_data['Qty']))