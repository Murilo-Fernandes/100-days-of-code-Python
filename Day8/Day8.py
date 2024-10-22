# Caesar Cipher
again = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (original_text, shift_amount, decode_or_encode):
    new_phrase = ""
    if decode_or_encode == "decode":
        shift_amount = -shift_amount
    
    for letter in original_text:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_phrase += alphabet[index]
        else:
            new_phrase += letter
    print(f"This is the {decode_or_encode}d message: {new_phrase}")

while again:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if direction in ['encode', 'decode']:
            break
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")

    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    
    caesar(original_text=text,shift_amount=shift,decode_or_encode=direction)
    while True:
        choice = input("Type 'yes' if you want to go again. Type 'no' if you want to stop. ").lower()
        if choice == "no":
            print("Good Bye.")
            again = False
            break
        elif choice == "yes":
            print("Here we go again!")
            break
        else:
            print("Type 'yes' or 'no'!")



# def encrypt(original_text, shift_amount):
#     new_phrase = ""
#     for letter in original_text:
#         if letter in alphabet:
#             index = (alphabet.index(letter) + shift_amount) % len(alphabet)
#             new_phrase += alphabet[index]
#         else:
#             new_phrase += letter
#     print(f"this is the encoded message: {new_phrase}")

# def decrypt(original_text, shift_amount):
#     new_phrase = ""
#     for letter in original_text:
#         if letter in alphabet:
#             index = (alphabet.index(letter) - shift_amount) % len(alphabet)
#             new_phrase += alphabet[index]
#         else:
#             new_phrase += letter
#     print(f"This is the decoded message: {new_phrase}")