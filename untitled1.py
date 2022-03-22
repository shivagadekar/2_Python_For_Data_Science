# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:19:34 2022

@author: shiva
"""

import pandas as pd
import numpy as np
data = pd.read_csv('income.csv')


column_names = data.columns
print('Type is ', type(column_names))
empty_set = []


# for i in column_names:
#     empty_set.append(np.unique(data[i]))

for i in column_names:
    print(np.unique(data[i]))