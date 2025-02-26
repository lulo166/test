1.1
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

Q4 = 'fait'
#On peut faire des lancers en prenant un intervale de p, 
#car si on divise p**2 par p, on se retrouve avec p.
#Puis dès que la première balle se casse, on sait dans quel intervale
#il faut lancer la deuxième balle. On lance la deuxième balle jusqu'a ce
#que la deuxième balle se casse, et on a le résultat.

#En tout on lance les deux balles de cette manière.
#On lance la première balle un nombre <= p fois, 
#Puis notre deuxième balle un nombre <= p fois,
#ce qui va être un nombre de lancer plus petit ou égal à 2p.



1.2
Q5 = 'fait'
#1) On dispose de r-1 oeufs, et il reste i-1 étages à tester.

#2) On dispose de r oeufs, et il reste n-i étages à tester.

#3) Non car si l'oeuf ne s'est pas cassé à l'étage i, 
# il ne se cassera pas à l'étage i-1 car c'est un étage plus proche 
# du sol que l'étage i, même chose pour i-2, et etc...
# On dispose de r oeufs, et il reste n-i étages à tester, 
# donc les étages i+1, i+2, etc...

Q6 = 'a faire'
# on sait que L(10,2) = 6, en utilisant la technique de la question 4
# si on utilise l'equation, on a 
# L(10,2) = 1 + min1 ()






