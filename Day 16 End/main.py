from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

card = Menu() 
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine():
    """Main function to run the coffee machine."""
    is_on = True

    while is_on: 
        options = card.get_items()
        choice = input(f"What would you like? ({options}): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            is_on = False

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        elif choice in options:
            drink = card.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    coffee_machine()