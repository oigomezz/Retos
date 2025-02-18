MOD = 1000000007
INF = int(1e9)


def bit_count(_x):
    _ret = 0
    while _x:
        if _x % 2 == 1:
            _ret += 1
        _x //= 2
    return _ret


def bit(_mask, _i):
    return 0 if (_mask & (1 << _i)) == 0 else 1


def powermod(_a, _b, _m=MOD):
    _r = 1
    while _b:
        if _b % 2 == 1:
            _r = (_r * _a) % _m
        _b //= 2
        _a = (_a * _a) % _m
    return _r


def add(a, b, m=MOD):
    x = a + b
    while x >= m:
        x -= m
    while x < 0:
        x += m
    return x


def sub(a, b, m=MOD):
    x = a - b
    while x < 0:
        x += m
    while x >= m:
        x -= m
    return x


def mul(a, b, m=MOD):
    x = a * b
    x %= m
    while x < 0:
        x += m
    return x


class SegtreeNode:
    def __init__(self, l=0, r=0, best=0, sz=0):
        self.l = l
        self.r = r
        self.best = best
        self.sz = sz


class Segtree:
    MAXN = 4000010

    def __init__(self, m):
        self.size = m
        self.seg_tree = [SegtreeNode() for _ in range(4 * (m + 1))]

    def merge_seg_tree(self, a, b):
        temp = SegtreeNode()
        temp.sz = a.sz + b.sz
        if a.l == a.sz:
            temp.l = a.sz + b.l
        else:
            temp.l = a.l
        if b.r == b.sz:
            temp.r = b.sz + a.r
        else:
            temp.r = b.r
        temp.best = max(a.best, b.best)
        temp.best = max(temp.best, a.r + b.l)
        return temp

    def build_seg_tree(self, s, e, idx):
        if s == e:
            self.seg_tree[idx].l = 0
            self.seg_tree[idx].r = 0
            self.seg_tree[idx].best = 0
            self.seg_tree[idx].sz = 1
        else:
            mid = (s + e) >> 1
            self.build_seg_tree(s, mid, 2 * idx + 1)
            self.build_seg_tree(mid + 1, e, 2 * idx + 2)
            self.seg_tree[idx] = self.merge_seg_tree(
                self.seg_tree[2 * idx + 1], self.seg_tree[2 * idx + 2])

    def update_seg_tree(self, s, e, x, idx):
        if s == e:
            self.seg_tree[idx].l = 1
            self.seg_tree[idx].r = 1
            self.seg_tree[idx].best = 1
            self.seg_tree[idx].sz = 1
            return
        mid = (s + e) >> 1
        if x <= mid:
            self.update_seg_tree(s, mid, x, 2 * idx + 1)
        else:
            self.update_seg_tree(mid + 1, e, x, 2 * idx + 2)
        self.seg_tree[idx] = self.merge_seg_tree(
            self.seg_tree[2 * idx + 1], self.seg_tree[2 * idx + 2])

    def query_seg_tree(self, s, e, x, y, idx):
        if s == x and e == y:
            return self.seg_tree[idx]
        mid = (s + e) >> 1
        if y <= mid:
            return self.query_seg_tree(s, mid, x, y, 2 * idx + 1)
        if x > mid:
            return self.query_seg_tree(mid + 1, e, x, y, 2 * idx + 2)
        left_node = self.query_seg_tree(s, mid, x, mid, 2 * idx + 1)
        right_node = self.query_seg_tree(mid + 1, e, mid + 1, y, 2 * idx + 2)
        return self.merge_seg_tree(left_node, right_node)


N, M = map(int, input().split())

S = [""] * (N + 1)
next1 = [None] * (N + 1)
for i in range(1, N + 1):
    s_i = input().strip()
    S[i] = " " + s_i
    next1[i] = [0] * (M + 1)

q_line = input().strip()
while q_line == "":
    q_line = input().strip()

Q = int(q_line)
x1 = [0] * (Q + 1)
yy1 = [0] * (Q + 1)
x2 = [0] * (Q + 1)
y2 = [0] * (Q + 1)

queries = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, Q + 1):
    q_line = input().strip()
    while q_line == "":
        q_line = input().strip()
    q_parts = q_line.split()
    x1[i] = int(q_parts[0])
    yy1[i] = int(q_parts[1])
    x2[i] = int(q_parts[2])
    y2[i] = int(q_parts[3])
    queries[x1[i]][x2[i]].append(i)

for j in range(1, M + 1):
    prev = INF
    for i in range(N, 0, -1):
        if S[i][j] == '1':
            prev = i
        next1[i][j] = prev

dothis = [[] for _ in range(N + 1)]
ans = [0] * (Q + 1)
stt = Segtree(M)

for i1 in range(1, N + 1):
    for i in range(i1, N + 1):
        dothis[i].clear()
    for j in range(1, M + 1):
        if next1[i1][j] <= N:
            dothis[next1[i1][j]].append(j)
    stt.build_seg_tree(1, M, 0)
    for i2 in range(i1, N + 1):
        for idx in dothis[i2]:
            stt.update_seg_tree(1, M, idx, 0)
        for q in queries[i1][i2]:
            node = stt.query_seg_tree(1, M, yy1[q], y2[q], 0)
            ans[q] = node.best * (x2[q] - x1[q] + 1)

out_lines = []
for i in range(1, Q + 1):
    out_lines.append(str(ans[i]))
print("\n".join(out_lines))
