def greet(nome):
    print(f"Hello, {nome}!")

def greet_with(name, location):
    print(f"Hello, {name}! You are from {location}.")

greet_with(location="Brazil", name="Alice")  # Keyword arguments allow you to specify the order of arguments

greet("Alice") 
