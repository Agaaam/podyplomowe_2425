#Lista:
do_kupienia = ['marchew','chleb','maslo','mleko']
print(do_kupienia)

#Pętla FOR oznacza że "i" będzie wywoływane 5 razy, od 0 do 4
for i in range(5):
    print(i)

#przykład użycia z nasza listą:
for i in range(len(do_kupienia)):
    print(do_kupienia[i])

for produkt in do_kupienia:
    print(produkt)

#---------------------------------------------------------------------------
#Zadanie
#Napisz program co faktycznie chcesz kupic (czyli różnica dwóch list)

do_kupienia = ['marchew','chleb','maslo','mleko']
w_domu = ['miod','chleb','mleko','pomidor','sok']

#1.spoosob
for produkt in do_kupienia:
    if produkt in w_domu:
        print (f'Nie kupuj {produkt}')
    else:
        print(f'kup {produkt}')

#2.wersja
for produkt in do_kupienia:
    mam = False
    for item in w_domu:
        if produkt == item:
            mam = True
            print(f'Nie kupuj {produkt}')
    if mam == False:
        print(f'Kup {produkt}')



