t = int(input())

score = list(map(int, input().split()))

max_score = max(score)

avg = sum(score)/len(score)

print(avg/max_score*100)