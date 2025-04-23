S = input()

for char in range(ord('a'), ord('z') + 1):
    print(S.find(chr(char)), end=' ')