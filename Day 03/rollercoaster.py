print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? ")) # User's height in cm
age = int(input("What is your age? ")) # User's age in years
bill = 0

if height >= 120: # Check if the user is tall enough to ride
    print("You can ride the rollercoaster!")
    if age < 12:
        print("It will cost $5.")
        bill += 5
    elif age <= 18:
        print("It will cost $10.")
        bill += 10
    elif age >= 45 and age <= 55:
        print("It will be free, grandpa")
    else:
        print("It will cost $25, grandpa.")
        bill += 25

    photo = input("Do you want a photo taken? y or n: ")
    if photo == "y":
        bill += 3
        print("It will cost an additional $3 for the photo.")
    else: 
        print("No photo taken.")

else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")
    
print(f"Your total bill is ${bill}.")
