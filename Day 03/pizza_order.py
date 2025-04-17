print("Welcome to Python Pizza Delivery")

size = input("What size pizza do you want? S, M, or L: ").upper() # User's pizza size 
pepperoni = input("Do you want pepperoni? Y or N: ").upper() # User's choice for pepperoni
extra_cheese = input("Do you want extra cheese? Y or N: ").upper() # User's choice for extra cheese
bill = 0 

if size == "S": # Check if the size is small
    bill += 15 # Add the cost of small pizza
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y": # Check if the user wants pepperoni
    if size == "S":
        bill += 2 # Add the cost of pepperoni for small pizza
    else:
        bill += 3 # Add the cost of pepperoni for medium and large pizzas
else:
    print("No pepperoni added.")

if extra_cheese == "Y": # Check if the user wants extra cheese
    bill += 1 # Add the cost of extra cheese
else:
    print("No extra cheese added.")

print(f"Your final bill is: ${bill:.2f}") # Print the final bill