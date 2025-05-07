T = int(input())
x_len = []
y_len = []
for i in range(T):
    x = list(map(int, input().split()))
    x_len.append(x[0])
    y_len.append(x[1])
    
x = max(x_len) - min(x_len)
y = max(y_len) - min(y_len)

print(x*y)
