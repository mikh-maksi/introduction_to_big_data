import numpy as np # linear algebra
import pandas as pd # data processing
import seaborn as sns
import matplotlib.pyplot as plt
import os
#Setting Style for Plotting
plt.style.use('fivethirtyeight')


df = pd.read_csv('c:/work/introduction_to_big_data/kaggle/LifeCircleBalance.csv')
# print('Dataset dimentions' + str(df.shape))
print(df.head())
print(df['Points for today'][0:8])