# Caesar Cypher Code 
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop = False 

# ### def encode(original_text, shift):
#     cypher_message = ""
#     for letter in original_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift) % 26
#             cypher_message += alphabet[new_position]
#         else:
#             cypher_message += letter  
#     print(f"The original text is: {original_text}")
#     print(f"The encoded text is: {cypher_message}")

# def decode(original_text, shift):
#     cypher_message = ""
#     for letter in original_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift) % 26
#             cypher_message += alphabet[new_position]
#         else:
#             cypher_message += letter  
#     print(f"The original text is: {original_text}")
#     print(f"The decoded text is: {cypher_message}") 

def caesar_cypher(original_text, shift, direction):
    cypher_message = ""
    encode_or_decoded = "encoded"

    if direction == "decode":
            shift = -shift 
            encode_or_decoded = "decoded"

    for letter in original_text: 
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            cypher_message += alphabet[new_position]
        else:
            cypher_message += letter

    print(f"The original text is: {original_text}")
    print(f"The {encode_or_decoded} message is: {cypher_message}")


while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    os.system('cls')

    caesar_cypher(original_text, shift, direction)
    
    choice = input("Do you want to continue? (Y/N): ").lower()
    if choice == "n":
        stop = True
        print("Thanks for using the Caesar Cypher program!")
    elif choice == "y":
        os.system('cls')
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        
    

    