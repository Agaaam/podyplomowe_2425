#regresja liniowa

import pandas as pd

df = pd.read_csv('Pliki_do_cwiczen\\AI\\weight-height.csv')
print(df.head(10))

print(df.Gender.value_counts())