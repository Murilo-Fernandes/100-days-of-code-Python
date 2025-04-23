def life_in_weeks(age):
    rest = 90 - age 
    weeks_left = rest * 52 
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(int(input("Enter your age: ")))