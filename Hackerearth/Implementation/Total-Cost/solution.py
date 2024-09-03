p, s, t, h, x = map(int, input().split())

cost = 0

for i in range(x):
    if (s <= t):
        cost = cost+h
        x = x-1
        s = s-1
    else:
        cost = cost+p
        x = x-1
        s = s-1

print(cost)
