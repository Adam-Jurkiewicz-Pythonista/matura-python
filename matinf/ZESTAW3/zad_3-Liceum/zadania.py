# wczytujemy wszystkie informacje z pliku zewnętrznego, będziemy mogli z nich korzystać
import json
from dane import *
print(przedmioty)

with open("oceny.txt") as dane:
    dane_wczytane = dane.readlines()

# print(dane_wczytane)
# przykładowe dane:
# [
# 'OU geo 6\n',
# 'EP jpo 6 3 2 5 5 6 1\n',
# 'OH fiz 1 4 1 1 4\n',
# 'JO wos 2 6 5 4 2 6\n'
# ]

# teraz czyścimy wstępnie
dane_czyste = []
for wiersz in dane_wczytane:
    dane_czyste.append(wiersz.strip().split())

# print(dane_czyste)
# przykładowe dane:
# [
# ['OU', 'geo', '6'],
# ['EP', 'jpo', '6', '3', '2', '5', '5', '6', '1'],
# ['OH', 'fiz', '1', '4', '1', '1', '4'],
# ['JO', 'wos', '2', '6', '5', '4', '2', '6']
# ]

print(f"Łącznie wczytano danych: {len(dane_czyste)}.")


# teraz zaczniemy odpowiedzi na pytania

# 3.1 - ile osób bez ocen?
bez_ocen = 0
for element in dane_czyste:
    if len(element) == 2:
        bez_ocen += 1
        print(f"Bez ocen osoba: {element[0]}")
else:
    print(f"Bez ocen osób: {bez_ocen}")

# 3.2 - ile osób aktywnych?
osoby_aktywne = {"INICJAŁY": [] }
ile_aktywnych = 0

for element in dane_czyste:
    inicjaly = element[0]
    przedmiot = element[1]
    if inicjaly not in osoby_aktywne:
        osoby_aktywne[inicjaly] = []

    (osoby_aktywne[inicjaly]).append(przedmiot)

print(json.dumps(osoby_aktywne, indent=3))

for osoba in osoby_aktywne:
    przedmioty = set(osoby_aktywne[osoba])
    if len(przedmioty) >= 2:
        ile_aktywnych += 1
        print(f"Aktywna osoba: {osoba}")
else:
    print(f"Sumarycznie aktywnych osób: {ile_aktywnych}")

