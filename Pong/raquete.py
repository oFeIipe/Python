from turtle import Turtle



class Raquete(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(x, 0)
        self.y_cor = 0
        self.x_cor = x

    def raqueteUp(self):
        if self.y_cor < 245:
            self.y_cor += 20
            self.goto(self.x_cor, self.y_cor)

    def raqueteDown(self):
        if self.y_cor > -245:
            self.y_cor -= 20
            self.goto(self.x_cor, self.y_cor)