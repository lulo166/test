def enumere(tab):
    d = {}
    for i in range (len(tab)):
        d[tab[i]] = [i]
    print(d)

assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}
assert enumere([]) == {}