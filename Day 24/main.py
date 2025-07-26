with open("Day 24/Input/Letters/starting_letter.txt", mode="r") as file:
    letter_template = file.read()

with open("Day 24/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    name = name.strip()
    letter = letter_template.replace("[name]", name)
    with open(f"Day 24/Output/ReadyToSend/letter_to_{name}.txt", mode="w") as file:
        file.write(letter)
