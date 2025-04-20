student_scores = [150, 100, 90, 85, 100, 95, 80, 70, 60, 50, 199, 177, 200, 150, 120, 130, 140, 160, 170, 180]

total_student_scores = sum(student_scores)
print(f"Total student scores: {total_student_scores}")
average_student_scores = total_student_scores / len(student_scores)
print(f"Average student scores: {average_student_scores:.2f}")
highest_student_score = max(student_scores)
print(f"Highest student score: {highest_student_score}")

max_score = 0
# max without function 
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Max score without function: {max_score}")

range(len(student_scores))
print(f"Range of student scores: {max(student_scores) - min(student_scores)}")