def life_in_weeks(idade):
    idade_90 = 90 - idade
    restante = idade_90 * 52
    print(f"Você tem {restante:.0f} semanas de vida restante")
    
idade = int(input("Qual a sua idade? "))    

life_in_weeks(idade)