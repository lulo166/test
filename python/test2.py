def distanceeuclidienne(liste1, liste2):
   distance = {} # la distance est d'abord nulle
   for i in range(len(liste1)): # pour chaque element de la liste (chaque pixel de l'image)
     distance += (liste1[i] - liste2[i]) ** 2 # a la distance on ajoute la difference au carre entre les deux pixels
   return distance ** 0.5 # on retourne la racine carree de la distance