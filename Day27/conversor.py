from tkinter import *

window = Tk()
window.title("Conversor milhas para Kms")
window.config(padx=30, pady=30)

def calculo():
    try:
        resultado = float(enput.get()) * 1.6
        label_result.config(text=f"{resultado:.2f}")
        enput.delete(0, END)
    except ValueError:
        pass

enput = Entry(width=10)
enput.grid(column=1, row=0)

label = Label(text="Milhas", font=("calibri", 10))
label.grid(column=2, row=0)

label2 = Label(text="É igual a:", font=("calibri", 10))
label2.grid(column=0, row=1)

label_result = Label(text="0", font=("calibri", 10))
label_result.grid(column=1, row=1)

label3 = Label(text="KM", font=("calibri", 10))
label3.grid(column=2, row=1)

btn = Button(text="Calcular", command=calculo)
btn.grid(column=1, row=2)

window.mainloop()

'''
def calculo():

    resultado = float(enput.get()) * 0.62
    label_result.config(text=f"{resultado:.2f}")


enput = Entry(width=10)
enput.grid(column=1, row=0)

label = Label(text="KMs", font=("calibri", 10))
label.grid(column=2, row=0)

label2 = Label(text="É igual a:", font=("calibri", 10))
label2.grid(column=0, row=1)

label_result = Label(text="0", font=("calibri", 10))
label_result.grid(column=1, row=1)

label3 = Label(text="Milhas", font=("calibri", 10))
label3.grid(column=2, row=1)

btn = Button(text="Calcular", command=calculo)
btn.grid(column=1, row=2)

window.mainloop()'''