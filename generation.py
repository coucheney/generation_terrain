##########################
# Auteur: Pierre Coucheney

########################
# import des librairies

import tkinter as tk


########################
# constantes

# hauteur du canvevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N = 3

# paramètres de l'automate:
# probabilité d'être un mur à l'initialisation:
P = 0.5


####################
# fonctions

def init_terrain():
    """Initialiser le terrain:
    * initialiser la liste carrée terrain à 2D de taille N telle
    que la case de coordonnées (i,j) vaut 1 si il y a un mur
    dessus et 0 sinon
    * initialiser la liste carrée grille à 2D de taille N
    telle que la case de coordonnées (i,j) contient l'identifiant
    du carré dessiné sur le canevas 
    * Une case est un mur avec probabilité P
    """
    grille = []
    for i in range(N):
        grille.append([0]*N)
    print(grille)




#########################
# partie principale

# création des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)

# placement des widgets
canvas.grid(column=1, row=0)


init_terrain()

# boucle principale
racine.mainloop()
