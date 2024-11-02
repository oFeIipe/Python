import random
import img
import dados

def sorteio_pessoa():
    pessoa_aleatoria = random.choice(dados.dados)
    return pessoa_aleatoria

def conta_pontuacao(chute, A, B, score, certo):
    if chute == "a":
        if A["numero_seguidores"] > B["numero_seguidores"]:
            score += 1
            return score, certo
        else:
            certo = False
            return score, certo

    elif chute == "b":
        if A["numero_seguidores"] < B["numero_seguidores"]:
            score += 1
            return score, certo
        else:
            certo = False
            return score, certo

def jogo():
    pessoa_a = sorteio_pessoa()
    pessoa_b = sorteio_pessoa()
    pontuacao = 0

    saida = True

    while saida:
        print(img.logo)

        if pontuacao > 0:
            print(f"Você acertou! sua pontuação: {pontuacao}")

        print(f"{pessoa_a['nome']}, {pessoa_a['descricao']}, {pessoa_a['pais']}")
        print(img.versus)
        print(f"{pessoa_b['nome']}, {pessoa_b['descricao']}, {pessoa_b['pais']}")
        resposta = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()


        pontuacao, saida = conta_pontuacao(resposta, pessoa_a, pessoa_b, pontuacao, saida)

        pessoa_a = pessoa_b
        pessoa_b = sorteio_pessoa()

        if pessoa_a == pessoa_b:
            pessoa_b = sorteio_pessoa()
        print("\n" *5)

        if not saida:
            print(f"Você errou, sua pontuação final foi: {pontuacao}")
            break
jogo()