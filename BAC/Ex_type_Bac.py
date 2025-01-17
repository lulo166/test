#ex 3
#2)
# AE ED
#3)a finir
[[0, 4, 0, 0, 4, 0, 0],
 [4, 0, 0, 0, 0, 7, 5]
 ]
#4)a finir
g2 = {'A':['B', 'C', 'H'],
    'B':['B', 'C', 'H'],
    'C':['B', 'C', 'H'],
    'D':['B', 'C', 'H'],
    'A':['B', 'C', 'H'],
    'A':['B', 'C', 'H'],
    'A':['B', 'C', 'H'],
    'A':['B', 'C', 'H']}
#5)
#A, B, C, H, I, D, E, G, F 
#6)
#Car elle s'appelle elle-même
#7)
#Le but de cette fonction est de trouver tous les itinéraires possibles.
#8)
def itineraires_court(G,dep,arr):
    cherche_itineraires(G, dep, arr)
    tab_court = []
    mini = float('inf') # valeur infinie
    for v in tab_itineraires:
        if len(v) <= mini :
            mini = len(v)
    for v in tab_itineraires:
        if len(v) == mini:
             tab_court.append(v)
    return tab_court

#9)
#Le problème est que tab_itineraire ne se resset pas a la fin de l'execution de la fonction itinéraire court, ce qui signifie que pour la deuxième execution du programme, on va trouver les itinéraires pour cette execution, mais aussi ceux pour les excutions d'avant, ce qui signifie qu'on va se retrouver avec des itinéraires qui n'appartiennent pas cette execution, et qui peut fausser les résultats.

#10)
#Car on piocher les informations qui sont importantes a ce moment même, et ignorer les autres.
#et il ne faut pas lire toute les informations pour trouver celles qui sont importantes

#11) souligne la clé primaire, puis clé normale, puis # + clé etrangère avec vers origine

#12)C'est une clé étrangère qui fait un lien entre la table sport et la table ville

#13) Chamonix

#14) SELECT nom FROM sport WHERE type = 'piscine';

#15) UPDATE sport SET note = 7 WHERE nom = 'Ballon perdus';

#16) INSERT INTO ville VALUES(8, 'Toulouse', 31, 471941, 118);

#16) SELECT sport.nom FROM sport JOIN ville ON ville.id = sport.id_ville WHERE sport.type = 'mur' d'escalade AND WHERE ville.nom = 'Annecy';
