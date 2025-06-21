# That's an app who will simulate a coffee machine
pennies = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}
coffe_flavor = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
} 

def process_coins():
    """Process the coins inserted by the user."""
    print("Please insert coins.")
    total = 0
    for coin, value in pennies.items():
        count = int(input(f"How many {coin}s? "))
        total += count * value
    return total

def check_price(coffe_type):
    """Check the price of the selected coffee."""
    prices = {
        "espresso": 1.50,
        "latte": 2.00,
        "cappuccino": 2.50,
    }
    return prices.get(coffe_type, 0)

def check_resources(coffe_type):
    """Check if there are enough resources to make the coffee."""
    for ingredient, amount in coffe_flavor[coffe_type].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def make_coffee(coffe_type):
    """Make the coffee and update resources."""
    for ingredient, amount in coffe_flavor[coffe_type].items():
        resources[ingredient] -= amount
    print(f"Here is your {coffe_type}. Enjoy!")

def coffee_machine():
    """Main function to run the coffee machine."""
    money = 0
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml"
                  f"\nMilk: {resources['milk']}ml"
                  f"\nCoffee: {resources['coffee']}g"
                  f"\nMoney: ${money:.2f} ")
            continue
        elif choice in coffe_flavor:
            if check_resources(choice):
                price = check_price(choice)
                print(f"The price for {choice} is ${price:.2f}.")
                inserted_money = process_coins()
                money += price
                if inserted_money >= price:
                    change = inserted_money - price
                    if change > 0:
                        print(f"Here is your change: ${change:.2f}.")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                continue
        elif choice == "refuel":
            print("Refueling resources...")
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
            continue
        else:
            print("Invalid choice. Please choose espresso, latte, or cappuccino.")

if __name__ == "__main__":
    coffee_machine()