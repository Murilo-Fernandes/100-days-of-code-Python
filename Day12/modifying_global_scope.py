enemies = 1

def increase_enemies(enemy):
    print(f"Enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"Enemies outside function: {enemies}")