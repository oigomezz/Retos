N = 502
M = 500002

n, m, q, k = map(int, input().split())
a = [[0] * N for _ in range(N)]
st = [0] * M
e = [0] * M
dx = [1, 0]
dy = [0, 1]


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n

    def getPar(self, k):
        while self.par[k] != self.par[self.par[k]]:
            self.par[k] = self.par[self.par[k]]
        return self.par[k]

    def unite(self, u, v):
        par1 = self.getPar(u)
        par2 = self.getPar(v)
        if par1 == par2:
            return
        if self.sz[par1] > self.sz[par2]:
            self.sz[par1] += self.sz[par2]
            self.par[par2] = par1
        else:
            self.sz[par2] += self.sz[par1]
            self.par[par1] = par2


def get(y, x): return y * m + x


def get1(y, x): return (y - 1) * m + x - 1


def valid(y, x, lim): return y < n and x < m and a[y][x] <= lim


def check(lim):
    dsu = DSU(n * m)
    for i in range(n):
        for j in range(m):
            if a[i][j] > lim:
                continue
            for dir in range(2):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if valid(nx, ny, lim):
                    dsu.unite(get(i, j), get(nx, ny))
    cnt = 0
    for i in range(q):
        cnt += dsu.getPar(st[i]) == dsu.getPar(e[i])
        if cnt >= k:
            return 1
    return 0


def search(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(q):
    ys, xs, yd, xd = map(int, input().split())
    st[i] = get1(ys, xs)
    e[i] = get1(yd, xd)

ans = search(1, int(1e9))
print(ans)
