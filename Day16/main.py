from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True

while should_continue:
    choice = input(f"What would you drink:({menu.get_items()}): ")

    if choice == "report":
        coffee_machine.report()
        money_machine.report()

    elif choice == "off":
        should_continue = False

    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
