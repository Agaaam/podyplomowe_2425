#regresja liniowa
from statistics import linear_regression

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression



df = pd.read_csv('Pliki_do_cwiczen\\AI\\weight-height.csv')
print(df.head(5))

print(df.Gender.value_counts())

df.Height *= 2.54 #przemnażamy całą kolumnę aby były cm
print(f'Po zmianie jednostek: \n{df.head(5)}')

df.Weight /= 2.2 #przemnażamy całą kolumnę aby były kg
print(f'Po zmianie jednostek: \n{df.head(5)}')

#niezależne 2 kolumny - gender i height. Wynik weight
#wszystkie płcie
# plt.hist(df.Weight, bins=50)
# plt.show()


#osobno panie i panowie na jednym wykresie. Aby były dwa osobne to musimy uruchomish zahaszowany kod
# plt.hist(df.query("Gender=='Male'").Weight, bins=50)
# #plt.show() #
# plt.hist(df.query("Gender=='Female'").Weight, bins=50)
# plt.show()

df = pd.get_dummies(df) #usuwam dane nienumeryczne
print(df.head())
del df['Gender_Male'] #usuwa kolumne
print(df.head())

df.rename(columns={'Gender_Female': 'Gender'}, inplace=True) #wykonaj w locie
print(df.head())

#dane na stole
#Gender 0 - mezczyzna, 1 - kobieta
model = LinearRegression()
model.fit(df[['Height','Gender']], df['Weight'])


print(f'Wspolczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')
print(f'Waga = wzrost * 1.06 + plec * (-8.8) + (-102,5)')

#Sprawdzenie
print(model.predict([[192,0], [167,1], [80,1]]))