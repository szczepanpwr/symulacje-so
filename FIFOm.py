def fifo(strony, ramka, rozmiar, chybienie, trafienie):
    for i in range(len(strony)):
        if len(ramka) < rozmiar:
            if strony[i] not in ramka:
                ramka.append(strony[i])
        else:
            if strony[i] not in ramka:
                del ramka[0]
                ramka.append(strony[i])
                chybienie += 1
            else:
                # print("ramka ktroa dziala", ramka)
                # print("liczba w stronie ktora jest w ramce", strony[i])
                trafienie += 1
        print(ramka)
    return trafienie, chybienie
