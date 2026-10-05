from customtkinter import *
from random import *

l = 25
L = 35
t = 20
grille = []

def show_grille():
    canvas_grille.delete("all")
    for i in range(l):
        for k in range(L):
            if grille[i][k] == 1:
                x = t * k
                y = t * i
                canvas_grille.create_rectangle(x, y, x+t, y+t, fill="white")

def create_grille():
    for i in range(l):
        ligne = []
        for k in range(L):
            ligne.append(0)
        grille.append(ligne)

    for j in range(100):
        grille[randint(0, l-1)][randint(0, L-1)] = 1

voisins = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def count_voisins(i, k):
    nb_voisins_vie = 0
    for di, dk in voisins:
        n_l = i + di
        n_L = k + dk
        if 0 <= n_l < l and 0 <= n_L < L:
            if grille[n_l][n_L] == 1:
                nb_voisins_vie+=1
    return nb_voisins_vie

def next_generation():
    n_grille = []
    for i in range(l):
        ligne = []
        for k in range(L):
            nb = count_voisins(i, k)
            if grille[i][k] == 1:
                if nb != 2 and nb != 3:
                    ligne.append(0)
                else:
                    ligne.append(1)
            if grille[i][k] == 0:
                if nb == 3:
                    ligne.append(1)
                else:
                    ligne.append(0)
        n_grille.append(ligne)
    return n_grille

def game_loop():
    global grille
    grille = next_generation()
    show_grille()
    window.after(200, game_loop)
'''for ligne in grille:
    print(ligne)'''            #affiche la grille en format textuel dans la console

set_appearance_mode('dark')
window = CTk()
window.title("Game of the life")
window.geometry("700x500")

canvas_grille = CTkCanvas(window, width=700, height=500, background="black", borderwidth=0)
canvas_grille.pack()

create_grille()
show_grille()
game_loop()
window.mainloop()