import sys
answer = []

for i in sys.stdin:
    a = int(i)
    answer.append(a)

count = max(answer)
for i in range(len(answer)):
    if answer[i] == count:
        print(count)
        print(i+1)
    