enemies = "Skeleton"

def increase_enemies():
    enemies = "Scarecrow"
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

bruces = 1 

def increase_bruce(bruces):
    bruces += 1
    print(f"Bruces inside function: {bruces}") 
    return bruces + 1

increase_bruce(bruces)
print(f"Bruces outside function: {bruces}")
bruces = increase_bruce(bruces)
print(f"Bruces outside function: {bruces}")