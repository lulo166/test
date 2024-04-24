def recherche_motif(motif, texte):
    position = []
    l = len(motif)
    for i in range(len(texte)):
        for j in range(len(motif)):
            if texte[i+j] != motif[j]:
                break
        position.append(i)
    return position

