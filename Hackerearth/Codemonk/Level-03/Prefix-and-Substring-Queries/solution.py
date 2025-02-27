from collections import defaultdict

n, q = map(int, input().split())
s = input()
adj = defaultdict(list)
qry = defaultdict(list)
p = [0] * (300010)
h = [0] * (300010)
lca = [[0] * 20 for _ in range(300010)]
answer = [-1] * (300010)
sz = [0] * (300010)


class BIT:
    def __init__(self, n):
        self.bit_array = [0] * (n + 5)

    def update(self, pos, val):
        if not pos:
            return
        while pos < len(self.bit_array):
            self.bit_array[pos] += val
            pos += pos & (-pos)

    def sum(self, pos):
        ans = 0
        while pos:
            ans += self.bit_array[pos]
            pos -= pos & (-pos)
        return ans


bit = BIT(n)


def add(c, pos):
    p[pos] = p[pos - 1]
    while p[pos] and s[p[pos]] != c:
        p[pos] = p[p[pos] - 1]
    p[pos] += c == s[p[pos]]
    u = pos + 1
    lca[u][0] = p[pos]
    h[u] = h[p[pos]] + 1
    for i in range(1, 20):
        lca[u][i] = lca[lca[u][i - 1]][i - 1]
    adj[lca[u][0]].append(u)


def build_kmp():
    adj[0].append(1)
    for i in range(1, len(s)):
        add(s[i], i)


def get_lca(u, v):
    if h[u] < h[v]:
        u, v = v, u
    d = h[u] - h[v]
    for i in range(20):
        if d & (1 << i):
            u = lca[u][i]
    if u == v:
        return u
    for i in range(19, -1, -1):
        if lca[u][i] != lca[v][i]:
            u = lca[u][i]
            v = lca[v][i]
    return lca[u][0]


def build_tree(u):
    sz[u] = 1
    for v in adj[u]:
        build_tree(v)
        sz[u] += sz[v]


def dfs(u, val):
    bit.update(u, val)
    for v in adj[u]:
        dfs(v, val)


def sack(u, keep):
    big = -1
    for v in adj[u]:
        if big == -1 or sz[v] > sz[big]:
            big = v
    for v in adj[u]:
        if v != big:
            sack(v, 0)
    if big != -1:
        sack(big, 1)
    for v in adj[u]:
        if v != big:
            dfs(v, 1)
    bit.update(u, 1)
    for id, l, r in qry[u]:
        answer[id] = bit.sum(r) - bit.sum(l - 1)
    if not keep:
        dfs(u, -1)


build_kmp()
for _ in range(q):
    op, *line = map(str, input().split())
    op = int(op)
    if op == 1:
        c = line[0]
        add(c, len(s))
        s += c
        n += 1
    elif op == 2:
        l, r = int(line[0]), int(line[1])
        answer[_] = get_lca(l, r)
    else:
        x, l, r = int(line[0]), int(line[1]), int(line[2])
        if l + x - 1 > r:
            answer[_] = 0
        else:
            qry[x].append((_, l + x - 1, r))

bit = BIT(n)
build_tree(0)
sack(0, 0)
for i in range(q):
    if answer[i] != -1:
        print(answer[i])
