import img

def adicao(n1, n2):
    return f"{n1 + n2:.2f}"

def subtracao(n1, n2):
    return f"{n1 - n2:.2f}"

def multiplicacao(n1, n2):
    return f"{n1 * n2:.2f}"

def divisao(n1, n2):
    return f"{n1 / n2:.2f}"

simbolos = {
            "+": adicao,
            "-": subtracao,
            "*": multiplicacao,
            "/": divisao
}
def calculadora():
    print(f"{img.logo}\n")
    num1 = float(input("Digite um número: "))
    resposta = True

    while resposta:
        operador = input("""
+
-
*
/
Digite um operador: """)
        num2 = float(input("\nDigite um número: "))

        result = float(simbolos[operador](num1, num2))
        print(f"{num1} {operador} {num2} = {result}")

        decisao = input(f"digite 'S' se você quer continuar a conta com o número {result}, caso contrário digite 'N': ").lower()

        if decisao == "n":
            resposta = False
            print(f"\n" * 40)
            calculadora()
        else:
            num1 = result
calculadora()                
