x1 = int(input())
x2 = int(input())
x3 = int(input())

if x1 + x2 + x3 != 180:
    print('Error')
elif x1 == x2 == x3:
    print("Equilateral")
elif x1 + x2 + x3 == 180:
    if x1 == x2 or x1 == x3 or x2 == x3:
        print("Isosceles")
    else:
        print("Scalene")
