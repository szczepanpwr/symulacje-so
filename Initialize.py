import random


def self_init():
    rozmiar = int(input("\nPodaj rozmiar ramki: "))
    dlugosc_stron = int(input("Podaj długośc listy z numerami stron: "))
    strony = [0] * dlugosc_stron
    ramka = []
    trafienie = 0
    chybienie = 0

    for i in range(dlugosc_stron):
        liczba = int(input("Podaj liczbe: "))
        strony.append(liczba)

    return strony, ramka, rozmiar, chybienie, trafienie


def auto_init():
    rozmiar = int(input("\nPodaj rozmiar ramki: "))
    dlugosc_stron = int(input("Podaj długośc listy z numerami stron: "))
    przedzial_stron = int(input("Podaj przedział losowo generowanego numerów stron: "))
    # strony = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    # strony = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0]
    strony = [0] * dlugosc_stron
    ramka = []
    trafienie = 0
    chybienie = 0

    for i in range(dlugosc_stron):
        strony[i] = random.randint(0, przedzial_stron)

    return strony, ramka, rozmiar, chybienie, trafienie, dlugosc_stron, przedzial_stron


def wynik(trafienie, chybienie):
    print("\nTrafienia = ", trafienie, "\nChybienia = ", chybienie)
