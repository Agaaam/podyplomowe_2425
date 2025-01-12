#Pętla while - działa w nieskończoność a IF zadziała tylko raz

# x = 0
# while x < 5:
#     print('Wykonuje kod')
#     x += 1 #dodaj do 1 x
#
# print('koniec')
#
# passwd = '1234'
# user_passwd = input('Podaj haslo: ')
# while user_passwd != passwd:
#     user_passwd = input('Podaj haslo: ')
# print('haslo poprawne')


#Pętla while true
# standard_username = 'Agnieszka'
# standard_passwdr = '1234'
#
# username = input('Podaj nazwe: ')
# passwd = input('Podaj haslo:')
# while username != standard_username or passwd != standard_passwdr:
#     print('Zle dae')
#     username = input('Podaj nazwe: ')
#     passwd = input('Podaj haslo:')
# print('Zalogowano')


# standard_username = 'Agnieszka'
# standard_passwdr = '1234'
# service_passw = 'service'
# a = 0
#
# username = input('Podaj nazwe: ')
# passwd = input('Podaj haslo:')
#
# while True:
#     if username == standard_username and passwd == standard_passwdr:
#         break
#     elif passwd == service_passw:
#         break
#
#     print('Zle dane')
#     username = input('Podaj nazwe: ')
#     passwd = input('Podaj haslo:')
#
# print('Zalogowano')


#---------------------------------
#Program losuje liczbę a użytkownik ją zgaduję. Program informuje, czy za dyżo czy za mało czy ok
#do losowania liczb służy bilbioteka random
# import random
#
# liczba = random.randint(0, 100)
#
# while True:
#     liczba_uzytkownika = int(input('Podaj liczbe: '))
#
#     if liczba_uzytkownika == 9999:
#         print('Tryb tajny')
#         passwd = input('Wpis haslo: ')
#         if passwd == 'Merito':
#             break
#     if liczba_uzytkownika > liczba:
#         print('za dużo')
#     elif liczba_uzytkownika < liczba:
#         print('za malo')
#     else:
#         print('ok')
#         break

#-------------------------------------------------------------------------------------------------
#Słownik
# uzytkownicy = ['Kamil', 'python123','Monia','Monia1', 'Monia']
# hasla = ['123','asfaff34','Piesek','1234', 'dsfs']
#
# users = {'Kamil':'123',
#          'python123':'asfaff34',
#          'Monia':'Piesek',
#          'Monia1':'1234'
#          }
# print(users['Kamil'])
# users['Mariusz'] = '456' #dodaj
# users['Monia'] = 'Kotek' #nadpisz wartość
# print(users)

#Zadanie ze słownikiem
#Stwórz baze uzytkowników gdzie każdy uzytkownik ma mieć "imie", "nazwisko", "wiek"
#Baza to lista a użytkownik to słownik

# emp1 = {'imie': ' Anna', 'Nazwisko': 'Kowalska', 'wiek':18}
# emp2 = {'imie': ' Anna', 'Nazwisko': 'Nowak', 'wiek':15}
#
# user_database = [emp1, emp2]
# print(user_database[1]['Nazwisko'])
#
# wiek_suma = 0
# sredni_wiek = 0
#
# for user in user_database:
#     user['mail']=user['imie']+'.'+ user['Nazwisko']+'@merito.pl'
#     wiek_suma += user['wiek']
# sredni_wiek = wiek_suma / len(user_database)
# print(f'sredni-wiek {sredni_wiek}')
# print(user_database)

#--------------------------------------------
#Kolejne zadanie ze słownikiem
# zakupy = {'chleb': 4, 'maslo': 1, 'sok': 2, 'jabko': 5}
#
# ceny_lidl = {'chleb': 2.5, 'maslo': 9, 'sok': 4.7, 'jabko': 5, 'kurczak': 9.98}
# ceny_aldi = {'chleb': 6, 'maslo': 7, 'sok': 0.99, 'jabko': 7, 'kurczak': 13}
# ceny_dino = {'chleb': 4, 'maslo': 4, 'sok': 9.99, 'jabko': 0, 'kurczak': 14}
#
# total_lidl = 0
# total_aldi = 0
# total_dino = 0
# # gdzie najtaniej?
# for produkt in zakupy.keys():
#     print(produkt)
#     print(f'Cena {produkt} w lidlu wynosi: {ceny_lidl[produkt]}')
#     total_lidl += ceny_lidl[produkt] * zakupy[produkt]
#     total_aldi += ceny_aldi[produkt] * zakupy[produkt]
#     total_dino += ceny_dino[produkt] * zakupy[produkt]
#
# print(f'Lidl: {total_lidl}')
# print(f'Aldi: {total_aldi}')
# print(f'Dino: {total_dino}')

#---------------------------------------------------------------------------------------------------------
#Funkcje
NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# # sprawdźmy, ile osób chorowało w ostatnim roku na krzykach
# print(f'\nChorzy w ostatnim roku na krzykach: {chorzy_rok & krzyki}')
# print(f'ilość: {len(chorzy_rok & krzyki)}')
#
# # sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
# print(f'\nChorzy w ostatnim roku na krzykach: {krzyki & chorzy_rok}')
# print(f'ilość: {len(krzyki & chorzy_miesiac)}')
#
# # sprawdźmy, ile osób chorowało w ostatnim miesiącu w centrum
# print(f'\nChorzy w ostatnim miesiącu w centrum {centrum & chorzy_miesiac}')
# print(f'Ilość {len(centrum & chorzy_miesiac)}')
#
# # sprawdźmy, ile osób mieszka w sumie w centrum i na krzykach
# print(f'\nMieszkańcy centrum i krzyków: {krzyki | centrum}')
# print(f'Ilosc {len(krzyki | centrum)}')

#------------------------------------------------------------------------