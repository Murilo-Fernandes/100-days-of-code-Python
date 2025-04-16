# BMI Calculator 

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height ** 2

print(round(bmi,2)) # This will round the result to 2 decimal places.
