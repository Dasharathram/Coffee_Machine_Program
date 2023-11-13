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

is_on = True
profit = 0
print("Hi, Hope you are doing good today.")


def is_resources_enough(order_ingredients):
    """returns true if order ingredients are lower than resources and false if not"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """processes the amount and returns total"""
    print("Please insert only coins")
    total = int(input("How many of Quarters? ")) * 0.25
    total += int(input("How many of dimes? ")) * 0.1
    total += int(input("How many of nickels? ")) * 0.05
    total += int(input("How many of cents? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """returns true if the amount inserted is enough for drink, false if not. prints change too"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, I can't make your coffee not enough money. Take them back.")
        return False


def make_coffee(drink_name, order_ingredients):
    """makes coffee and deducts resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, ☕️ Enjoy")


while is_on:
    order = input("What is your order? (espresso/latte/cappuccino): ")
    if order == "off":
        print("Switching off...")
        is_on = False
    elif order == "report":
        print("Here is you report:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        print(order)
        print(drink)
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
