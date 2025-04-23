alpha = input()
count = 0
now = 0

number = {}
for ch in "ABC":
    number[ch] = 2
for ch in "DEF":
    number[ch] = 3
for ch in "GHI":
    number[ch] = 4
for ch in "JKL":
    number[ch] = 5
for ch in "MNO":
    number[ch] = 6
for ch in "PQRS":
    number[ch] = 7
for ch in "TUV":
    number[ch] = 8
for ch in "WXYZ":
    number[ch] = 9

for i in alpha:
    count += number[i]+1
    
print(count)