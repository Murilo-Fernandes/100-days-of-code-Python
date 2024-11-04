print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza: Y or N: ")

# How much the people need to pay based on the size
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed something wrong, pal.")
# How much the people need to pay based on they wanting or not pepperoni

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    else:
        bill += 5

# How much the people need to pay based on they wanting or not extra cheese
if extra_cheese == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    else:
        bill += 5

print(f"Your total bill is ${bill}")