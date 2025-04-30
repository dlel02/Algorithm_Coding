N, K = map(int, input().split())
count = []


for _ in range(1, N + 1):
    if N % _ == 0:
        count.append(_) 
     

if K <= len(count):
    print(count[K-1])
else:
    print(0)