from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-90, 180)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(90, 180)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def r_pontua(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_pontua(self):
        self.l_score += 1
        self.update_scoreboard()