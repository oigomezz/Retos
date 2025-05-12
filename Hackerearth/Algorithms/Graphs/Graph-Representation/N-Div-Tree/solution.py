from collections import defaultdict

n = 0
dfn = [0] * 100009
tot = 0
end = [0] * 100009
anc = [[0] * 20 for _ in range(100009)]
tag = [0] * 400009
suma = [0] * 400009
ne = defaultdict(list)
evt = defaultdict(list)


class Tri:
    def __init__(self, a=0, b=0, f=False):
        self.a = a
        self.b = b
        self.f = f


def dfs(x, fa):
    global tot
    dfn[x] = tot + 1
    tot += 1
    anc[x][0] = fa
    for i in range(1, 20):
        anc[x][i] = anc[anc[x][i - 1]][i - 1]
    for y in ne[x]:
        if y != fa:
            dfs(y, x)
    end[x] = tot


def isanc(u, v):
    return dfn[u] <= dfn[v] and end[v] <= end[u]


def up(u, v):
    for i in range(19, -1, -1):
        if isanc(u, anc[v][i]) and u != anc[v][i]:
            v = anc[v][i]
    return v


def addrec(x1, x2, y1, y2):
    if 1 <= x1 <= x2 <= n and 1 <= y1 <= y2 <= n:
        evt[x1].append(Tri(y1, y2, True))
        evt[x2 + 1].append(Tri(y1, y2, False))


def add(u, v):
    if dfn[u] > dfn[v]:
        u, v = v, u
    if isanc(u, v):
        r = up(u, v)
        addrec(1, dfn[r] - 1, dfn[v], end[v])
        addrec(dfn[v], end[v], end[r] + 1, n)
    else:
        addrec(dfn[u], end[u], dfn[v], end[v])


def get(x, l, r):
    if tag[x]:
        return r - l + 1
    else:
        return suma[x]


def mdf(x, l, r, ql, qr, f):
    if ql <= l and r <= qr:
        if f:
            tag[x] += 1
        else:
            tag[x] -= 1
        return
    mid = (l + r) >> 1
    if ql <= mid:
        mdf(x << 1, l, mid, ql, qr, f)
    if qr > mid:
        mdf(x << 1 | 1, mid + 1, r, ql, qr, f)
    suma[x] = get(x << 1, l, mid) + get(x << 1 | 1, mid + 1, r)


def qsum(x, l, r, ql, qr):
    if tag[x]:
        return min(qr, r) - max(ql, l) + 1
    if ql <= l and r <= qr:
        return get(x, ql, qr)
    mid = (l + r) >> 1
    ret = 0
    if ql <= mid:
        ret += qsum(x << 1, l, mid, ql, qr)
    if qr > mid:
        ret += qsum(x << 1 | 1, mid + 1, r, ql, qr)
    return ret


if __name__ == "__main__":
    n = int(input())
    for i in range(1, n):
        u, v = map(int, input().strip().split())
        ne[u].append(v)
        ne[v].append(u)

    dfs(1, 0)
    for i in range(1, n + 1):
        for j in range(i + i, n + 1, i):
            add(i, j)

    ans = (n * (n - 1)) // 2
    for i in range(1, n):
        for x in evt[i]:
            mdf(1, 1, n, x.a, x.b, x.f)
        ans -= qsum(1, 1, n, i + 1, n)
    print(ans)
