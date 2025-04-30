N = int(input())
num_list = [0] * N
point = 0
num_list = list(map(int, input().split()))


for i in range(len(num_list)):
    count = 0
    if num_list[i] == 1:
        continue
    for _ in range(2, num_list[i]):
        if num_list[i] % _ == 0:
            count = 1
            break
    if count != 1:
        point += 1

print(point)