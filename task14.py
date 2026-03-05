student_scores = [100, 85, 92, 78, 95]

max_score = max(student_scores)
print(max_score)

min_score = min(student_scores)
print(min_score)

sum_score = sum(student_scores)
print(sum_score)

avg_score = sum_score / len(student_scores)
print(avg_score)

max_scores = 0
for score in student_scores:
    if score > max_scores:
        max_scores = score
print(max_scores)

min_scores = 100
for score in student_scores:
    if score < min_scores:
        min_scores = score
print(min_scores)

sum_scores = 0
for score in student_scores:
    sum_scores += score
print(sum_scores)

avg_score = sum_scores / len(student_scores)
print(avg_score)
