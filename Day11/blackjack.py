import logo
import random

def dar_carta():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta


def conta_pontuacao(carta):

    pontuacao = sum(carta)

    if 11 in carta and pontuacao > 21:
        carta.remove(11)
        carta.append(1)

    if len(carta) == 2 and pontuacao == 21:
        return 0

    return pontuacao

def apuracao(pontuacao_player, pontuacao_pc):

    if pontuacao_pc == pontuacao_pc and pontuacao_player == pontuacao_pc:
        print("Empate")

    elif pontuacao_pc == 0:
        print("Você perdeu! computador tem o BlackJack")
    elif pontuacao_player == 0:
        print("Você venceu! você tem o BlackJack")

    elif pontuacao_player > 21:
        print("Você perdeu! sua pontuação passou de 21")
    elif pontuacao_pc > 21:
        print("Você venceu! a pontuação do computador passou de 21")

    else:
        if pontuacao_pc > pontuacao_player:
            print("Vitória do computador!")
        else:
            print("Você venceu!")

def blackjack():
    cartas_player = []
    cartas_pc = []
    pontuacao_player = -1
    pontuacao_pc = -1
    jogo = True
    print(logo.logo)
    dar_carta()

    for card in range(2):
        cartas_player.append(dar_carta())
        cartas_pc.append(dar_carta())

    while jogo:
        pontuacao_player = conta_pontuacao(cartas_player)
        pontuacao_pc = conta_pontuacao(cartas_pc)
        print(f"Suas cartas {cartas_player}, sua pontuação: {pontuacao_player}")
        print(f"Cartas do computador {cartas_pc[0]}\n")

        if pontuacao_pc == 0 or pontuacao_player == 0 or pontuacao_player >= 21:
            jogo = False

        else:
            decisao = input("Você deseja outra carta? Digite 'S' ou 'N': ").lower()
            if decisao == "s":
                cartas_player.append(dar_carta())
            else:
                jogo = False

    while pontuacao_pc != 0 and pontuacao_pc <= 17:
        cartas_pc.append(dar_carta())
        pontuacao_pc = conta_pontuacao(cartas_pc)

    print(f"Sua mão final {cartas_player}, pontuação final {pontuacao_player}")
    print(f"Mão final do computador {cartas_pc}, pontuação final {pontuacao_pc}")
    apuracao(pontuacao_player, pontuacao_pc)

while input ("\nVocê quer jogar uma partida de BlackJack(21)? Digite 'S' para sim e 'N' para não: ").lower() == "s":

    print("\n" * 20)
    blackjack()










