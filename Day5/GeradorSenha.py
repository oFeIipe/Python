import random

alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

simbolos =["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Bem vindo em gerador de senhas!\n")

num_letras=int(input("Quantas letras você deseja colocar na sua senha? \n"))
num_numeros=int(input("Quantos numeros você deseja colocar na sua senha? \n"))
num_simbolos=int(input("Quantos simbolos você deseja colocar na sua senha? \n"))


letras_qtd = 0

for letter in alfabeto:
    letras_qtd += 

'''for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: #confere se algum número e divisivel por 3 e 5
        print("FizzBuzz")
    elif number % 3 == 0: #confere se o número é divisivel por 3
        print("Fizz")
    elif number % 5 == 0: #confere se o número é divisivel por 5 
        print("Buzz")
    else:
        print(number) #printa os números restantes '''