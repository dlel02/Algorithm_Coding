cnt = [int(input()) for _ in range(5)]

cnt.sort()

avg = sum(cnt) // 5
mid = cnt[2]

print(avg)
print(mid)