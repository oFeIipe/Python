MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "agua": 1000,
    "leite": 600,
    "cafe": 200,
}
ganhos = 0

def troco():
    print("Por favor insira as moedas.")
    moedas = int(input("Quantas moedas de 25 centavos? ")) * 0.25
    moedas += int(input("Quantas moedas de 10 centavos? ")) * 0.10
    moedas += int(input("Quantas moedas de 5 centavos? ")) * 0.05
    moedas += int(input("Quantas moedas de 1 centavo? ")) * 0.01

    return moedas

def order(pedido, recursos, ganhos):

    ingredientes = MENU[pedido]['ingredients']

    if recursos['agua'] - ingredientes['water'] < 0:
        print("Água insuficiente")
        return

    elif recursos['leite'] - ingredientes['milk'] < 0:
        print("Leite insuficiente")
        return

    elif recursos['cafe'] - ingredientes['coffee'] < 0:
        print("Café insuficiente")
        return

    total = troco()
    precoDrink = MENU[pedido]['cost']
    troco_restante = total - precoDrink

    if total < precoDrink:
        print("Desculpe o valor inserido é insuficiente, valor retornado\n")

    else:
        print(f"Aqui está seus ${troco_restante:.2f} de troco")
        print(f"Aqui está seu {pedido}☕. Aproveite! \n")

        ganhos += precoDrink
        recursos['agua'] -= ingredientes['water']
        recursos['cafe'] -= ingredientes['coffee']
        recursos['leite'] -= ingredientes['milk']

        return ganhos

while True:

    pedido = input("Qual seu pedido? (expresso/latte/cappuccino): ")
    if pedido == "off":
        break
    elif pedido == "report":
        print(f"\nÁgua: {resources['agua']}ml")
        print(f"Leite: {resources['leite']}ml")
        print(f"Café: {resources['cafe']}g")
        print(f"Dinheiro: ${ganhos}\n")
    else:
        ganhos = order(pedido, resources, ganhos)