import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


unique_values = data['whoAmI'].unique()


one_hot_data = pd.DataFrame(columns=unique_values)


for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

# Вывод преобразованного DataFrame
one_hot_data.head()
print(one_hot_data)