from turtle import Turtle, Screen

ronaldin = Turtle()
ronaldin.width(5)
ronaldin.shape('arrow')

def andar_frente():
    ronaldin.forward(10)

def andar_tras():
    ronaldin.backward(10)

def sentido_anti_horario():
    ronaldin.left(10)

def sentido_horario():
    ronaldin.right(10)

def limpar_tela():
    tela.resetscreen()

tela = Screen()
tela.listen()

tela.onkeypress(andar_frente, "w")
tela.onkeypress(andar_tras, "s")
tela.onkeypress(sentido_anti_horario, "a")
tela.onkeypress(sentido_horario, "d")
tela.onkeypress(limpar_tela, "c")
tela.exitonclick()