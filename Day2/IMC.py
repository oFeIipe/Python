print("CALCULADORA IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {round(imc,2)}")#print(f"Seu IMC é: {imc:.2f}") pode ser usado, e terá a mesma funcionalidade