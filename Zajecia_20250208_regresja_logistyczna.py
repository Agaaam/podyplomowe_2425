from operator import index

import pandas as pd
import numpy as np

df = pd.read_csv('Pliki_do_cwiczen\\AI\\diabetes.csv')
print(df.describe().T.to_string())

#wpisać wartości średnie (bez zer) tam gdzie jest null
for col in ['glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']:
#Usunąc zera
    df[col].replace(0, np.nan, inplace=True) #usuwamy zera, inplace czyli w locie
#liczymy średnią
    mean_ = df[col].mean() #liczymy średnią per columna
#Wpisujemy średnia tam gdzie brak wartości
    df[col].replace(np.nan, mean_, inplace=True) #wpisujemy średnią tam gdzie puste i robimy to w locie

print('Po czyszczeniu')
print(df.describe().T.to_string())

df.to_csv('Pliki_do_cwiczen\\AI\\cukrzyca_poprawiona.csv', index=False)