def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    total_name = (name1 + name2).lower()

    for letter in total_name:
        if letter in "true":
            true_score += 1
        if letter in "love":
            love_score += 1

    punctuation = str(true_score) + str(love_score)
    print(punctuation)

calculate_love_score("Kim Kardashian", "Kanye West")

# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")