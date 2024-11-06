game_level = 10
enemies = ["Skeleton", "Alien", "Zombie", "Cowboy"]
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    else:
        new_enemy = enemies[3]

    print(new_enemy)

create_enemy()

