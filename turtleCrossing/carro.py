from turtle import Turtle
from random import choice, randint
cores = ["red", "yellow", 'green', 'blue', 'orange', 'purple', 'pink', 'white']

class Carro:
    def __init__(self):
        super().__init__()
        self.carros = []
        self.velocidade = 10
        self.criar_carro()

    def criar_carro(self):
        chance = randint(1,6)
        if chance == 1:
            carrinho = Turtle("square")
            carrinho.shapesize(1, 2)
            carrinho.penup()
            carrinho.color(choice(cores))
            carrinho.goto(310, randint(-250, 250))
            self.carros.append(carrinho)

    def move(self):
        for car in self.carros:
            car.backward(self.velocidade)

    def aumentar_nivel(self):
        self.velocidade *= 1.10