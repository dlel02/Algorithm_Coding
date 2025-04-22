t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dx = x2 - x1
    dy = y2 - y1
    distance = dx**2 + dy**2
    
 
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif distance == (r2 + r1)**2 or distance == (r2 - r1)**2:
        print(1)
    elif (r2 - r1) ** 2 < distance < (r2 + r1)**2:
        print(2)
    else:
        print(0)
      