# Code for Python

Підключення до гугл диску
```
from google.colab import drive
drive.mount('/content/drive')
```


```
# шлях до датасету з даними про будинки Мельбурну
melbourne_file_path = '/content/drive/MyDrive/ds/ml/melb_data.csv'

# Створіть об'єкт, який міститиме в собі наш датасет
melbourne_data = pd.read_csv(melbourne_file_path)

```


```
melbourne_data.describe() 
```

```
melbourne_data.head()
```