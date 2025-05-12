try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    age = int(input("Enter your age: "))
