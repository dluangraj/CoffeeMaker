from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

closed = False

while not closed:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}: ")
    if choice == "off":
        closed = True
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)