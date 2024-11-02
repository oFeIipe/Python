import logo
import random

DIFICULDADE_FACIL = 10
DIFICULDADE_DIFICIL = 5

def set_dificulty(nivel):

    if dificuldade == "f":
        return DIFICULDADE_FACIL
    else:
        return DIFICULDADE_DIFICIL

def distancia(numero_escolhido, numero_aleatorio):

    if numero_escolhido < numero_aleatorio:
        print("\nMuito baixo")
    elif numero_escolhido > numero_aleatorio:
        print("\nMuito alto")


def jogo(chances):

    numero_aleatorio = random.randint(1, 100)

    while chances > 0:
        print(f"Você tem {chances} chances restantes para advinhar o número")
        numero_escolhido = int(input("Faça uma tentativa: "))

        distancia(numero_escolhido, numero_aleatorio)
        if numero_escolhido == numero_aleatorio:
            print(f"\nVocê acertou! a resposta era {numero_aleatorio}")
            break
        else:
            chances -= 1

    if chances == 0:
        print(f"\nVocê gastou todas suas tentativas, você perdeu")

print(logo.logo)
print("Bem vindo ao jogo da advinhação!")
print("Estou pensando em um número entre 1 a 100")

dificuldade = input("Escolha a dificuldade: 'F' para fácil e 'D' para Difícil: ").lower()
chances = set_dificulty(dificuldade)
jogo(chances)