from collections import defaultdict


def root(u):
    if fa[u] == u:
        return u
    fa[u] = root(fa[u])
    return fa[u]


n, m = map(int, input().split())
fa = list(range(2 * n + 1))
e = defaultdict(list)

for _ in range(m):
    l, r = map(int, input().split())
    length = r - l + 1
    r = 2 * n - r + 1
    for i in range(30, -1, -1):
        if (1 << i) <= length:
            e[i].append((l, r))
            l += (1 << i)
            r += (1 << i)
            length -= (1 << i)

for k in range(30, -1, -1):
    for i in range(1, 2 * n + 1):
        fa[i] = i
    for it in e[k]:
        fa[root(it[0])] = root(it[1])
    if k == 0:
        break
    for u in range(1, 2 * n + 1):
        ru = root(u)
        np = (1 << (k - 1))
        if u != ru:
            e[k - 1].append((u, ru))
            e[k - 1].append((u + np, ru + np))

for i in range(1, n + 1):
    fa[root(i)] = root(2 * n - i + 1)

s = set()
for i in range(1, 2 * n + 1):
    s.add(root(i))

print(len(s))
