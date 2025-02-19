from bisect import bisect_right, bisect_left


class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.sum = 0


tree = [Node() for _ in range(10000007)]
root = [None] * 200005
used = -1
MAXR = int(1e5) + 3


def md(s, e):
    return (s + e) // 2


def build(s, e):
    global used
    used += 1
    ret = tree[used]
    if s == e:
        return ret
    ret.l = build(s, md(s, e))
    ret.r = build(md(s, e) + 1, e)
    return ret


def update(now, i, v, s=0, e=MAXR):
    if e < i or i < s:
        return now
    global used
    used += 1
    ret = tree[used]
    if s == e:
        ret.sum = now.sum + v
        return ret
    ret.l = update(now.l, i, v, s, md(s, e))
    ret.r = update(now.r, i, v, md(s, e) + 1, e)
    ret.sum = ret.l.sum + ret.r.sum
    return ret


def find(now, l, r, s=0, e=MAXR):
    if r < s or e < l:
        return 0
    if l <= s and e <= r:
        return now.sum
    return find(now.l, l, r, s, md(s, e)) + find(now.r, l, r, md(s, e) + 1, e)


class Edge:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        return self.c < other.c


edge = [None] * 200005
p = list(range(200005))
val = [0] * 200005


def find_set(a):
    if a == p[a]:
        return a
    p[a] = find_set(p[a])
    return p[a]


def merge(e):
    a = e.a
    b = e.b
    c = e.c
    a = find_set(a)
    b = find_set(b)
    if a == b:
        return False
    if val[a] > val[b]:
        a, b = b, a
    root[c] = update(root[c], val[b], val[b])
    p[b] = a
    return True


compress = []
psum = [0] * 200005
N, Q = map(int, input().split())

for i in range(N - 1):
    a, b, c = map(int, input().split())
    edge[i] = Edge(a, b, c)
    compress.append(c)

compress.append(-1)
compress = sorted(set(compress))

for i in range(N - 1):
    edge[i].c = bisect_left(compress, edge[i].c)

edge = sorted(edge[:N - 1])

tot = 0
line = list(map(int, input().split()))
for i in range(1, N + 1):
    p[i] = i
    val[i] = int(line[i -1])
    tot += val[i]
    psum[val[i]] += val[i]

for i in range(1, MAXR + 1):
    psum[i] += psum[i - 1]

root[0] = build(0, MAXR)
i = 0
while i < N - 1:
    c = edge[i].c
    root[c] = root[c - 1]
    while i < N - 1 and edge[i].c == c:
        merge(edge[i])
        i += 1

ans = 0
for _ in range(Q):
    D, T, X = map(int, input().split())
    D ^= ans
    T ^= ans
    X ^= ans
    D = bisect_right(compress, D) - 1
    if T == 0:
        ans = 0
    else:
        ans = (tot - psum[min((X - 1) // T, MAXR)] -
               find(root[D], min((X + T - 1) // T, MAXR), MAXR)) * T
    print(ans)
