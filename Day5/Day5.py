# Password generator 
import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_amount = int(input("How many letters would you like on your password?\n"))
numbers_amount = int(input("How many numbers would you like on your password?\n"))
symbols_amount = int(input("How many symbols would you like on your password?\n"))


# Hard Level

password_list = []
password = ""
random_character = ""

for quantidade in range(letters_amount):
    random_character = random.choice(letters)
    password_list.append(random_character)

for quantidade in range(numbers_amount):
    random_character = random.choice(numbers)
    password_list.append(random_character)

for quantidade in range(symbols_amount):
    random_character = random.choice(symbols)
    password_list.append(random_character)

random.shuffle(password_list)
for character in password_list:
    password += character

print(letters)
print(numbers)
print(symbols)

print(f"Your password could be: {password} ")




#Easy Level 

# password_list = []
# password = ""
# random_character = ""

# for quantidade in range(letters_amount):
#     random_character = random.choice(letters)
#     password += random_character

# for quantidade in range(numbers_amount):
#     random_character = random.choice(numbers)
#     password += random_character

# for quantidade in range(symbols_amount):
#     random_character = random.choice(symbols)
#     password += random_character

# print(password)