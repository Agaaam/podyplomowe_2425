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
