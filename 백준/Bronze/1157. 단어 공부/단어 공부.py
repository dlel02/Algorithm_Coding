alpha = input().upper()
set_alpha = list(set(alpha))
count = 0
keyword = ''


for _ in set_alpha:
    if count < alpha.count(_):
        count = alpha.count(_)
        keyword = _
set_alpha.remove(keyword)       
 
for _ in set_alpha:
    if alpha.count(keyword) == alpha.count(_):
        keyword = "?"
        
print(keyword)


        
    
    