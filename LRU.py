def lru(strony, ramka, rozmiar, chybienie, trafienie):
    for i in range(len(strony)):
        if len(ramka) == rozmiar:
            if strony[i] not in ramka:
                del ramka[0]
                ramka.append(strony[i])
                chybienie += 1
            else:
                # print("ramka ktroa dziala", ramka)
                # print("liczba w stronie ktora jest w ramce", strony[i])
                ramka.remove(strony[i])
                ramka.append(strony[i])
                trafienie += 1
        else:
            ramka.append(strony[i])
        print(ramka)
    return trafienie, chybienie

# strona = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
# strony = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
