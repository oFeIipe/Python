print("Montanha Russa")
altura = int(input("Digite sua altrua em cm: "))

if altura >= 120:
    print("Você pode andar na montanha russa!")
    taxa = 0
    idade = int(input("Qual sua idade? "))

    if idade <= 18 and idade > 11:
        print("Você deverá pagar R$20 reais")
        taxa = 20
    elif idade < 12:
        print("Voce deverá pagar R$12")
        taxa = 12
    elif idade >= 45 and idade <= 55: # 45 <= idade <= 55
        print("O ingresso é por conta da casa!") 
    else:
        print("Você devera pagar R$30 reais")
        taxa = 30
    quer_foto = input("Você que uma foto do passeio? digite s para Sim e n para Não: ").lower()

    if quer_foto == "s":
        taxa += 5
    print(f"O valor total ficou: R${taxa}")
       
else:
    print("Você não pode entrar na montanha russa")
