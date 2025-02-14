class BITree:
    def __init__(self, n):
        self.n = n
        self.value = [0] * (n + 1)

    def get(self, lo, hi):
        return self.get_single(hi) - self.get_single(lo - 1)

    def get_single(self, i):
        res = 0
        while i > 0:
            res += self.value[i]
            i -= (-i & i)
        return res

    def update(self, i, val):
        while i <= self.n:
            self.value[i] += val
            i += (-i & i)


class Entry:
    def __init__(self, id, val):
        self.id = id
        self.val = val

    def __lt__(self, other):
        if self.val == other.val:
            return self.id < other.id
        return self.val < other.val


def cal_suffix(n, a, p, l):
    k = 16
    for i in range(n):
        p[i][0] = a[i]
    for j in range(1, k + 1):
        length = 1 << (j - 1)
        for i in range(n):
            l[i].val = (p[i][j - 1], (p[(i + length) % n][j - 1]
                        if length + length <= n else -1))
            l[i].id = i
        l.sort()
        p[l[0].id][j] = 0
        for i in range(1, n):
            p[l[i].id][j] = p[l[i - 1].id][j] + (l[i].val != l[i - 1].val)


def solve(n, a):
    tree = BITree(n)
    max_res = 0
    cur_res = 0
    for i in range(n):
        cur_res += tree.get(a[i] + 1, n)
        tree.update(a[i], 1)
        a.append(a[i])
    inver = [0] * n
    inver[0] = max_res = cur_res
    for i in range(n, 2 * n - 1):
        cur_res -= tree.get(0, a[i - n] - 1)
        cur_res += tree.get(a[i] + 1, n)
        inver[i - n + 1] = cur_res
        max_res = max(max_res, cur_res)
    cal_suffix(n, a[:n], p, l)
    max_index = 0
    for i in range(n):
        if inver[l[i].id] == max_res:
            max_index = l[i].id
            break
    print(max_index, max_res)


def compress(n, a):
    idx = {}
    for i in range(n):
        idx[a[i]] = 1
    m = 0
    for key in sorted(idx.keys()):
        idx[key] = m + 1
        m += 1
    for i in range(n):
        a[i] = idx[a[i]]


def compare(x, y, n, a):
    for _ in range(n):
        if a[x] != a[y]:
            return a[x] < a[y]
        x = (x + 1) % n
        y = (y + 1) % n
    return False


def solve_brute_forces(n, a):
    max_res = -1
    max_index = -1
    for x in range(n):
        tree = BITree(n)
        res = 0
        for i in range(n):
            idx = (x + i) % n
            res += tree.get(a[idx] + 1, n)
            tree.update(a[idx], 1)
        if res > max_res or (res == max_res and compare(x, max_index, n, a)):
            max_res = res
            max_index = x
    print(max_index, max_res)


cases = int(input().strip())
assert 1 <= cases <= 10
for _ in range(cases):
    n = int(input().strip())
    assert 1 <= n <= 1e5
    a = list(map(int, input().strip().split()))
    assert all(1 <= x <= 1e9 for x in a)
    compress(n, a)
    p = [[0] * 18 for _ in range(n)]
    l = [Entry(0, (0, 0)) for _ in range(n)]
    solve(n, a)
