import sys
input = sys.stdin.readline
N, M = map(int, input().split())
answer = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    
    for a in range(i, j+1):
        answer[a-1] = k
   
for s in answer:
    print(s, end=' ')        
    