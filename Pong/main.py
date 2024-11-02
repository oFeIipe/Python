from turtle import Turtle, Screen
from bola import Bola
from pontuacao import Pontuacao
from raquete import Raquete
import time

tela = Screen()
tela.tracer(0)
tela.bgcolor("black")
tela.setup(height=600, width=800)
tela.title("Pong")

raquete_direita = Raquete(350)
raquete_esquerda = Raquete(-350)
bola = Bola()
pontuacao = Pontuacao()

rede = Turtle("square")
rede.penup()
rede.color("white")
rede.goto(0, -300)
rede.setheading(90)
rede.pensize(5)
listras = 10

for i in range(listras):
    rede.pendown()
    rede.forward(40)
    rede.penup()
    rede.forward(30)


tela.listen()
tela.onkeypress(raquete_direita.raqueteUp, "Up")
tela.onkeypress(raquete_direita.raqueteDown, "Down")
tela.onkeypress(raquete_esquerda.raqueteUp, "w")
tela.onkeypress(raquete_esquerda.raqueteDown, "s")

jogo_rodando = True

while jogo_rodando:
    tela.update()
    time.sleep(0.05)
    bola.move()

    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.ricochete_y()


    if bola.distance(raquete_direita) < 50 and bola.xcor() > 320 or bola.distance(raquete_esquerda) < 50 and bola.xcor() < -320:
        bola.ricochete_x()

    if bola.xcor() > 400:
        bola.reinicio()
        pontuacao.l_pontua()

    if bola.xcor() < -400:
        bola.reinicio()
        pontuacao.r_pontua()



tela.exitonclick()