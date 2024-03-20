def enumere(tab):
    d = {}
    for i in range (len(tab)):
        d[tab[i]] = [i]
    print(d)

enumere([1, 2, 3])