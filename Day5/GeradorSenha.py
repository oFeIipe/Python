import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

simbolos =["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Bem vindo em gerador de senhas!\n")

num_letras=int(input("Quantas letras você deseja colocar na sua senha? "))
num_simbolos=int(input("Quantos simbolos você deseja colocar na sua senha? "))
num_numeros=int(input("Quantos numeros você deseja colocar na sua senha? "))


letras_qtd = ""
numeros_qtd = ""
simbolos_qtd = ""

for num_letras in range(num_letras): #para cada número digitado em num_letras
    letra_random = random.choice(alfabeto) #cria a variavel letra_random e utiliza ramdom.choice pra aleatorizar as letras da lista alfabeto
    letras_qtd += letra_random #adiciona a letra aletoria tirada da lista para a variavel letras_qtd


for num_numeros in range(num_numeros): #para cada número digitado em num_numeros
    numero_random = random.choice(numeros)  #cria a variavel numero_random e utiliza ramdom.choice pra aleatorizar os números da lista numeros     
    numeros_qtd += numero_random  #adiciona o número aletorio tirado da lista para a variavel numeros_qtd

for num_simbolos in range(num_simbolos): #para cada número digitado em num_simbolos
    simbolos_random = random.choice(simbolos) #cria a variavel simbolos_random e utiliza ramdom.choice pra aleatorizar os simbolos da lista simbolos 
    simbolos_qtd += simbolos_random  #adiciona o simbolo aletorio tirado da lista para a variavel simbolos_qtd

senha_forte = simbolos_qtd + numeros_qtd + letras_qtd #une todos os caracteres aleatórios gerados

senha_convert_list = list(senha_forte) #converte senha_forte para um tipo lista
random.shuffle(senha_convert_list) #aleatoiza os caracteres da lista senha_convert_list

senha_final_convertida = ''.join(senha_convert_list) #remove as aspas, colchetes e espaços vazios dos caracteres da lista

print(f"\nSua Senha é: {senha_final_convertida}")

   
