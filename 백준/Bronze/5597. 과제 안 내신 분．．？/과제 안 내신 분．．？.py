import sys
student_number = []

for _ in sys.stdin:
    student_number.append(int(_.strip()))
for i in range(1, 31):
    if i not in student_number:
        print(i)       
    