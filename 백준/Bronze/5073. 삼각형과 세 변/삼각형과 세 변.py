a = [list(map(int, line.split())) for line in open(0)]

for i in range(len(a)):
    a[i].sort()
    if sum(a[i]) == 0:
        break
    
    if a[i][2] >= a[i][0] + a[i][1]:
        print("Invalid")
        continue
    
    
    if a[i][0] == a[i][1] or a[i][0] == a[i][2] or a[i][1] == a[i][2]:
        if a[i][0] == a[i][1] == a[i][2]:
            print("Equilateral")
            continue
        print('Isosceles')
    else:
        print("Scalene") 