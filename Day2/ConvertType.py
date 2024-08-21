print(type("Hello"))
print(type(123))
print(type(123.45))
print(type(False))

print(int("123") + int("456"))

nome = input("Digite seu nome: ")

numero_de_letras = len(nome)

print(type(f"Número de letras do seu nome: {numero_de_letras}"))
print(type(numero_de_letras))


print("Número de letras no seu nome: " + str(len(input("Digite seu nome: "))))