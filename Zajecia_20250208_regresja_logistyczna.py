import pandas as pd
import numpy as nd

df = pd.read_csv('Pliki_do_cwiczen\\AI\\diabetes.csv')
print(df.describe().T.to_string())
