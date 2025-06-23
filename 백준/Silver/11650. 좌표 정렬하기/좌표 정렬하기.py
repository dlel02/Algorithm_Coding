N = int(input())

x = []

for i in range(N):
    x.append(list(map(int, input().split())))
    
x.sort()
for i in range(len(x)):
    print(x[i][0], x[i][1])
    