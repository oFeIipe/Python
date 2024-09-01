import img

def adicao(n1, n2):
    return f"{n1 + n2:.2f}"

def subtracao(n1, n2):
    return f"{n1 - n2:.2f}"

def multiplicacao(n1, n2):
    return f"{n1 * n2:.2f}"

def divisao(n1, n2):
    return f"{n1 / n2:.2f}"



while True:

    print(f"{img.logo}\n")
    num1 = float(input("Digite um número: "))

    resposta = True


    while resposta:
        escolha = input("""
+
-
*
/
Escolha um operador: """)
        num2 = float(input("\nDigite um número: "))

        if escolha == "+":
            adicao(num1, num2)
            result = num1 + num2
            print(f"{num1:.2f} + {num2:.2f} = {result:.2f}")

        elif escolha == "-":
            subtracao(num1,num2) 
            result = num1 - num2 
            print(f"{num1:.2f} - {num2:.2f} = {result:.2f}")

        elif escolha == "*":
            multiplicacao(num1,num2)  
            result = num1 * num2
            print(f"{num1:.2f} * {num2:.2f} = {result:.2f}")

        elif escolha == "/":
            divisao(num1,num2)
            result = num1 / num2
            print(f"{num1:.2f} / {num2:.2f} = {result:.2f}")

        pergunta = input(f"\nDeseja continuar a calcular com {result:.2f}? digite 'S' ou 'N': ").lower()
        
        if pergunta == "s":
            num1 = result
        else:
            resposta = False
            print(f"\n" * 50)


             