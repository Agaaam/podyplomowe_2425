#zaladowanie biblioteki pandas
from statistics import linear_regression

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL.GimpGradientFile import linear
from sklearn.linear_model import LinearRegression


#Zasilenie csv
df = pd.read_csv('Pliki_do_cwiczen\\weight-height.csv', delimiter=';')
print(df)
(print(type(df)))

print(df.describe())

df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3))


# print('\nWykres')
# plt.hist(df.Weight, 50)
# plt.show()
#
# plt.hist(df.query('Gender=="Male"').Weight, 50)
# plt.hist(df.query('Gender=="Female"').Weight, 50)
# plt.show()

#biblioteką seaborn można też zrobić histogram ale przy pomocy hist_plot
#print('\nWykresy Seaborn')
# sns.histplot(df.query('Gender=="Male"').Weight)
# # sns.histplot(df.query('Gender=="Female"').Weight)
# # plt.show()

#Zamiana płci na dane numeryczne
df = pd.get_dummies(df)
print(df.head(3))
#usuwanie jednej kolumny
del df['Gender_Male']
print(df.head(3))

#Zamiana nazwy kolumny female na gender only
df=df.rename(columns={'Gender_Female':'Gender'}) #jako mężczyzna=False / kobieta=True
print(df.head(3))

#algorytm
model = LinearRegression()
model_regresji=model.fit(df[['Height','Gender']], df['Weight'])
print(model.coef_) #współczynnik kierunkowy
print(model.intercept_) #wyraz wolny

print(f'Weight = Height * {model.coef_[0]} + Gender * {model.coef_[1]} + {model.intercept_}')