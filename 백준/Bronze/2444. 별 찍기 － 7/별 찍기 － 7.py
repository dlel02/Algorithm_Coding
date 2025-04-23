t = int(input())

for i in range(1, t+1):
    print(" "*(t-i)+"*"*(2*i-1))
    
for j in range(t-1, 0, -1):
    print(" "*(t-j) + "*"*(2*j-1))