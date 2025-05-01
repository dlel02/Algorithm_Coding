M = int(input())
N = int(input())
sum_answer = []
min_answer = 0


for i in range(M, N+1):
    if i == 1:
        continue
    count = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            count = 1
            break
    if count == 0:
        sum_answer.append(i)
        
        
if len(sum_answer) == 0:
    print(-1)
else:
    print(sum(sum_answer))
    print(min(sum_answer))