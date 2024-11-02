from Animal import Animal


class Cachorro (Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade)

    def latir(self):
        print(f"{self.nome} late")