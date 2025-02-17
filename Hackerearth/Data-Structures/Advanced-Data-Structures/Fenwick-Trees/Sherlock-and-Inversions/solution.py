import math
from bisect import bisect_left

N = 1e5 + 5
sq = math.sqrt(N)


class Query:
    def __init__(self, l, r, id):
        self.l = l
        self.r = r
        self.id = id

    def __lt__(self, other):
        if self.l // sq != other.l // sq:
            return self.l < other.l
        if (self.l // sq) % 2 == 1:
            return self.r < other.r
        return self.r > other.r


class Fenwick:
    def __init__(self, n):
        self.n = n + 1
        self.fen = [0] * (n + 1)

    def update(self, x, val):
        x += 1
        while x < self.n:
            self.fen[x] += val
            x += x & -x

    def query(self, x):
        res = 0
        x += 1
        while x > 0:
            res += self.fen[x]
            x -= x & -x
        return res

    def query_range(self, l, r):
        return self.query(r) - self.query(l - 1)


n, x = map(int, input().split())
a = []
t = []
arr = list(map(int, input().split()))
for i in range(n):
    a.append(int(arr[i]))
    t.append(a[i])

res = [0] * x
q = []
for i in range(x):
    line = list(map(int, input().split()))
    l, r = line[0] - 1, line[1] - 1
    q.append(Query(l, r, i))

q.sort()
t.sort()
for i in range(n):
    a[i] = bisect_left(t, a[i]) + 1

ds = Fenwick(n + 5)
inv = 0
l = 0
r = 0

for i in range(x):
    while r <= q[i].r:
        inv += ds.query_range(a[r] + 1, n + 4)
        ds.update(a[r], 1)
        r += 1
    while r - 1 > q[i].r:
        r -= 1
        ds.update(a[r], -1)
        inv -= ds.query_range(a[r] + 1, n + 4)
    while l > q[i].l:
        l -= 1
        inv += ds.query_range(0, a[l] - 1)
        ds.update(a[l], 1)
    while l < q[i].l:
        ds.update(a[l], -1)
        inv -= ds.query_range(0, a[l] - 1)
        l += 1
    res[q[i].id] = inv

for i in range(x):
    print(res[i])
