from tkinter import *

window = Tk()

window.title("Telinha poggers")
window.minsize(500, 300)
window.config(padx=20, pady=20)

label = Label(text="Label", font=("calibri", 20, "bold"))
label.grid(column=0, row=0)

butones = Button(text="Butão")
butones.grid(column=1, row=1)

butones2 = Button(text="Butão2")
butones2.grid(column=2, row=0)

enput = Entry(width=10)
enput.grid(column=3, row=2)

window.mainloop()