class Animal:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def respirar(self):
        print("Inspirando e expirando")