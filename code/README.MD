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