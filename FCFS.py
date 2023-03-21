import random

ilosc_procesow = int(input("Podaj ilosc procesow: "))
procesy = [0] * ilosc_procesow
for i in range(ilosc_procesow):
    procesy[i] = procesy[i] + i + 1
# print(procesy)

przedzial_czasu_nadejscia = int(input("Podaj przedzial losowego generowania czasu nadejscia: "))
czas_nadejscia = [0] * ilosc_procesow
for i in range(ilosc_procesow):
    czas_nadejscia[i] = random.randint(0, przedzial_czasu_nadejscia)
# czas_nadejscia.sort()
# print(czas_nadejscia)

przedzial_czasu_wykonania = int(input("Podaj przedzial losowego generowania czasu wykonania: "))
czas_wykonania = [0] * ilosc_procesow
for i in range(ilosc_procesow):
    czas_wykonania[i] = random.randint(0, przedzial_czasu_wykonania)
# print(czas_wykonania)

#czas_nadejscia, procesy, czas_wykonania = zip(*sorted(zip(czas_nadejscia, procesy, czas_wykonania)))
#czas_nadejscia, procesy, czas_wykonania = (list(t) for t in zip(*sorted(zip(czas_nadejscia, procesy, czas_wykonania))))

suma_wykonania = [0] * ilosc_procesow
czas_czekania = [0] * ilosc_procesow
calkowite_czekania = 0

for i in range(1, ilosc_procesow):
    suma_wykonania[i] = suma_wykonania[i - 1] + czas_wykonania[i - 1]
    czas_czekania[i] = suma_wykonania[i] - czas_nadejscia[i]
    if czas_czekania[i] <= 0:
        czas_czekania[i] = 0

czas_zwrotu = [0] * ilosc_procesow
calkowite_zwrotu = 0

for i in range(ilosc_procesow):
    czas_zwrotu[i] = czas_czekania[i] + czas_wykonania[i]
    calkowite_czekania += czas_czekania[i]
    calkowite_zwrotu += czas_zwrotu[i]

sredni_czas_czekania = calkowite_czekania / ilosc_procesow
sredni_czas_zwrotu = calkowite_zwrotu / ilosc_procesow

print("procesy\t", procesy)
print("czas nadejscia\t", czas_nadejscia)
print("czas wykonania\t", czas_wykonania)
print("suma wykonania\t", suma_wykonania)
print("czas zwrotu\t", czas_zwrotu)
print("czas czekania\t", czas_czekania)
print("sredni czas czekania\t", sredni_czas_czekania)
print("sredni czas zwrotu\t", sredni_czas_zwrotu)
