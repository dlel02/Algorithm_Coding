n = int(input())
answer = 0
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    
    x, y = map(int, input().split())
    
    for X in range(x, x+10):
        for Y in range(y, y+10):
            if X >= 100 or Y >= 100:
                break
            
            paper[X][Y] = 1

for i in range(100):
    answer += paper[i].count(1)

print(answer)    