from Animal import Animal


class Peixe(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade)

    def respirar(self):
        super().respirar()
        print("De baixo da água")