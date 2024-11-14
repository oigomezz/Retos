import sys
from collections import defaultdict

n, m = 0, 0
d = [[0] * 2050 for _ in range(2050)]
u = [[0] * 2050 for _ in range(2050)]
l = [[0] * 2050 for _ in range(2050)]
r = [[0] * 2050 for _ in range(2050)]
ul = [[0] * 2050 for _ in range(2050)]
dr = [[0] * 2050 for _ in range(2050)]
t = [0] * 2050
board = [[0] * 2050 for _ in range(2050)]


def add(ps, val):
    while ps <= n:
        t[ps] += val
        ps |= (ps + 1)


def sum_func(r):
    res = 0
    while r >= 0:
        res += t[r]
        r = (r & (r + 1)) - 1
    return res


def sum_range(l, r):
    return sum_func(r) - sum_func(l - 1)


n, m = map(int, input().split())
for i in range(n + 2):
    for j in range(m + 2):
        board[i][j] = 1

for i in range(1, n + 1):
    st = input()
    for j in range(1, m + 1):
        board[i][j] = int(st[j - 1])

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        r[i][j] = r[i][j + 1] + 1
        d[i][j] = d[i + 1][j] + 1
        if board[i][j] == 1:
            r[i][j] = d[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        u[i][j] = u[i - 1][j] + 1
        l[i][j] = l[i][j - 1] + 1
        if board[i][j] == 1:
            u[i][j] = l[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        ul[i][j] = min(u[i][j], l[i][j])
        dr[i][j] = min(d[i][j], r[i][j])

ans = 0
for Dif in range(-n - m, n + m + 1):
    event = defaultdict(list)
    for i in range(1, n + 1):
        event[i].clear()
    for i in range(n + 1):
        t[i] = 0
    for i in range(1, n + 1):
        for ps in event[i]:
            add(ps, -1)
        j = i + Dif
        if j < 1 or j > m:
            continue
        if board[i][j]:
            continue
        add(i, 1)
        q = dr[i][j]
        if i + q <= n:
            event[i + q].append(i)
        q = ul[i][j]
        ans += sum_range(i - q + 1, i)

print(ans)
