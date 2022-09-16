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


def get_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


def make_drink(drink_name):
    ingredients = MENU[drink_name]

    if ingredients['ingredients']['water'] >= resources['water']:
        return "UnSufficient Water"

    elif ingredients['ingredients']['milk'] >= resources['milk']:
        return "UnSufficient Milk"

    elif ingredients['ingredients']['coffee'] >= resources['coffee']:
        return "UnSufficient Coffee"

    return f"Here's your {drink_name}"


def main():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice in MENU:
        print("We will check")
        print(make_drink(choice))

    else:
        print("Check your spelling")


main()
