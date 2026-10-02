from customtkinter import *

set_appearance_mode('dark')
window = CTk()
window.title("Game of the life")
window.geometry("700x500")

canvas_grille = CTkCanvas(window, width=700, height=500)
canvas_grille.pack()

window.mainloop()