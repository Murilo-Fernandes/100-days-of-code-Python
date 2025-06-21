from prettytable import PrettyTable 

table = PrettyTable()

table.add_column("Pokémon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"]) 
table.align = "l"
table.align["Type"] = "r"
print(table)
