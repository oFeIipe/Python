from tkinter import *
from tkinter import messagebox
import json
from random import randint, choice, shuffle
from simbolos import *
import pyperclip

def search_website():
    site_data = site_input.get().lower()

    if site_data:

            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    email = data[site_data]['email']
                    senha = data[site_data]['senha']
            except FileNotFoundError:
                messagebox.showerror(title="Erro", message="Arquivo não encontrado")
            except KeyError:
                messagebox.showerror(title=site_data, message="Esse site não foi cadastrado")
            else:
                messagebox.showinfo(title=site_data, message=f"Email: {email}\nSenha: {senha}")

def gerador_senhas():
    password_input.delete(0, END)

    letras_random = [choice(alfabeto) for l in range(randint(6, 8))]
    numeros_random = [choice(numbers) for n in range(randint(2, 4))]
    simbolos_random = [choice(simbolos) for s in range(randint(2, 4))]

    lista_senha = letras_random + numeros_random + simbolos_random
    shuffle(lista_senha)
    senha_aleatoria = "".join(lista_senha)
    password_input.insert(0, senha_aleatoria)
    pyperclip.copy(senha_aleatoria)


def save_informations():
    site_data = site_input.get().lower()
    username_data = username_input.get()
    password_data = password_input.get()

    new_data = {
        site_data: {
            "email": username_data,
            "senha": password_data,
        }
    }

    if not site_data or not username_data or not password_data:
        messagebox.showerror(title="Inválido", message="Campo(s) vazio(s)")
        return

    is_ok = messagebox.askokcancel(title=site_data, message="Esse são os dados escritos: \n"
                                                    f"Email: {username_data}\n"
                                                    f"Senha: {password_data}")
    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                d = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(title="Aviso", message="Dados salvos com sucesso!")
        else:
            with open("data.json", "w") as data_file:
                d.update(new_data)
                json.dump(d, data_file, indent=4)
                messagebox.showinfo(title="Aviso", message="Dados salvos com sucesso!")
        finally:

            site_input.delete(0, END)
            password_input.delete(0, END)


tela = Tk()
tela.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(column=1, row=0)

#Label
site_label = Label(text="Site:")
site_label.grid(column=0, row=1)
username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)
password_label = Label(text="Senha:")
password_label.grid(column=0, row=3)

#Input
site_input = Entry(width=36)
site_input.grid(column= 1, row=1)
site_input.focus()
username_input = Entry(width=50)
username_input.grid(column= 1, row=2, columnspan=2)
username_input.insert(0, "costadecarvalho.felipe@gmail.com")
password_input = Entry(width=36)
password_input.grid(column= 1, row=3)

#BTN
gen_pas_btn = Button(text="Gerar Senha", command=gerador_senhas)
gen_pas_btn.grid(column=2, row=3, sticky=EW)
add_btn = Button(text="Adicionar", width=42, command=save_informations)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn = Button(text="Procurar", command=search_website)
search_btn.grid(column=2, row=1, sticky=EW)
tela.mainloop()