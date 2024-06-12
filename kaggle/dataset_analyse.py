import numpy as np # linear algebra
import pandas as pd # data processing
import seaborn as sns
import matplotlib.pyplot as plt
import os
#Setting Style for Plotting
plt.style.use('fivethirtyeight')

# path to the Melbourne Houses dataset
melbourne_file_path = '/kaggle/input/melb-data-example-1206/melb_data.csv'

# Create an object that will contain our dataset
melbourne_data = pd.read_csv(melbourne_file_path) 


melbourne_data.describe()



melbourne_data.head()


melbourne_data.columns


y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']



X = melbourne_data[melbourne_features]

X.head()

from sklearn.tree import DecisionTreeRegressor

# Define the module. Specify the number for random_state to ensure the same results every time you run the code
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit the model
melbourne_model.fit(X, y)


print("We make a forecast for the following 5 houses:")
print(X.head())
print("their price predictions are as follows:")
print(melbourne_model.predict(X.head()))


from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)