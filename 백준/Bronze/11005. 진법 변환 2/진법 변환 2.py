N, B = map(int, input().split())
alpha = {str(i): chr(ord('A') + i - 10) for i in range(10, 36)}

def solution(n, q):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += alpha[str(mod)]
        else:
            rev_base += str(mod)  
    
    return rev_base[::-1]

answer = solution(N, B)
print(answer)
