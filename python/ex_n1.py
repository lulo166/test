# tab est une liste, elt est un élément de tab, cette partie sert a déclarer les variables qui sont dans la liste.

def recherche(elt,tab): 
    val = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            val = i
        #else : # ces deux lignes sont CONTRE PRODUCTIVES.
            #return None
    return val

assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5