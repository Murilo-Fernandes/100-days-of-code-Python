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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True

def is_resources_sufficient(order_ingredients):
    """Returns true when the order can be made, and false otherwise"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False 
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total 

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit  
        profit += drink_cost
        print(f"Your change is ${change}")
        return True
    else: 
        print("Not enough money. Money refunded.")
        return False

def report(resource):
    """Returns all the current resources"""
    return f"water: {resource['water']}ml\nmilk: {resource['milk']}ml\ncoffee: {resource['coffee']}ml"

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    try:
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(report(resources))
        else:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(money_received=payment, drink_cost=drink["cost"]):
                    for item in drink["ingredients"]:
                        resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {choice} ☕.")
    except KeyError:
        print("Invalid choice. Please choose a valid option: espresso, latte, or cappuccino.")
