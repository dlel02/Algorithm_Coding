import sys
word = []
len_max = 0

for N in range(5):
    row = list(map(str, input()))
    word.append(row)
    if len(word[N]) > len_max:
        len_max = len(word[N])


for N in range(len_max):
    for M in range(5):
        try:
            print(word[M][N], end='')
        except:
            pass
    