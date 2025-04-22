N, X = map(int, input().split())
answer = map(int, input().split())

for i in answer:  
    if i < X:
        print(i, end=' ')