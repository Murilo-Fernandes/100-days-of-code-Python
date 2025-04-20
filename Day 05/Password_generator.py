import random
# This program generates a random password based on user-defined criteria.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "ä", "&", "(", ")", "*", "+", "-", "=", "_", "{", "}", "[", "]", ";", ":", "'", '"', "<", ">", ",", ".", "?"]

print("Welcome to the Password Generator!")
password = ""
nr_letters = int(input("How many letters would you like in your password?\n")) # Number of letters
nr_symbols = int(input("How many symbols would you like?\n")) # Number of symbols
nr_numbers = int(input("How many numbers would you like?\n")) # Number of numbers
password_list = []


#easy level and hard level

for char in range(1, nr_letters + 1): # Loop to generate letters
    password += random.choice(letters)
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers):
    password += random.choice(number)
    password_list.append(random.choice(number))

for char in range(1, nr_symbols):
    password += random.choice(symbols)
    password_list.append(random.choice(symbols))

print(f"Your password could be: {password}") # easy level
print(f"Your password could be: {''.join(password_list)}") # hard level



