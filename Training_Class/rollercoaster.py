print("Welcome to rollercoaster box office!")
height = int(input("What's your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster, cody rhodes.")
    age = int(input("What's you age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    elif age >= 45 and age <= 55:
        print("You're too old bruv, you can ride for free.")
    else: 
        print("Adult tickets are $12.")
        bill += 12
    wants_pic = input("Do you want a photo taken? Y or N. ")
    if wants_pic == "Y":
        bill += 3
        print(f"Your total bill is ${bill}.")
    else:
        print(f"Your total bill is ${bill}.")
        
else: 
    print("You're too small, you can't ride.")