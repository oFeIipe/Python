print("Bem vindo a pizzaria Pythonica")

tamanho = input("Qual o tamanho da sua pizza? P, M ou G: ").upper()
pepperoni = input("Quer adicionar pepperoni na sua pizza? S ou N: ").upper()
queijo = input("Quer adicionar queijo extra na sua pizza? S ou N: ").upper()

preco = 0

if tamanho == "P":
    preco += 15
elif tamanho == "M":
    preco += 20
elif tamanho == "G":
    preco += 25
else:
    print("Você digitou algo errado")

if pepperoni == "S":
    if tamanho == "P":
        preco += 2
    else:
        preco += 3
    
if queijo == "S":
    preco += 1
    
print(f"O valor final é: R${preco}")    
    
    
    