import time
from turtle import Screen
from tartaruga import Tartas
from carro import Carro
from pontuacao import Score

tela = Screen()
tela.setup(600, 600)
tela.bgcolor("grey")
tela.tracer(0)
tela.title("Turtle Crossing")
tartas = Tartas()

tela.listen()
pontuacao = Score()

tela.onkeypress(tartas.andar,"w")

jogo_rodando = True

carro = Carro()

while jogo_rodando:
    tela.update()
    time.sleep(0.1)
    carro.criar_carro()
    carro.move()

    if tartas.ycor() > 290:
        pontuacao.avanca_nivel()
        tartas.posicao_inicial()
        carro.aumentar_nivel()

    for car in carro.carros:
        if tartas.distance(car) < 20:
            pontuacao.game_over()
            jogo_rodando = False

tela.exitonclick()