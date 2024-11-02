from pickle import FALSE

import dados
import random
import img

DADO = dados.dados
FIM = True

def sorteia_pessoa(dados):
    pessoa_aleatoria = random.choice(dados)
    return pessoa_aleatoria

def troca(A, B):

def pontuacao(alternativa, A, B, score):

    if alternativa == "a":
        if A['numero_seguidores'] > B['numero_seguidores']:
            print("Você acertou, A é maior que B")
            score += 1
            return score
        else:
            print("Você errou")
    else:
        if A['numero_seguidores'] < B['numero_seguidores']:
            print("Você acertou, B é maior que A")
            score += 1
            return score
        else:
            print("Você errou")

def jogo():
    score = 0
    pessoa_A = sorteia_pessoa(DADO)
    pessoa_B = sorteia_pessoa(DADO)
    while FIM:

        print(img.logo)
        print(f"Compare A: {pessoa_A['nome']}, {pessoa_A['descricao']}, {pessoa_A['pais']}, {pessoa_A['numero_seguidores']}")
        print(img.versus)
        print(f"Contra B: {pessoa_B['nome']}, {pessoa_B['descricao']}, {pessoa_B['pais']}, {pessoa_B['numero_seguidores']}")
        resposta = input("\nQuem tem mais seguidores? Digite 'A' ou 'B': ").lower()

        score = (pontuacao(resposta, pessoa_A, pessoa_B, score))

        print(score)
jogo()