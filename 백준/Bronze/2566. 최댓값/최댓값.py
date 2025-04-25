answer = []
top = 0
index_a, index_b = 0, 0

for N in range(9):
    row = list(map(int, input().split()))
    answer.append(row)

for i in range(9):
    for j in range(9):
        if answer[i][j] > top:
            top = answer[i][j]
            index_a, index_b = i, j
print(top)
print(index_a+1, index_b+1)            