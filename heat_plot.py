import pandas as pd
import seaborn as sns

readed_data2 = pd.read_csv('Toyota.csv', index_col=0, na_values=(['??', "????"]))


readed_data = readed_data2.copy(deep=True)


# readed_data['F']
ct = pd.crosstab(index=readed_data["Automatic"], 
                 columns=readed_data['FuelType'],
                 dropna=True)


ct = pd.crosstab(index=readed_data["Automatic"], 
                 columns=readed_data['FuelType'],
                 margins=True,
                 normalize='index',
                 dropna=True)
print(ct, '\n\n\n\n')


ct = pd.crosstab(index=readed_data["Automatic"], 
                 columns=readed_data['FuelType'],
                 margins=True,
                 normalize='columns',
                 dropna=True)
print(ct)


numerical_data = readed_data.select_dtypes(exclude='object')
corr = (numerical_data.corr())
print(corr)


sns.pairplot(readed_data, kind="scatter", hue='FuelType')
plt.show()
# Data frame is collection of data
# copied_data = readed_data.copy(deep=True)

# print(copied_data)

# print(copied_data.shape)

# print(copied_data.ndim)
# print(copied_data.head(10))
# print(copied_data.tail(10))
# print(copied_data.at[4, "FuelType"])
# print(copied_data.iat[4,1])
# print(copied_data.loc[1, ["FuelType", "HP", "CC"]])


# print(copied_data.info())
# # print(copied_data.dtypes)
# # print(copied_data.select_dtypes(include=object, exclude=None))
# print(copied_data.select_dtypes(exclude=object))
# print(copied_data.select_dtypes(exclude=object).info())
# unique = np.unique(copied_data["KM"])
# print(np.unique(copied_data["KM"]))
# doors = np.unique(copied_data["Doors"])
# print(np.unique(copied_data["Doors"]))
# copied_data["MetColor"] = copied_data["MetColor"].astype('object')
# print(copied_data.info())
# # copied_data['Doors'].replace([o])
# print(copied_data['FuelType'].nbytes)
# print(copied_data["FuelType"].astype('category').nbytes)



# def replacea(data_frame, column_name, list_to_find, list_to_replace):
#     for i in range(0, len(data_frame[column_name])):
#         data_frame[column_name].replace(list_to_find[i], list_to_replace[i], inplace=True)
#     return data_frame        
        
        
        
# copied_data["Doors"].replace("three", 3, inplace=True)
# copied_data["Doors"].replace("four", 4, inplace=True)
# copied_data["Doors"].replace("five", 5, inplace=True)
# print(copied_data.info())
# copied_data["Doors"] = copied_data["Doors"].astype('int64')

# print(copied_data.info())

# print(copied_data.isnull().sum())

# copied_data.insert(10, "Price_Class", "")

# for i in range(0, len(copied_data['Price']), 1):
#     if copied_data['Price'][i] <= 8450:
#         copied_data['Price_Class'][i]='Low'
#     if copied_data['Price'][i] > 11950:
#         copied_data['Price_Class'][i]='High'
#     else:
#         copied_data['Price_Class'][i]='Medium'


# replacea(copied_data, 'Doors', [3, 5], [100, 105])

# print(copied_data)


