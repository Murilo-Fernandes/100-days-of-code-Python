# Encode or Decode 

again = True 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"Your {encode_or_decode}d message is: {output_text}")

while (again):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    choice = input("Type 'yes' if you want to go again. Type 'no' if you want to stop. ").lower()
    if choice == "yes":
        break 
    else:
        again = False 
        print("Good Bye Mate.")