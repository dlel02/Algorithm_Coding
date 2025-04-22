N, X = map(int, input().split())
answer = list(map(int, input().split()))

for i in answer:  
    if i < X:
        print(i, end=' ')