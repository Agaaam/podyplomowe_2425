import pandas as pd
import numpy as np
from pandas import value_counts
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('Pliki_do_cwiczen\\AI\\iris.csv')
print(df.head(5))
print(df['class'].value_counts())
print(df.describe().T.to_string())

species = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
df['class_value'] = df['class'].map(species) #tworzymy nową kolumnę z zmapowanymi wartościami (taki słownik)
print(df)
sample = [5.6, 3.2, 5.2, 1.45]

sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, c='r')
plt.show()

sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

print('Klasyfikator')
X = df.iloc[:, 2:4]
y =  df.class_value

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) #dane testowe to 20% bazy

model = KNeighborsClassifier(100, weights='distance') #uniform, distance
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test)))) #Weź X testowe i zwróć mi wyniki czyli Y a potem to razem z prawdziwymi wynikami ładuje do confusion matrix i rób z tego ramkę danych

results = []
for k in range (1, 101):
    model = KNeighborsClassifier(n_neighbors=k, weights='distance')
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.plot(range(1,101), results)
plt.show()