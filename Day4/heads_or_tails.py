import random

# Heads or Tails game

value = random.randint(1, 10)

print(value)
if value <= 5:
    print("Heads.")
else:
    print("Tails.")