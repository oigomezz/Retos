s = input()

s += s[-1]
limit = len(s)
count = 1
maximum = 1

for i in range(limit-1):
    if s[i+1] != s[i]:
        count += 1
    else:
        maximum = maximum if maximum > count else count
        count = 1

maximum = maximum if maximum > count else count
print(maximum)
