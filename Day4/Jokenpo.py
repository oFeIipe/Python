import random


pedra ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel =''' 
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
'''
tesoura ='''
    _______
---'   ____)____
          ______)_
        __________)
      (____)
---.__(___)
'''

jokenpo =[pedra, papel, tesoura]

escolha_player = int(input("Pedra, Papel ou Tesoura? digite 0 para pedra, 1 para Papel e 2 para Tesoura: "))
print(f"Você escolheu: {jokenpo[escolha_player]}")
escolha_maquina = random.randint(0, 2)
print(f"O computador escolheu:")
print(jokenpo[escolha_maquina])

if escolha_player >= 3 or escolha_player < 0:
    print("Inválido")    
elif escolha_player == 0 and escolha_maquina == 2:
    print("Você Venceu")
elif escolha_player == 2 and escolha_maquina == 0:
    print("Você Perdeu")    
elif escolha_maquina > escolha_player:
    print("Você Perdeu")
elif escolha_maquina == escolha_player:
    print("Empate") 
elif escolha_player > escolha_maquina:
    print("Você venceu")       


            