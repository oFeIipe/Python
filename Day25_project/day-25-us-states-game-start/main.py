from tokenize import cookie_re
from turtle import Turtle, Screen
import pandas
tela = Screen()
texto = Turtle()
texto.penup()
texto.hideturtle()

df = pandas.read_csv("50_states.csv")

tela.title("Estragos Cunidos States Game")

imagem = "blank_states_img.gif"
tela.addshape(imagem)

tartaruga = Turtle(imagem)

jogo_rodando = True
respostas_certas = []
pontuacao = 0

while jogo_rodando:

    pergunta = tela.textinput(f"Estados corretos: {pontuacao}/50", "Qual o nome do próximo estado?").title()

    try:
        if pergunta == "Sair":
            data_frame = {
                "Estados Para Aprender": []
            }
            for state in df.state:
                if state not in respostas_certas:
                    data_frame["Estados Para Aprender"].append(state)
            aprender = pandas.DataFrame(data_frame)
            aprender.to_csv("estados_para_aprender.csv")
            break
        correcao = df[df.state == pergunta]
        indice = df[df.state == pergunta].index[0]


        texto.goto(correcao.x[indice], correcao.y[indice])
        texto.write(f"{pergunta}")


        if pergunta in respostas_certas:
            continue
        pontuacao += 1
        respostas_certas.append(pergunta)

        if pontuacao > 49:
            jogo_rodando = False

    except IndexError:
        continue

