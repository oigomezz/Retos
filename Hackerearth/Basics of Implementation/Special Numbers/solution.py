import math

n = int(input())
va = []


def f(val):
    if val > n:
        return
    if val > 0:
        va.append(val)
    f(10*val+4)
    f(10*val+7)


v = 0
f(v)

count = 0
cou = 0

for i in va:
    cou += 1
    for j in va[cou:]:
        if (math.gcd(i, j) == 1):
            count += 1

print(count)
