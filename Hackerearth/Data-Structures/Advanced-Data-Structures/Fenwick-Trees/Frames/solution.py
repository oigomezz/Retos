from collections import defaultdict


def min_pair(p):
    return min(p[0], p[1])


def update(k, delta):
    while k <= MAX:
        BIT[k] += delta
        k += k & -k


def get_sum(k):
    ret = 0
    while k > 0:
        ret += BIT[k]
        k -= k & -k
    return ret


MAXN = int(2e3 + 3)
BIT = [0] * MAXN
mat = [[''] * MAXN for _ in range(MAXN)]
dp = [[(0, 0)] * MAXN for _ in range(MAXN)]
rdp = [[(0, 0)] * MAXN for _ in range(MAXN)]
top = []
del_list = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n + 1):
    mat[i] = [''] + list(input().strip())
    for j in range(1, m + 1):
        if mat[i][j] == '0':
            dp[i][j] = (dp[i][j - 1][0] + 1, dp[i - 1][j][1] + 1)

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if mat[i][j] == '0':
            rdp[i][j] = (rdp[i][j + 1][0] + 1, rdp[i + 1][j][1] + 1)

x, y, pos = 0, 0, 0
MAX = min(m, n)
top.append((1, 1))
for i in range(2, n + 1):
    top.append((i, 1))
for i in range(2, m + 1):
    top.append((1, i))

res = 0
for i in range(len(top)):
    x, y = top[i]
    pos = 0
    BIT[:] = [0] * MAXN
    del_list.clear()
    while x <= n and y <= m:
        pos += 1
        for j in del_list[pos]:
            update(j, -1)
        if mat[x][y] == '0':
            del_list[pos + min_pair(rdp[x][y])].append(pos)
            update(pos, 1)
            res += get_sum(pos) - get_sum(pos - min_pair(dp[x][y]) - 1)
        x += 1
        y += 1
print(res)
