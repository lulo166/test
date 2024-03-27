def distanceeuclidienne(liste1, liste2):
   distance = 0 # la distance est d'abord nulle
   for i in range(len(liste1)): # pour chaque element de la liste (chaque pixel de l'image)
     distance += (liste1[i] - liste2[i]) ** 2 # a la distance on ajoute la difference au carre entre les deux pixels
   return distance ** 0.5 # on retourne la racine carree de la distance

def knn(images, nouvelle_image, k):
   distances = [] # on initialise une liste vide pour stocker les distances
   for image in images: # pour chaque image dans la liste d'images.
     distances.append((distanceeuclidienne(image, nouvelle_images), image)) # on ajoute a la liste des distances la distance euclidienne entre l'image et la nouvelle image.
   distances.sort(key=lambda x: x[0]) # on trie la liste des distances par ordre croissant
   voisins = [distance[1] for distance in distances[:k]] # on prend les k premiers elements de la liste des distances
   return voisins # on retourne la liste des k voisins

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
nouvelle_images = [7, 8, 9]
print(knn)
