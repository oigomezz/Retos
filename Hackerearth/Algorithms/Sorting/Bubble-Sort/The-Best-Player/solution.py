from collections import defaultdict

n, t = map(int, input().strip().split())
d = defaultdict(list)
for i in range(n):
    name, fan_quotient = input().strip().split()
    d[int(fan_quotient)].append(name)
fans = sorted(d, reverse=True)
max_fan = t
for i in range(t):
    d[fans[i]].sort()
    for j in d[fans[i]]:
        if max_fan == 0:
            break
        print(j)
        max_fan -= 1
    if max_fan == 0:
        break
