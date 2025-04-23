t = int(input())

for i in range(t):
    alpha = list(map(str, input().split()))
    for j in alpha[1]:
        print(j*int(alpha[0]), end='')
    print()
