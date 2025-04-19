# A code to define who will pay the bill for a group of friends at a restaurant. The code randomly selects one of the friends to pay the bill. It also includes a function to get the name of the friend who will pay the bill and a function to display the result. 
import random 

buddies = ["Dick Grayson", "Bruce Wayne", "Barbara Gordon", "Tim Drake", "Jason Todd", "Alfred Pennyworth", "Selina Kyle"]
unlucky = random.choice(buddies)

print(f"{unlucky} is going to pay the bill.")