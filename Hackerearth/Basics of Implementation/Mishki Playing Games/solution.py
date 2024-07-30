import math

n, q = map(int, input().split())
a = list(map(int, input().split()))
cumulative = [0]

for i in range(n):
    cumulative.append(cumulative[i] + math.floor(math.log2(a[i])) + 1)

for day in range(q):
    l, r = map(int, input().split())
    count = cumulative[r] - cumulative[l - 1]
    if count % 2 == 1:
        print('Mishki')
    else:
        print('Hacker')
