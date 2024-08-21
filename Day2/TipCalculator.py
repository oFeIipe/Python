print("Calculadora de gorjeta")

total = float(input("Qual o valor total da conta? "))
gorjeta = int(input("Qual valor em porcetagem da gorgeta você gostaria de dar? 10, 12 ou 15? "))
pessoas = int(input("Você vai dividar a conta com quantas pessoas? "))

total_percent = total / 100
gorjeta_total = gorjeta * total_percent
valor_final = (total + gorjeta_total) / pessoas

print(f"Cada pessoa pagará: {round(valor_final, 2)}")