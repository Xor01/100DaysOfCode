MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cash = 0.00


def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${cash}")


def check_ingredient(drink_name):
    for item in MENU[drink_name]['ingredients']:
        if MENU[drink_name]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_drink(drink_name):
    for item in MENU[drink_name]['ingredients']:
        resources[item] -= MENU[drink_name]['ingredients'][item]


def check_money(drink_name):
    drink_price = MENU[drink_name]['cost']

    total_money = take_money(drink_name)

    if total_money - drink_price < 0:
        print(f"Insufficient money, take it back")
        return False

    print(f"This Drink cost you ${drink_price} you get in return ${'{:.2f}'.format(total_money - drink_price)}")
    return True


def take_money(drink_name):

    quarters = int(input("Enter Quarters: ")) * 0.25
    dimes = int(input("Enter Dimes: ")) * 0.1
    nickles = int(input("Enter Nickles: ")) * 0.05
    penny = int(input("Enter Penny: ")) * 0.01
    total_money = quarters + dimes + nickles + penny

    return total_money


def main():

    while True:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice in MENU:

            if check_ingredient(choice):
                if check_money(choice):
                    make_drink(choice)
                    global cash
                    cash += MENU[choice]['cost']

        elif choice == "report":
            get_report()

        elif choice == "off":
            return

        else:
            print("Check your spelling")


main()
