import sys
number = []
count = 0
answer =[]

for i in sys.stdin:
    number.append(int(i))
    
for j in range(len(number)):
    if number[j] % 42 not in answer:
        answer.append(number[j]%42)
        count += 1
print(count)