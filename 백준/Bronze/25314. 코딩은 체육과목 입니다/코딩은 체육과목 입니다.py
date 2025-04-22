import sys
input = sys.stdin.readline

digit = int(input())

byte = digit // 4

for _ in range(byte):
    print('long', end=' ')
print('int')