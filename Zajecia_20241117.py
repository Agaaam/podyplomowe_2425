#zaladowanie biblioteki pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Zasilenie csv
df = pd.read_csv('Pliki_do_cwiczen\\weight-height.csv', delimiter=';')
print(df)
(print(type(df)))

print(df.describe())

df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3))


print('\nWykres')
plt.hist(df.Weight)
plt.show()
