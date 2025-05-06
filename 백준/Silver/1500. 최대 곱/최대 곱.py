S, K = map(int, input().split())

q = S // K
r = S % K

nums = [q+1]*r + [q]*(K - r)

result = 1
for num in nums:
    result *= num

print(result)