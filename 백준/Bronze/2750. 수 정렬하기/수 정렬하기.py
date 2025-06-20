N = int(input())

cnt = []

for i in range(N):
    cnt.append(int(input()))
    
cnt.sort()

for i in range(len(cnt)):
    print(cnt[i])