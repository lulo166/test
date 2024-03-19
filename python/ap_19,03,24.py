def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui represente par s en appliquant le procede de lecture, je suis le plus fort''' 
    # ceci est du doc string, donc si tu fait print(help(la fonction)), cette phrase va etre emise, python a ca pour ses fonctions.
    resultat = ''
    chiffre = s[0] # recupere la valeur dans la liste s a l'index 0.
    compte = 1
    for i in range(1, len(s)): # pour chaque element dans la liste s
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = compte
            ...
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat        

print(help(nombre_suivant))
