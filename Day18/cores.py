import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)

def criar_cores():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor_aleatoria = (r,g,b)
    return cor_aleatoria

ronaldin = Turtle()

lados = [0, 90, 180, 270]
ronaldin.pensize(10)
ronaldin.speed(0)

for i in range(300):
    ronaldin.forward(30)
    ronaldin.setheading(random.choice(lados))
    ronaldin.pencolor(criar_cores())
tela = Screen()
tela.exitonclick()