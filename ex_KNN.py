# Données d'entraînement
import numpy as np
donnees_entrainement = np.array([[2, 4], [1, 3], [2, 3], [3, 2], [2, 1], [5, 6], [4, 5], [4, 6], [6, 6], [5, 4]])
etiquettes_entrainement = np.array(['blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'orange', 'orange', 'orange', 'orange']) 

def_distance = {}
for i in range(len(donnees_entrainement)):
    if donnees_entrainement[i] in def_distance:
        def_distance[donnees_entrainement[i]].append(etiquettes_entrainement[i])
    else:
        def_distance[donnees_entrainement[i]] = etiquettes_entrainement[i]   
print(def_distance) 
# Nouveau point à prédire 
nouveau_point = np.array([3, 3])

