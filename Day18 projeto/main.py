'''import colorgram as c

cores = []
colors = c.extract('.venv\imgCores.jpg', 40)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r > 225 and g  > 225 and b > 225:
        continue
    cor_nova = (r, g, b)
    cores.append(cor_nova)
print(cores)'''
import turtle
from random import choice
from turtle import Turtle, Screen, mode

turtle.colormode(255)
matutuo = [(46, 92, 144), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (211, 56, 76), (155, 23, 19), (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), (163, 209, 182), (227, 171, 180), (17, 75, 108), (116, 123, 146), (184, 188, 208), (73, 79, 43), (162, 199, 214)]
ronaldin = Turtle()

ronaldin.up()
ronaldin.speed(0)
tela = Screen()
ronaldin.hideturtle()
y = -230

def desenhar_circulos(y):
    ronaldin.setpos(-230, y)
    for i in range(10):
        ronaldin.dot(25, choice(matutuo))
        ronaldin.forward(50)

for j in range(10):
    desenhar_circulos(y)
    y += 50

tela.exitonclick()

