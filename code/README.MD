# Code for Python

Підключення до гугл диску
```
from google.colab import drive
drive.mount('/content/drive')
```


```
import pandas as pd
# шлях до датасету з даними про будинки Мельбурну
file_path = '/content/drive/MyDrive/ds/melb_data.csv'

# Створіть об'єкт, який міститиме в собі наш датасет
data = pd.read_csv(file_path)

```


```
data.head()
```

```
data.describe()
```

```
data_encoded = pd.get_dummies(data, drop_first=True)
corr_matrix = data_encoded.corr()
```
```
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(corr_matrix)
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Кореляційна матриця (з кодуванням категорій)")
plt.tight_layout()
plt.show()
```