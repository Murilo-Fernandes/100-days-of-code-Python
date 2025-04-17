# BMI Calculator with interpretations 

weight = float(input("Enter your weight in kg: ")) # Weight in kg
height = float(input("Enter your height in m: ")) # Height in meters

bmi = weight / (height ** 2) # Calculate BMI

if bmi < 18.5: 
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")  
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi:.2f}. You are obese (Class 1).") 
elif 35 <= bmi < 40:    
    print(f"Your BMI is {bmi:.2f}. You are obese (Class 2).") 
else:       
    print(f"Your BMI is {bmi:.2f}. You are obese (Class 3).")
