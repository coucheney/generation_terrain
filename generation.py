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
N = 10

# paramètres de l'automate:
# probabilité d'être un mur à l'initialisation:
P = 0.5
# nombre d'itérations de l'automate
N_ITER = 1
# valeur seuil à parti de laquelle une case devient un mur
SEUIL = 4
# distance du voisinage considéré
D = 1

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
    grille = []
    terrain = []
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
        
def affiche_terrain():
    """ Affiche le terrain sur le canvas"""
    for i in range(N):
        for j in range(N):
            if terrain[i][j] == 0:
                coul = COUL_LIBRE
            else:
                coul = COUL_MUR
            canvas.itemconfigure(grille[i][j], fill=coul)


def sauvegarde():
    """Ecrit la taille de la grille et les valeurs de la variable
     terrain das le fichier sauvegarde.txt
     """
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(terrain[i][j]) + "\n")
    fic.close()


def load():
    """
    Lire le fichier sauvegarde.txt et affiche dans le canvas le terrain lu
    """
    global N
    fic = open("sauvegarde.txt", "r")
    taille = fic.readline()
    N = int(taille)
    canvas.delete()
    # initialisation pour avoir des listes à la bonne taille
    init_terrain()
    print(terrain)
    i = j = 0
    for ligne in fic:
        terrain[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    print(terrain)
    affiche_terrain()
    fic.close()


def cpt_murs(i, j, d):
    """Retourne le nombre de murs voisins de la case
     de coordonnées (i,j) à distance au plus d"""
    cpt = 0
    delta_i = 0
    if i + d + 1 >= N:
        delta_i = N
    for k in range(i - d - delta_i, i + d + 1 - delta_i):
        delta_j = 0
        if j + d + 1 >= N:
            delta_j = N
        for l in range(j - d - delta_j, j + d + 1 - delta_j):
            # si il y a un mur à la case de coordonnées (k, l)
            if terrain[k][l] == 1:
                cpt += 1
    if terrain[i][j] == 1:
        cpt -= 1
    return cpt

def etape():
    """Fait une étape de l'automate"""
    global terrain
    terrain_res = []
    for i in range(N):
        terrain_res.append([0]*N)
    for i in range(N):
        for j in range(N):
            nb_murs = cpt_murs(i, j, D)
            if nb_murs > SEUIL:
                terrain_res[i][j] = 1
    terrain = terrain_res
    affiche_terrain()




def genere():
    """Fonction qui génère le terrain en suivant les régles de l'automate"""
    for i in range(N_ITER):
        etape()    


def compte_mur(event):
    """fonction qui donne le nombre de murs voisins de la case cliquée"""
    x = event.x
    y = event.y
    largeur = LARGEUR // N
    hauteur = HAUTEUR // N
    i = x // largeur
    j = y // hauteur
    murs = cpt_murs(i, j, D)
    print(i, j, murs)

#########################
# partie principale

# création des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
bouton_sauvegarde = tk.Button(racine, text="Sauvegarde", command=sauvegarde)
bouton_load = tk.Button(racine, text="Charger terrain", command=load)
bouton_genere = tk.Button(racine, text="genere terrain", command=genere)

# placement des widgets
canvas.grid(column=1, row=0, rowspan=10)
bouton_sauvegarde.grid(row=0)
bouton_load.grid(row=1)
bouton_genere.grid(row=2)

init_terrain()

# pour tester la fonction qui compte le nombre de murs
canvas.bind("<Button-1>", compte_mur)


# boucle principale
racine.mainloop()
