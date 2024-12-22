Q1 = 'Done'
def verif_etage_critique(c):
    if lacher(c-1) == False:
        if lacher(c) == True:
            return True
    else:
        return False

Q2 = 'Done'
def critique_un_seul_oeuf(n):
    for i in range(1, n + 1):
        if lacher(i) == True:
            return i
    return n + 1

Q3 = 'Done'
#1)
#on peut faire une recherche dichotomique car les étages sont en ordre.
#de plus, comme la compléxité d'une recherche par dichotomie est de log2 n, on sait que l'on n'aura pas de problèmes avec le nombre d'oeuf

#2)
#log2 n

#3)  
def critique_dichotomie(n):
    low = 1
    high = n
    if n == 1:
        if lancer(n):
            return n
        else:
            return n+1
    if lancer(n) == False:
        return n + 1
    while low != high:
        if lancer((low + high)//2):
            high = (low + high)//2
        else:
            low = (low + high)//2
    return high

#4)  
# on sait que le cas supérieur (donc n+1) est considérer,
#et que le cas n = 1 est pris en compte
#ca marche car les valeurs changent tout le temps sauf si elles sont égales,
#car la division reduit les deux valeurs vers un seul même valeur
#et quand elles deviennent égales, la boucle s'arrête.

Q4 = 'a faire'


