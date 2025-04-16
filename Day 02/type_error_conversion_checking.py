print(len("1234"))

print(type(277)) # This is an integer
print(type(3.14159)) # This is a floating point number
print(type("hello")) # This is a string
print(type(True)) # This is a boolean value 

int("1234") # This is a string converted to an integer
print(int("1234") + int("277")) # This is a string converted to an integer
float("3.14159") # This is a string converted to a floating point number
str(277) # This is an integer converted to a string
bool(1) # This is an integer converted to a boolean value (True)
name = input("What is your name? ") # This is a string input from the user

print(f"The number of letters in you name is: {len(name)}")