from random import randint
from turtle import Turtle, Screen

cores = ["red", "yellow", "orange", "blue", "green", "purple"]

tela = Screen()
tela.setup(500,400)

y = -70

is_race_on = False

aposta = tela.textinput("Faça sua aposta", "Qual tartaruga vencerá a corrida? digite a cor: ")

lista_tartaruga = []

for indice in range(0, 6):
    tartagura = Turtle(shape="turtle")
    tartagura.penup()
    tartagura.color(cores[indice])
    lista_tartaruga.append(tartagura)
    tartagura.goto(-220, y)
    y += 30

    if aposta:
        is_race_on = True
cor_vencedora = ""

while is_race_on:
    for turtle in lista_tartaruga:
        if turtle.xcor() > 230:
            is_race_on = False
            cor_vencedora = turtle.pencolor()
            if cor_vencedora == aposta:
                print(f"A tartaruga vencedora foi a tartaruga de cor {cor_vencedora}, você"
                      f" acertou a aposta!")
            else:
                print(f"A tartaruga vencedora foi a tartaruga de cor {cor_vencedora}, você"
                      f" não acertou a aposta")

        numero_aleatorio = randint(0, 50)
        turtle.forward(numero_aleatorio)



tela.exitonclick()