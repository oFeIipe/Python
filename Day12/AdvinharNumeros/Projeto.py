import logo
import random

def jogo(chances):

    numero_aleatorio = random.randint(1, 100)

    while chances > 0:
        print(f"Você tem {chances} chances restantes para advinhar o número")
        numero_escolhido = int(input("Faça uma tentativa: "))

        if numero_escolhido == numero_aleatorio:
            print(f"\nVocê acertou! a resposta era {numero_aleatorio}")
            break
        else:
            chances -= 1
            if numero_escolhido < numero_aleatorio:
                print("\nMuito baixo")
            else:
                print("\nMuito alto")
    if chances == 0:
        print(f"\nVocê gastou todas suas tentativas, você perdeu")

print(logo.logo)
print("Bem vindo ao jogo da advinhação!")
print("Estou pensando em um número entre 1 a 100")

dificuldade = input("Escolha a dificuldade: 'F' para fácil e 'D' para Difícil: ").lower()

tentativas = 10 if dificuldade == "f" else 5

jogo(tentativas)