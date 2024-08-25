import random

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

simbols =["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Bem vindo em gerador de senhas!\n")

num_letters=int(input("Quantas letras você deseja colocar na sua senha? "))
num_simbols=int(input("Quantos simbolos você deseja colocar na sua senha? "))
num_numbers=int(input("Quantos numeros você deseja colocar na sua senha? "))

password_list = []

for char in range(0, num_letters):
    password_list.append(random.choice(letters))

for char in range(0, num_simbols):
    password_list.append(random.choice(simbols))

for char in range(0, num_numbers):
    password_list.append(random.choice(numbers))   

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
print(f"Your Password is: {password}")    
         