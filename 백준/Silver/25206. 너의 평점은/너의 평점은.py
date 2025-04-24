import sys
grade_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0}
score_sum = 0
answer = 0
major = 0

for _ in range(20):
    name, score, grade = map(str, input().split())
    score = float(score)
    if grade == 'P':
        continue
    else:
        answer += score * grade_dict[grade]
        score_sum += score

print(answer/score_sum) 