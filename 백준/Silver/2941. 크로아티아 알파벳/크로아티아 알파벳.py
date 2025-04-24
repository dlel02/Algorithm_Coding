t = input()
count = 0
result = ''

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for _ in croatia:
    if _ in t:
        t = t.replace(_, 'a')
        
        
        

print(len(t))
        
