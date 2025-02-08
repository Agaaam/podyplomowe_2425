#regresja liniowa
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Pliki_do_cwiczen\\AI\\weight-height.csv')
print(df.head(5))

print(df.Gender.value_counts())

df.Height *= 2.54 #przemnażamy całą kolumnę aby były cm
print(f'Po zmianie jednostek: \n{df.head(5)}')

df.Weight /= 2.2 #przemnażamy całą kolumnę aby były kg
print(f'Po zmianie jednostek: \n{df.head(5)}')

#niezależne 2 kolumny - gender i height. Wynik weight
#wszystkie płcie
plt.hist(df.Weight, bins=50)
plt.show()
#osobno panie i panowie na jednym wykresie. Aby były dwa osobne to musimy uruchomish zahaszowany kod
plt.hist(df.query("Gender=='Male'").Weight, bins=50)
#plt.show() #
plt.hist(df.query("Gender=='Female'").Weight, bins=50)
plt.show()
