enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

player_health = 10

# Local Scope
def game(): 
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

game()


