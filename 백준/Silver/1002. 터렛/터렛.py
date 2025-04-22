import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.dist((x1, y1), (x2, y2))  

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        print(1)
    elif abs(r1 - r2) < dist < r1 + r2:
        print(2)
    else:
        print(0)
