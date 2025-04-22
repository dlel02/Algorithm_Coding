t = int(input())
l = list(map(int, input().split()))
hit = int(input())
count = 0


for i in range(t):
    if l[i] == hit:
        count += 1
print(count)
