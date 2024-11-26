# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import *

tela = Tk()
tela.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.pack()

tela.mainloop()
# ---------------------------- UI SETUP ------------------------------- #