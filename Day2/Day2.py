# Desafio é fazer uma calculadora do quanto você vai gastar num jantar 

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? "))
split = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100) * bill + bill
amount_per_person = bill_with_tip / split

print(f"Each person should pay: ${round(amount_per_person, 2)}")
