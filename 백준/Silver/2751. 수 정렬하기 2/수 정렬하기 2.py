import sys

N = int(sys.stdin.readline())
cnt = []

for i in range(N):
    cnt.append(int(sys.stdin.readline()))
    
cnt.sort()

for i in cnt:
    print(i)