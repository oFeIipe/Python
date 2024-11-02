from turtle import Turtle

class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.direcao_y = 8
        self.direcao_x = 8

    def move(self):
        novo_x = self.xcor() + self.direcao_x
        novo_y = self.ycor() + self.direcao_y
        self.goto(novo_x, novo_y)

    def ricochete_y(self):
        self.direcao_y *= -1

    def ricochete_x(self):
        self.direcao_x *= -1
        self.direcao_x *= 1.05

    def reinicio(self):
        self.direcao_x = 10
        self.goto(0,0)
        self.ricochete_x()