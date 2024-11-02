from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.__desenha_nivel()

    def __desenha_nivel(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"LEVEL: {self.score}", align="center", font=("Arial", 20, "normal"))

    def avanca_nivel(self):
        self.score += 1
        self.__desenha_nivel()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME-OVER", align="center", font=("Courier", 20, "normal"))