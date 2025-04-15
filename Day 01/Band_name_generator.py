# This program generates a band name based on the user's input.
print("Welcome to the band name generator!")

# Variables initialization
city = input("What's the name of the city you grew up in? ")
pet = input("What's your pet's name? ")

# Concatenating the city and pet name to create a band name
band_name = city + " " + pet

# Displaying the generated band name
print("Your band name could be: " + band_name)