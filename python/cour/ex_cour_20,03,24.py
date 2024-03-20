def enumere(tab):
    for i in range (len(tab)):
        print(i, tab[i])

assert enumere([1, 2, 3]) == {1: [0], 1: 2, 2: 3}