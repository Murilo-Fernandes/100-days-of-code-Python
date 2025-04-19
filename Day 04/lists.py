# how to use lists in python

fruits = ["apple", "banana", "cherry"]
print(fruits[2])  # prints the list of fruits
fruits[0] = "kiwi"  # 
fruits.append("orange")  # adds orange to the end of the list
fruits.extend(["mango", "grape"])  # adds mango and grape to the end 
fruits.insert(1, "lemon")  # adds lemon to the second position in the list
fruits.remove("banana")  # removes banana from the list
# fruits.pop(1)  # removes the second item in the list
# fruits.clear()  # clears the list 

print(fruits)  # prints the list of fruits