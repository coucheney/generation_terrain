##########################
# Auteur: Pierre Coucheney

########################
# import des librairies

import tkinter as tk
import random as rd


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

# choix des couleurs

COUL_MUR = "grey"
COUL_LIBRE = "white"


############################
# variables globales
terrain = []
grille = []




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
    global grille, terrain
    for i in range(N):
        grille.append([0]*N)
        terrain.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 1
                coul = COUL_MUR
            else:
                terrain[i][j] = 0
                coul = COUL_LIBRE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x1 = largeur * i
            y1 = hauteur * j
            x2 = largeur * (i+1)
            y2 = hauteur * (j + 1)
            carre = canvas.create_rectangle((x1, y1), (x2, y2), fill=coul)
            grille[i][j] = carre
        





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
