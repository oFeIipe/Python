from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink = Menu()
maquina = CoffeeMaker()
money = MoneyMachine()

while True:
    order = input(f"Qual seu pedido? ({drink.get_items()}):")
    if order == "report":
        report = maquina.report(), money.report()
    elif order == "off":
        break
    else:
        drinque = drink.find_drink(order)
        if maquina.is_resource_sufficient(drinque) and money.make_payment(drinque.cost):
                maquina.make_coffee(drinque)