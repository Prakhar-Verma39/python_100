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


# def venting_machine(water, coffee, milk, money):
#     ask = input("What would you like? (espresso/latte/cappuccino):").lower()
#     if ask == "off":
#         return
#     elif ask == "report":
#         print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
#     elif ask == "espresso" or ask == "latte" or ask == "cappuccino":
#         value = MENU[ask]["ingredients"]
#         if value["coffee"] > coffee:
#             print("Sorry there is not enough coffee.")
#         elif value["water"] > water:
#             print("Sorry there is not enough water.")
#         elif value["milk"] > milk:
#             print("Sorry there is not enough milk.")
#         else:
#             quarters = int(input("Please insert coins.\nhow many quarters?: ")) * 0.25
#             dimes = int(input("how many dimes?: ")) * 0.10
#             nickles = int(input("how many nickles?: ")) * 0.05
#             pennies = int(input("how many pennies?: ")) * 0.01
#             got_money = quarters + nickles + pennies + dimes
#
#             if MENU[ask]["cost"] <= got_money:
#                 if MENU[ask]["cost"] - got_money:
#                     print(f"Here is ${(got_money - MENU[ask]['cost']):.2f} dollars in change.")
#             else:
#                 print("Sorry that's not enough money. Money refunded.")
#                 return
#             money += MENU[ask]["cost"]
#             water -= value["water"]
#             milk -= value["milk"]
#             coffee -= value["coffee"]
#             print(f"Here is your {ask}. Enjoy!")
#     venting_machine(water, coffee, milk, money)
#
#
# venting_machine(300, 100, 200, 0)

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the totsl calculated from coins inserted"""
    quarters = int(input("Please insert coins.\nhow many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        # !important... because 'profit' variable here is treated as a local scope if not global is specified like this
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: "
              f"{resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



