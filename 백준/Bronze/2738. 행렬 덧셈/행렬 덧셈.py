N, M = map(int, input().split())
A, B = [], []

for a in range(N):
    a_h = list(map(int, input().split()))
    A.append(a_h)
    
for b in range(N):
    b_h = list(map(int, input().split()))
    B.append(b_h)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = ' ')
    print()