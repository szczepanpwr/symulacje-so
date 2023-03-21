import Initialize
import FIFOm
import LRU

while True:
    file = open("wyniki.txt", "a")
    wybor = int(input("\nWybierz algorytm zastępowania stron\n"
                      "1. FIFO - First In First Out\n"
                      "2. LRU - Least Recently Used\n"
                      "3. Wyjście\n\n"))
    if wybor == 1:
        file.write("\nAlgorytm FIFO")
        wybor2 = int(input("\nWybierz rodzaj wprowadzania danych do stron\n"
                           "1. Automatycznie (losowo)\n"
                           "2. Ręcznie\n\n"))
        if wybor2 == 1:
            strony, ramka, rozmiar, chybienie, trafienie, dlugosc_stron, przedzial_stron = Initialize.auto_init()
            trafienie, chybienie = FIFOm.fifo(strony, ramka, rozmiar, chybienie, trafienie)
            Initialize.wynik(trafienie, chybienie)
        elif wybor2 == 2:
            strony, ramka, rozmiar, chybienie, trafienie = Initialize.self_init()
            trafienie, chybienie = FIFOm.fifo(strony, ramka, rozmiar, chybienie, trafienie)
            Initialize.wynik(trafienie, chybienie)
        else:
            print("\nTaki wybor nie istnieje")
    elif wybor == 2:
        file.write("\nAlgorytm LRU")
        wybor2 = int(input("\nWybierz rodzaj wprowadzania danych do stron\n"
                           "1. Automatycznie (losowo)\n"
                           "2. Ręcznie\n\n"))
        if wybor2 == 1:
            strony, ramka, rozmiar, chybienie, trafienie, dlugosc_stron, przedzial_stron = Initialize.auto_init()
            trafienie, chybienie = LRU.lru(strony, ramka, rozmiar, chybienie, trafienie)
            Initialize.wynik(trafienie, chybienie)
        elif wybor2 == 2:
            strony, ramka, rozmiar, chybienie, trafienie = Initialize.self_init()
            trafienie, chybienie = LRU.lru(strony, ramka, rozmiar, chybienie, trafienie)
            Initialize.wynik(trafienie, chybienie)
        else:
            print("\nTaki wybor nie istnieje")
    elif wybor == 3:
        break
    file.write("\nStrony: ")
    file.write(str(strony))
    file.write("\nTrafienia: ")
    file.write(str(trafienie))
    file.write("\nChybienia: ")
    file.write(str(chybienie))
    file.close()
