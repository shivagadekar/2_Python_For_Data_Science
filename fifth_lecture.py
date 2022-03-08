# a = 2
# b = 10
#
#
# if a < b:
#     print('A is less than 10')
#     for i in range(a, b):
#         print(i)
# elif a == b:
#     print("A is equal to 10")
# else:
#     print('A is greater than b')
#
#

import pandas as pd

pd.options.mode.chained_assignment = None
read_data = pd.read_csv('stock_data.csv', na_values=['??', '???', '????', "?????", 'two'], index_col=0)
print(read_data.info())

read_data.insert(7, "Profit_Class", "")
read_data.insert(8, "Hold_Sell", "")
# print(read_data)
for i in range(0, len(read_data['P&L']), 1):
    if read_data['P&L'][i] < -1000.0:
        read_data['Profit_Class'][i] = "High Loss"
    elif -1000.0 < read_data['P&L'][i] < 0:
        read_data['Profit_Class'][i] = "Small Loss "
    elif read_data['P&L'][i] > 0:
        read_data['Profit_Class'][i] = "High Profit"
        buy_price = read_data["cost"][i]
        quantity = read_data["Qty"][i]
        LTP = read_data["LTP"][i]
        Cal1 = (LTP * quantity) - (buy_price * quantity)
        if Cal1 > 1000:
            read_data['Hold_Sell'][i] = 'Sell'
        elif Cal1 < -1000:
            read_data['Hold_Sell'][i] = 'Immediate Sell'
        else:
            read_data['Hold_Sell'][i] = 'Hold'

print(read_data['Profit_Class'].value_counts())
# with open('new_data.txt', 'w') as data_write:
#     data_write.write(str(read_data))
# 
# print(read_data['P&L'])
# print(read_data)
