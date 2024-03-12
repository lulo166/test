#la première ligne de la fonction montre les parametres globaux utilisés dans la fonction.
def maxliste(liste):
    #liste = [] cette ligne est contre productive car elle change la liste en une liste vide.
    max_val = 0 # la variable max_val est une variable locale qui agit simplement sur la fonction.
    for i in range(len(liste)):
        if liste [i] > max_val:
            max_val = liste[i]
    return max_val

assert maxliste([98, 12, 104, 23, 131, 9]) == 131
assert maxliste([-27, 24, -3, 15]) == 24