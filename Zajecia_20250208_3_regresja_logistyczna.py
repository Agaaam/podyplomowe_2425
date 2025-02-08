from operator import index

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


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

X = df.iloc[: , :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #dane testowe to 20% bazy

model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test)))) #Weź X testowe i zwróć mi wyniki czyli Y a potem to razem z prawdziwymi wynikami ładuje do confusion matrix i rób z tego ramkę danych
print(df.outcome.value_counts())

print('Zmiana danych')
df1 = df.query("outcome==0").sample(n=500)
df2 = df.query("outcome==1").sample(n=500)
df3 = pd.concat([df1, df2])

print(df3.describe().T.to_string())
print(df3.outcome.value_counts())

X = df3.iloc[: , :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #dane testowe to 20% bazy

model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test)))) #Weź X testowe i zwróć mi wyniki czyli Y a potem to razem z prawdziwymi wynikami ładuje do confusion matrix i rób z tego ramkę danych

