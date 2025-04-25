# Nested List in Dictionary 

capitals = { 
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Italy": ["Rome", "Milan", "Naples"],
    "Spain": ["Madrid", "Barcelona", "Valencia"],
}

Travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

nested_dictionary = {
    "France": Travel_log["France"],
    "Germany": "Berlin",
}

nested_list = ['A', 'B', ['C', 'D', 'E'], 'F']
print(nested_list[2][1])
print(Travel_log["France"][1])