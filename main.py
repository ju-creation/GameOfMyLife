from customtkinter import *
from random import *

l = 25
L = 35
t = 20
grille = []
running = False

def show_grille():
    canvas_grille.delete("all")
    for i in range(l):
        for k in range(L):
            if grille[i][k] == 1:
                x = t * k
                y = t * i
                canvas_grille.create_rectangle(x, y, x+t, y+t, fill="white")

def create_grille():
    grille.clear()
    for i in range(l):
        ligne = []
        for k in range(L):
            ligne.append(0)
        grille.append(ligne)
    v_nb_cellules_aleatoire = int(slider_cases_v.get())
    for j in range(v_nb_cellules_aleatoire):
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
    if running:
        grille = next_generation()
        show_grille()
        window.after(200, game_loop)

def run():
    global running
    running = True
    create_grille()
    show_grille()
    window.after(200, game_loop)

def stop():
    global running
    grille.clear()
    running = False


def update_ui(value):
    t_slider_value.configure(text=str(int(value)))
'''for ligne in grille:
    print(ligne)'''            #affiche la grille en format textuel dans la console

set_appearance_mode('dark')
window = CTk()
window.title("Game of the life")
window.geometry("900x600")

canvas_grille = CTkCanvas(window, width=700, height=500, background="black", borderwidth=0)
canvas_grille.pack()

frame_sliders = CTkFrame(window, width=400, height=200, fg_color='transparent')
frame_sliders.pack(anchor='se', padx=20, pady=30)

bt_run = CTkButton(window, text='Run', text_color='white', fg_color='#22C55E', hover_color='#4ADE80',
                   command=run)
bt_run.pack(anchor='sw', pady=20, padx=20)

bt_stop = CTkButton(window, text='Stop', text_color='white', fg_color='#EF4444', hover_color="#F87171",
                    command=stop)
bt_stop.pack(anchor='sw', padx=20)

t_slider_cases_v = CTkLabel(frame_sliders, text_color='white', text='Nb cases en vies (0-875):')
t_slider_cases_v.pack()

slider_cases_v = CTkSlider(frame_sliders, from_=0, to=875, command=update_ui)
slider_cases_v.pack()
slider_cases_v.set(100)

t_slider_value = CTkLabel(frame_sliders, text='100', text_color='white')
t_slider_value.pack()

window.mainloop()
#corriger le .after qui se superpose quand on appuie plusieurs fois sur run
#add bt stop et vitesse