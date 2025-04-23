def calculate_love_score(name1, name2):
    t = 0 
    l = 0
    combined_names = name1 + name2  
    for letter in combined_names:
        if letter.upper() in "TRUE":
            t += 1
        if letter.upper() in "LOVE":
            l += 1
    
    pontuation = str(t) + str(l)
    print(pontuation)
    
calculate_love_score("Kanye West", "Kim Kardashian")