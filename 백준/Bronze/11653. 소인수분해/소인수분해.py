T = int(input())
count = 2
answer= 0

while T >= 0:
    
    if T % count == 0:
        print(count)
        T = T // count
        continue
    else:
        count += 1
    if T < count:
        break
    