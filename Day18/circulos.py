import turtle
from turtle import Turtle, Screen
import random

def criar_cores():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor_aleatoria = (r,g,b)
    return cor_aleatoria


turtle.colormode(255)

rogerin = Turtle()

rogerin.speed(0)
def faz_circulos(qtd):
    for i in range(int(360 / qtd)):
        rogerin.circle(80)
        rogerin.setheading(rogerin.heading() + qtd)
        rogerin.color(criar_cores())
faz_circulos(5)


tela = Screen()
tela.exitonclick()