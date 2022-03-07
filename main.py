# import os
import pandas as pd


data_csv = pd.read_csv('stock_data.csv', index_col=0, na_values=[2])
# print(data_csv)

data_xlsx = pd.read_excel('stock_data_xlsx.xlsx', sheet_name='stock_data', index_col=0, na_values=[-11.57])
# print(data_xlsx)

data_txt_table = pd.read_table('stock_data_txt.txt', index_col=0)
print(data_txt_table)

data_txt_table_txt = pd.read_csv('stock_data_txt.txt', delimiter=',')
print(data_txt_table_txt)
