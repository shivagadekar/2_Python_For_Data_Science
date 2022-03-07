import pandas as pd

read_csv = pd.read_csv('stock_data.csv', index_col=0)
# print(read_csv)

read_data = read_csv.copy(deep=True)  # This is deep copy and original datafram cannot be affected
read_data = read_csv.copy(deep=False)  # This is not deep copy and original datafram is always affected
print(read_data)  # To get names of row labels
a = read_data.columns  # To get names of column labels
# print(a[0])
# print('size is', read_data.size)
# print('shape is', read_data.shape)
# print('memory is', read_data.memory_usage())
# print('axis/dimensions is', read_data.ndim)
# print("rows", read_data.head(2))
# print("rows", read_data.tail(2))
print("at", read_data.at['VIVANTA', 'Qty.'])
print("at", read_data.iat[5,5])
print(read_data.loc['VIVANTA', :])