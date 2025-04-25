programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected.",
    "Function": "A block of code that only runs when it is called.", 
    "Loop": "The action of doing something over and over again.", 
    "Conditional": "A statement that only runs under certain conditions.", 
    "List": "A collection of items in a particular order.", 
    "Dictionary": "A changeable, unordered collection of items. Each item is stored as a pair of keys and values."}

programming_dictionary["Loop"] = "A reserved memory location to store values."
programming_dictionary["Conditional"] = "A statement that only runs under certain conditions."
print(programming_dictionary["Bug"])
print(programming_dictionary["Loop"])

for key in programming_dictionary:
    print(programming_dictionary[key])