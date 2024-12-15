#Podsumowanie pandas
import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv('plik.csv')

# Wczytanie z pliku Excel (xlsx)
df_excel = pd.read_excel('plik.xlsx', sheet_name='Arkusz1')

df.head()      # Domyślnie wyświetla 5 pierwszych wierszy
df.head(10)    # Wyświetla 10 pierwszych wierszy

df.tail()      # Domyślnie wyświetla 5 ostatnich wierszy
df.tail(10)    # 10 ostatnich wierszy

df.info()      # Wyświetla liczbę wierszy, kolumn, typy danych oraz liczbę niepustych rekordów w każdej kolumnie

df.describe()  # Opis statyczny

df['nazwa_kolumny'] #zwraca series z danej kolumny
df[['kolumna1', 'kolumna2']] #zwraca Data Frame z wybranych kolumn

df[df['kolumna'] == 'wartość']
df[df['kolumna'] > 10]
df[(df['kolumna'] > 5) & (df['kolumna2'] == 'abc')]

df.loc[0:10, ['kolumna1', 'kolumna2']] #wiersze od 1 do 10, tylko dwie kolumny
df.iloc[0:10, 0:2] #wierswza od 0 do 10, kolumny od 0 do 2
