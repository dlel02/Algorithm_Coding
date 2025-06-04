M = int(input())

result = 0

for i in range(1, M + 1):
    N = list(map(int, str(i)))
    result = sum(N) + i
    
    if result == M:
        print(i)
        break
    if i == M:
        print(0)
        break