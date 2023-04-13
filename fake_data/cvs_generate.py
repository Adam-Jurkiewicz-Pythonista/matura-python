import csv
from faker import Faker
from random import random


def i(n=10000):
    return int(random() * n)

with open("dane_testowe.txt", mode='w') as f:

    for lang in ("pl_PL", "it_IT", "jp_JP", "ru_RU", "sl_SI", "sv_SE" , "tw_GH", "de_DE"):
        dane = Faker(lang)




        # plik_danych.writerow(["Imię i nazwisko", "m^2 pow", "Gaz", "Prąd", "Czynsz", "Woda", "Śmieci"])
        for _ in range(3):
            f.write(f"{dane.name()}, {dane.address()},zawód: {dane.job()}, zatrudnienie w: {dane.company()} \n")
            f.write(f"Tel.: {dane.phone_number()} \n")
            f.write("------\n")