# faire une fonction qui calcule la moyenne d'une liste de nombre avec un coefficient variable selon les nombres de la liste

def moyenne(liste):
    if float in liste:
         if len(liste) == 0:
             return 0
         else:
            return sum(liste)/len(liste)
    else:
        return "erreur"
