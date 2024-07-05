def recherche0(elt, tab):
    resultat = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            resultat = i
            break
    return resultat

def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(tab)
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l

def selection_enclos(table_animaux, num_enclos):
    l = []
    for i in range(len(table_animaux)):
        if table_animaux[i]['enclos'] == num_enclos:
            l.append(table_animaux[i])
    return l
    
def recherche1(tab, n):
    l = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            l = i
    return l

from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = distance(depart, point)
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
             point = tab[i]
             min_dist = distance(tab[i], depart)
    return point

assert plus_coute_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"

# rajoute des assert si tu as le temps.