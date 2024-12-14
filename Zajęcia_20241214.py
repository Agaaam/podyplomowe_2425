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

#Zasilenie csv
df = pd.read_csv('Pliki_do_cwiczen\\diabetes.csv') #zamiennie możemy stawiać "\\" oraz "/"
#df = pd.read_csv(r'Pliki_do_cwiczen\diabetes.csv', delimiter=';') #możemy też stosować "r" które oznacza "przeczytaj tą ścieżkę jak jest". Trzeba uważać bo "\n' oznacza exit
print(df)
(print(type(df)))
print(f'wypisuje wszystko:\n{df}')
print(f'wypisuje typ:\ntype{df}')
print(f'ilosc danych: {df.shape}\nliczba kolumn: {df.shape[1]}')
print(f'wypisuje tak, jak chce:\n{df.head(15).to_string()}') #wypisz wszystko
print(f'opis danych:\n{df.describe().T.to_string()}')#zamiana wierszy z kolumnami. FAJNE!

print(f'ilosc pustych:\n{df.isna().sum()}') #Pokaż ile jest pustych komórek