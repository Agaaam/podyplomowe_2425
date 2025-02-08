import pandas as pd
import numpy as np

df = pd.read_csv('Pliki_do_cwiczen\\AI\\iris.csv')
print(df.describe().T.to_string())