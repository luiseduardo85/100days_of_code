from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

turn_off = False

while not turn_off:
    type = menu.get_items()
    type_of_coffee = input(f"What would you like? ({type}): ").lower()
    if type_of_coffee == 'off':
        turn_off = True
    elif type_of_coffee == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(type_of_coffee)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)