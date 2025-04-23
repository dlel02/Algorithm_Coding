ches = list(map(int, input().split()))
check = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(ches)):
    answer.append(check[i] - ches[i])
    
print(*answer)
    