import random 
from os import system

players = [{
    "name": "Lionel Messi", "ballon d'ors": 7, "team": "Inter Miami"},
    {"name": "Cristiano Ronaldo", "ballon d'ors": 5, "team": "Al-Nassr"},
    {"name": "Karim Benzema", "ballon d'ors": 1, "team": "Al-Ittihad"},
    {"name": "Luka Modric", "ballon d'ors": 1, "team": "Real Madrid"},
    {"name": "Zinedine Zidane", "ballon d'ors": 1, "team": "Retired"},
    {"name": "Ronaldo Nazário", "ballon d'ors": 2, "team": "Retired"},
    {"name": "Ronaldinho Gaúcho", "ballon d'ors": 1, "team": "Retired"},
    {"name": "Kaká", "ballon d'ors": 1, "team": "Retired"},
    {"name": "George Weah", "ballon d'ors": 1, "team": "Retired"},
    {"name": "Marco van Basten", "ballon d'ors": 3, "team": "Retired"},
    {"name": "Michel Platini", "ballon d'ors": 3, "team": "Retired"},
    {"name": "Johan Cruyff", "ballon d'ors": 3, "team": "Retired"},
    {"name": "Franz Beckenbauer", "ballon d'ors": 2, "team": "Retired"},
    {"name": "Alfredo Di Stefano", "ballon d'ors": 2, "team": "Retired"},
    {"name": "Gerd Müller", "ballon d'ors": 1, "team": "Retired"},
    {"name": "Paolo Rossi", "ballon d'ors": 1, "team": "Retired"},
    {"name": "Jean-Pierre Papin", "ballon d'ors": 1, "team": "Retired"}
]

should_continue = True 
print("Welcome to the higher or lower game!!!!\n")
score = 0
player_a = random.choice(players)
player_b = random.choice(players)

def format_player(player):
    """Take the players info, and return the printable format"""
    player_name = player["name"]
    player_team = player["team"]
    if player_team == "Retired":
        return f"{player_name} is a retired football player."
    return f"{player_name} is a football player from {player_team}"

def check_answer(user_guess, a_ballons, b_ballons):
    if a_ballons > b_ballons:
        return user_guess == "a"
    elif a_ballons < b_ballons:
        return user_guess == "b"
    else:
        return "tie"  
    
while should_continue:
    reset = False
    while not reset: 
        if player_a == player_b:
            player_b = random.choice(players)
        elif player_a != player_b:
            reset = True

    print(f"Compare A: {format_player(player_a)}") 
    print("vs")
    print(f"Compare B: {format_player(player_b)}")

    choice = input("Who has more Ballon D'ors? Type 'A' or 'B': ").lower()

    a_ballon = player_a["ballon d'ors"]
    b_ballon = player_b["ballon d'ors"]
    is_correct = check_answer(choice, a_ballon, b_ballon)
    system('cls')
    if is_correct == "tie":
        print("It's a tie. No points awarded. The game continues.\n")
    elif is_correct:
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}.")
        should_continue = False
    
    player_a = player_b
    player_b = random.choice(players)
