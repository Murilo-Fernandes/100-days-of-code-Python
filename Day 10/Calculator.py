# This is a simple calculator program that performs basic arithmetic operations.
# In the function it will return True or False to continue or stop the program.
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculator():
    """All the calculator functions are in this function."""
    
    n1 = float(input("What's the first number? "))

    while True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        answer = operations[operation_symbol](n1, float(input("What's the second number? ")))
        os.system('cls')
        print(f"answer = {answer}")

        while True:
            choice = input(f"Type 'y' to continue calculating with {answer}, 's' to stop calculating or 'n' to start a new calculation: ").lower()
            if choice == "y":
                n1 = answer
                break
            elif choice == "s":
                print("Goodbye!")
                return False
            elif choice == "n":
                os.system('cls')
                return True 
            else:
                print("Please enter 'y', 's', or 'n'.")
                continue

operations = { 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide, } 


while True:
    if not calculator():
        break
    

