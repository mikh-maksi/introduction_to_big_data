import numpy as np # linear algebra
import pandas as pd # data processing
import seaborn as sns
import matplotlib.pyplot as plt
import os
#Setting Style for Plotting
plt.style.use('fivethirtyeight')


df = pd.read_csv('/kaggle/input/life-balance/Life Circle Balance.csv')
# print('Dataset dimentions' + str(df.shape))
df.head()