from turtle import Turtle
from random import randint

class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.6,0.6)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)