a, b = map(str, input().split())

r_a = ''
r_b = ''

for i in a[::-1]:
    r_a += i

for i in b[::-1]:
    r_b += i

if int(r_a) >= int(r_b):
    print(int(r_a))

else:
    print(int(r_b))
    