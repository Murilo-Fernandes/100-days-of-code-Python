file = open('example.txt')
content = file.read()
print(content)
file.close()

with open("Day 24/new_file.txt", mode="w") as file:
    file.write("o batman eh monstro.\n")

