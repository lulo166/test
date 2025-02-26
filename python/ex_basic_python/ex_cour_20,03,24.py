def enumere(tab):
    d = {} # creation du dictionnaire
    for i in range (len(tab)):
        if tab[i] in d: # if the value is already in the dictionary
            d[tab[i]].append(i) # append si la valeur est deja dans le dictionnaire.
        else:
           d[tab[i]] = [i]
    return d # ALWAYS use return instead of print.

assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([]) == {}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

# code alternatif
# def enumere(tab):
#     d = {}
#     for i,j in enumerate(tab): # enumerate est un fonction built-in qui retourne un tuple (index, valeur). i, j est un tuple
#         if j in d:
#             d[j].append(i)
#         else:
#             d[j] = [i]
#     return d
