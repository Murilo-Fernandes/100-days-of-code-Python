print("Welcome to the Tip Calculator!") 

price = float(input("Enter the total bill amount: $")) # Total bill amount
tip = int(input("What percentage tip would you like to give? (10, 12, or 15): ")) # Tip percentage
people = int(input("How many people to split the bill? ")) # Number of people to split the bill
total_tip = (tip / 100) * price # Calculate the total tip
total_bill = price + total_tip # Calculate the total bill including tip
per_person = total_bill / people # Calculate the amount each person should pay

# Print the results
print(f"Total bill: ${round(total_bill, 2)}")
print(f"Each person should pay: ${per_person:.2f}")