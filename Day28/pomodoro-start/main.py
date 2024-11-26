from math import floor
from re import match
from tkinter import *



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
contador = None


def reset():
    timer.config(text="Timer")
    canvas.itemconfig(text_timer, text="00:00")
    window.after_cancel(contador)
    check_mark.config(text="")
    global reps
    reps = 0

def start_time():
    global reps

    reps += 1
    segundos = WORK_MIN * 60
    descando_curto = SHORT_BREAK_MIN * 60
    descanso_longo = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(segundos)
        timer.config(text="Timer", fg=PINK)
    elif reps % 8 == 0:
        count_down(descanso_longo)
        timer.config(text="Descanso", fg=PINK)
    else:
        count_down(descando_curto)
        timer.config(text="Pausa", fg=YELLOW)

def count_down(count):
    minutos = floor(count / 60)
    segundos_restates = count % 60

    if segundos_restates < 10:
        segundos_restates = f"0{segundos_restates}"
    canvas.itemconfig(text_timer, text=f"{minutos}:{segundos_restates}")

    if count >= 0:
        global contador
        contador = window.after(1000, count_down, count - 1)
    else:
        start_time()
        if reps % 2 == 0:
            sessoes = floor(reps / 2)
            check_mark.config(text=check * sessoes)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)
check = "🗸"

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
imagem = PhotoImage(file="img/tomato.png")
canvas.create_image(100, 112, image=imagem)

text_timer = canvas.create_text(100, 130, text="00:00", font=("arial", 26, "bold"))
canvas.grid(column=2, row=2)

timer = Label(text="Timer", font=("Courier", 30, "bold"), bg=GREEN, fg=PINK)
timer.grid(column=2, row=1)

start_btn = Button(text="Começar", command=start_time)
start_btn.grid(column=1, row=3)

reset_btn = Button(text="Resetar", command=reset)
reset_btn.grid(column=3, row=3)

check_mark = Label(bg=GREEN, font=("arial", 25))
check_mark.grid(column=2, row=4)

window.mainloop()