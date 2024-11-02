class User:

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.seguidores = 0
        self.seguindo = 0

    def seguir(self, user):
        user.seguidores += 1
        self.seguindo += 1

user_1 = User("Felipão", 2345)
user_2 = User("Usuário sem U", 123)

print(user_1.seguidores, user_1.seguindo)
print(user_2.seguidores, user_2.seguindo)


user_1.seguir(user_2)

print(user_1.seguidores, user_1.seguindo)
print(user_2.seguidores, user_2.seguindo)


'''class Car:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

    def modo_corrida(self):
        print("VRUUUUUUUUUUUUMMMMMMMMMMMM")
        self.portas = 2

porsche = Car("Amarelo", "Porsche")

porsche.modo_corrida(portas)'''