#przypomnienie git hub, komendy
# git add . -  czyli dodanie pliku do obserwacji
# git commit -m 'wiadomosc' - opis comita
# git push - puszczenie aktualizacji na github

#powtórka  z printów i inputów
# print('Siema')
# input()
# age = int(input('Ile masz lat?  '))
# print(f'Wiec masz {age} lat')
# print(f'Będziesz dorosły za {18 - age} lat')


#Powtórka z while true (czyli rób tak długo dopóki nie wystąpi) oraz z if'a
# while True:
#     age = int(input('Ile masz lat? '))
#     if 0 < age <18:
#         print(f'Wiec masz {age} lat')
#         print(f'Będziesz dorosły za {18 - age} lat')
#         break
#
#     else:
#         print('zły wiek, jeszcze raz')
#
# print('dalsza częsc programu')

#----------------------------------------
#Pandas
import pandas as pd
import numpy as np

#Zasilenie csv
df = pd.read_csv('Pliki_do_cwiczen\\diabetes.csv') #zamiennie możemy stawiać "\\" oraz "/"
# #df = pd.read_csv(r'Pliki_do_cwiczen\diabetes.csv', delimiter=';') #możemy też stosować "r" które oznacza "przeczytaj tą ścieżkę jak jest". Trzeba uważać bo "\n' oznacza exit
# print(df)
# (print(type(df)))
# print(f'wypisuje wszystko:\n{df}')
# print(f'wypisuje typ:\ntype{df}')
# print(f'ilosc danych: {df.shape}\nliczba kolumn: {df.shape[1]}')
# print(f'wypisuje tak, jak chce:\n{df.head(15).to_string()}') #wypisz wszystko
# print(f'opis danych:\n{df.describe().T.to_string()}')#zamiana wierszy z kolumnami. FAJNE!
#
# print(f'ilosc pustych:\n{df.isna().sum()}') #Pokaż ile jest pustych komórek

#--------------------------------------------
#df['bmi'] += 1000 #dodajemy tysiąc do wartości w kolumach
#df['nowa_testowa'] = df['bmi'] / df['glucose'] - 50 * df.shape[1]
#print(f'opis danych:\n{df.describe().T.to_string()}')#zamiana wierszy z kolumnami. FAJNE!

#----------------------------------------
#wszędzie, gdzie są zera lub brak wartości - wpisac średnią (bez zer)
#df['bmi'].replace(0, 10)
#df['bmi'] = df['bmi'].replace(0, np.NaN) #zamiana zer na nulle przy pomocy numpy

for col in ['glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']:
    df[col].replace(0, np.nan, inplace=True) #usuwamy zera
    mean_ = df[col].mean() #liczymy średnią
    df[col].replace(np.nan, mean_, inplace=True) #wpisujemy średnią tam gdzie puste

df.to_csv(r'dane_po_obrobce\cukrzyca_zmodyfikowane.csv', sep=";", index=False) #..\ - oznacza ze przejdź o jeden w górę