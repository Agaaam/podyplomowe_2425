import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('Pliki_do_cwiczen\\AI\\otodom.csv')
print(df.head(5))

print(df.describe().T.to_string()) #T - oznacza transpozycje macierzy

sns.heatmap(df.iloc[:, 1:].corr(), annot=True) #wykres korelacji gdzie omijamy kolumnę z ID
plt.show()

sns.histplot(df.price)
plt.show()

plt.scatter(df.space, df.price)
plt.show()

Q3 = df.describe().T.loc['price','75%']
print(Q3)

df1 = df[df.price <= Q3]
plt.hist(df1.price, bins=50)
plt.show()

#dzielimy dane na próbę i bazę czyli uczymy sie na train
X = df1.iloc[: , 2:]
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #dane testowe to 20% bazy

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test)) #weź te x testowe i y testowe i przepuśc przez model i porównaj z wynikami jakie masz
print(pd.DataFrame(model.coef_, X.columns))


print('drzewo decyzyjne')
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model. fit(X_train, y_train)
print(model.score(X_test, y_test))
