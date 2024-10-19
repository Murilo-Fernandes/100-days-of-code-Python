student_scores = [123, 165, 142, 200, 321, 169, 124, 157, 198]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    
print(max_score)