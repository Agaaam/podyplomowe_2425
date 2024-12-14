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
while True:
    age = int(input('Ile masz lat? '))
    if 0 < age <18:
        print(f'Wiec masz {age} lat')
        print(f'Będziesz dorosły za {18 - age} lat')
        break

    else:
        print('zły wiek, jeszcze raz')

print('dalsza częsc programu')