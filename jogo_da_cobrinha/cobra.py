from turtle import Turtle
posicoes_iniciais = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Cobra:
    def __init__(self):
        self.segmentos = []
        self.__criar_cobra()
        self.cabeca = self.segmentos[0]

    def __criar_cobra(self):
        for position in posicoes_iniciais:
            self.add_segment(position)

    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000,1000)
        self.segmentos.clear()
        self.__criar_cobra()
        self.cabeca = self.segmentos[0]


    def add_segment(self, position):
        cobra = Turtle("square")
        cobra.color("white")
        cobra.penup()
        cobra.goto(position)
        self.segmentos.append(cobra)

    def adicionar_parte(self):
        self.add_segment(self.segmentos[-1].position())


    def move(self):
        for new_seg in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[new_seg - 1].xcor()
            novo_y = self.segmentos[new_seg - 1].ycor()
            self.segmentos[new_seg].goto(novo_x, novo_y)
        self.cabeca.forward(20)

    def up(self):
        if self.cabeca.heading() != DOWN:
            self.cabeca.setheading(UP)

    def down(self):
        if self.cabeca.heading() != UP:
            self.cabeca.setheading(DOWN)

    def right(self):
        if self.cabeca.heading() != LEFT:
            self.cabeca.setheading(RIGHT)

    def left(self):
        if self.cabeca.heading() != RIGHT:
            self.cabeca.setheading(LEFT)


