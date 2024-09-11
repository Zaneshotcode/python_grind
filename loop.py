# fruit = ["apple", "peach", "pear"]
# for fruit in fruit:
#     print(fruit)

student_scores = [150,142, 123, 123, 542, 524, 123, 123,145, 131, 114]

# total_exam_score = sum(student_scores)

# sum = 0
# for score in student_scores:
#     sum += score

# print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)