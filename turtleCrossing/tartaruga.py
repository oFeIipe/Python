from turtle import Turtle

class Tartas(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("dark green")
        self.setheading(90)
        self.posicao_inicial()

    def andar(self):
        self.forward(15)

    def posicao_inicial(self):
        self.goto(0, -280)