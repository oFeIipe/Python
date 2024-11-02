import random

numero_random = random.randint(1, 3)

escolha = int(input("Tente advinhar o número aleatório: "))

if escolha == numero_random:
    print(f"Acertou! o número era {numero_random}")