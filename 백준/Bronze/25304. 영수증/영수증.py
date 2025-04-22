import sys

price = int(sys.stdin.readline())
t = int(sys.stdin.readline())
answer = 0

for _ in range(t):
    item, count = map(int, sys.stdin.readline().split())
    answer += item * count

if price == answer:
    print("Yes")
else:
    print("No")