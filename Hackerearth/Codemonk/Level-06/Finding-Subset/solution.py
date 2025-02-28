from collections import defaultdict
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def sqrt_integer(x):
    y = int(math.sqrt(x))
    while y * y < x:
        y += 1
    while y * y > x:
        y -= 1
    return y if y * y == x else -1


ispr = [0] * (1 << 17)
pr = []
oo = {}

for i in range(2, 2156):
    if is_prime(i):
        pr.append(i)

for i in range(2, 1 << 17):
    if is_prime(i):
        ispr[i] = 1
        oo[i * i] = 1

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

ans = 0
mem = [[] for _ in range(n)]
mp = defaultdict(int)
used = set()

for i in range(n):
    y = int(a[i] ** (1/3))
    while y * y * y < a[i]:
        y += 1
    while y * y * y > a[i]:
        y -= 1

    if y * y * y == a[i]:
        if ans == 0:
            ans += 1
        continue

    x = a[i]
    cur = []
    for j in range(len(pr)):
        if x % pr[j] == 0:
            cnt = 0
            while x % pr[j] == 0:
                x //= pr[j]
                cnt += 1
            if cnt % 3 != 0:
                cur.append((pr[j], cnt % 3))

    if x < 100000 and ispr[x]:
        cur.append((x, 1))
        x = 1

    y = sqrt_integer(x)
    if y != -1 and ispr[y]:
        cur.append((y, 2))
        x = 1

    if x != 1:
        cur.append((200000 + i, 1))

    assert cur
    mem[i] = cur
    mp[tuple(cur)] += 1

for i in range(n):
    if not mem[i]:
        continue
    cur = mem[i]
    if tuple(cur) in used:
        continue
    oth = cur[:]
    for j in range(len(oth)):
        oth[j] = (oth[j][0], 3 - oth[j][1])
    ans += max(mp[tuple(cur)], mp[tuple(oth)])
    used.add(tuple(cur))
    used.add(tuple(oth))

print(ans)
