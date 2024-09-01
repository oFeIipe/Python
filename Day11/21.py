import logo 
import random


def blackjack():
    print(logo.logo)
    suas_cartas = []
    pontuacao = 0

    for i in range(2):
        suas_cartas.append(random.choice(cartas))
        pontuacao += suas_cartas[cartas]

    print(f"Suas cartas {suas_cartas}, pontuação atual: {pontuacao}")
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

escolha = input("Você quer jogar uma partida de BlackJack(21)? Digite 'S' ou 'N': ").lower()

if escolha == "s":
    blackjack()