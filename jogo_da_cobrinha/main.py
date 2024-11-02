from turtle import Turtle, Screen
from cobra import Cobra
from comida import Comida
from pontuacao import Pontuacao
import time

tela = Screen()
tela. setup(600, 600)
tela.bgcolor("black")
tela.title("Jogo da Cobrinha")
tela.tracer(0)

cobra = Cobra()
comida = Comida()

tela.listen()
tela.onkey(cobra.up, "Up")
tela.onkey(cobra.down, "Down")
tela.onkey(cobra.left, "Left")
tela.onkey(cobra.right, "Right")

score = Pontuacao()

jogo_rodando = True

while jogo_rodando:
    tela.update()
    time.sleep(0.1)

    cobra.move()

    if cobra.cabeca.distance(comida) < 15:
        comida.refresh()
        cobra.adicionar_parte()
        score.conta_pontuacao()


    if cobra.cabeca.xcor() > 290 or cobra.cabeca.xcor() < -290 or cobra.cabeca.ycor() > 290 or cobra.cabeca.ycor() < -290:
        score.reset()
        cobra.reset()

    for seg in cobra.segmentos[1:]:
        if cobra.cabeca.distance(seg) < 10:
            score.reset()
            cobra.reset()

tela.exitonclick()
