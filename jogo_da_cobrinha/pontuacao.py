from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open('jogo_da_cobrinha\maior_pontuacão.txt', 'r') as f:
            self.high_score = int(f.read())
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.__atualiza_pontuacao()

    def __atualiza_pontuacao(self):
        self.clear()
        self.write(f"PONTUAÇÃO: {self.score}, HIGH SCORE: {self.high_score}", align="center", font=("Helvetica", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('maior_pontuacão.txt', 'w') as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.__atualiza_pontuacao()


    def conta_pontuacao(self):
        self.score += 1
        self.__atualiza_pontuacao()