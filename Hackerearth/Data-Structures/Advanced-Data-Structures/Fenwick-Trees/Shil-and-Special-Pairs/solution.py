INF = 1e18
MOD = 1000000007
maxn = int(1e5) + 6
Q = [None] * maxn


class Query:
    def __init__(self, l, r, pos):
        self.l = l
        self.r = r
        self.pos = pos

    def __lt__(self, other):
        return self.r < other.r


def update(ind):
    while ind <= n:
        BIT[ind] += 1
        ind += ind & (-ind)


def query(ind):
    suma = 0
    while ind > 0:
        suma += BIT[ind]
        ind -= ind & (-ind)
    return suma


n, m, d = map(int, input().split())
a = [0] * maxn
pos = [0] * maxn
res = [0] * maxn
BIT = [0] * maxn
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = arr[i - 1]
    pos[a[i]] = i

for i in range(m):
    l, r = map(int, input().split())
    Q[i] = Query(l, r, i)

Q = sorted(Q[:m])
k = 0
for i in range(1, n + 1):
    for j in range(max(1, a[i] - d), min(n, a[i] + d) + 1):
        if pos[j] <= i:
            update(pos[j])

    while k < m and Q[k].r == i:
        res[Q[k].pos] = query(i) - query(Q[k].l - 1)
        k += 1

for i in range(m):
    print(res[i])
