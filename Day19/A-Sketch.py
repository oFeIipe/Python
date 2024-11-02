from turtle import Turtle, Screen

ronaldin = Turtle()


def andar_frente():
    ronaldin.forward(10)

def andar_tras():
    ronaldin.backward(10)

def sentido_anti_horario():
    new_heading = ronaldin.heading() + 10
    ronaldin.setheading(new_heading)

def sentido_horario():
    new_heading = ronaldin.heading() - 10
    ronaldin.setheading(new_heading)

def limpar_tela():
    ronaldin.clear()
    ronaldin.penup()
    ronaldin.home()
    ronaldin.pendown()

tela = Screen()
tela.listen()

tela.onkeypress(andar_frente, "w")
tela.onkeypress(andar_tras, "s")
tela.onkeypress(sentido_anti_horario, "a")
tela.onkeypress(sentido_horario, "d")
tela.onkeypress(limpar_tela, "c")
tela.exitonclick()