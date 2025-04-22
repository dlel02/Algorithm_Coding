import sys

student_number = []

for line in sys.stdin:
    student_number.append(int(line.strip()))  # 줄바꿈 제거하고 정수로 변환

for i in range(1, 31):
    if i not in student_number:
        print(i)
