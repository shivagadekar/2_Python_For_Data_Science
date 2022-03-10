# Data Visualization
# scatter plot
# Histogram
# Bar Plot
# matplotlib - Creates 2D graphs and plots
# Pandas Visualization - Easy to use interface , built on mat plot lab
# seaborn - Provides high level interface for drawing attractive, informative statistical graphics
# ggplot - based on R's ggplot2, uses Grammar of graphics
# ploty - can create interactive plots

import matplotlib.pyplot as plt  # To dp visualization
import numpy as np
import pandas as pd  # To work with data frames

# Scatter Plot


read_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])
read_data.dropna(axis=0, inplace=True)

# print(read_data.size)

# Scatter Plot

plt.scatter(read_data['Age'], read_data['Price'], c='red')
plt.title('Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()

Histogram

plt.hist(read_data['KM'],
          color= 'green',
          edgecolor= 'white',
          bins= 20)
plt.show()


# Bar plot
counts = [979, 120, 12]
fuelType = ('Petrol', 'Diesel', 'CNG')
index = np.array(len(fuelType))

plt.bar(index, counts, color=['red', 'blue', 'cyan'])
plt.title('Bar Plot')
plt.xlabel('Fuel  Types')
plt.ylabel('Frequency')
plt.xticks(index, fuelType, rotation = 90)
plt.show()
