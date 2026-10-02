from random import *
l = 25
L = 35
grille = []

for i in range(l):
    ligne = []
    for k in range(L):
        ligne.append(0)
    grille.append(ligne)

for j in range(100):
    grille[randint(0, 24)][randint(0, 34)] = 1

for ligne in grille:
    print(ligne)