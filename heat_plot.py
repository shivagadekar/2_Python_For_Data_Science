import pandas as pd
cars_data= pd.read_csv("Toyota.csv", index_col=0, na_values=["??", "????"])
cars_data2 = cars_data.copy()
# pd.crosstab(index=cars_data2['FuelType'],columns=cars_data2['Automatics]', dropna=True)
numerical_data = cars_data2.select_dtypes(exclude=[object])
corr_matrix = numerical_data.corr()