t = int(input())
count = 0

for _ in range(t):
    alpha = input()
    seen = set()
    prev = ''
    answer = True
    
    for i in alpha:
        if i != prev:
            if i in seen:
                answer = False
                break
            seen.add(i)
        prev = i
    if answer:
        count +=1

print(count)
                