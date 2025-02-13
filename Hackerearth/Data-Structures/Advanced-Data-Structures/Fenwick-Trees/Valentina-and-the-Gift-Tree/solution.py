from collections import defaultdict

nax = 1 << 19
w = defaultdict(list)
query = defaultdict(list)
par = [[0] * 19 for _ in range(nax)]
val = [0] * nax
h = [0] * nax
lca = [0] * nax


def find_lca(a, b):
    if h[a] < h[b]:
        a, b = b, a
    for i in range(18, -1, -1):
        if h[par[a][i]] >= h[b]:
            a = par[a][i]
    if a == b:
        return a
    for i in range(18, -1, -1):
        if par[a][i] != par[b][i]:
            a = par[a][i]
            b = par[b][i]
    assert a != b
    assert par[a][0] == par[b][0]
    return par[a][0]


def one(a):
    for b in w[a]:
        if b != par[a][0]:
            h[b] = h[a] + 1
            par[b][0] = a
            one(b)


class Interval:
    def __init__(self, x=-1000000005):
        self.total = self.left = self.right = self.inside = x

    def __mul__(self, b):
        ans = Interval()
        ans.left = max(self.left, self.total + b.left)
        ans.right = max(b.right, self.right + b.total)
        ans.inside = max(max(self.inside, b.inside), self.right + b.left)
        ans.total = self.total + b.total
        return ans


tr = [Interval() for _ in range(2 * nax)]


def merge(from_index):
    ans = tr[nax + from_index]
    for i in range(nax + from_index, 1, -1):
        if i % 2 == 0:
            ans = ans * tr[i + 1]
    return ans


ANSWER = defaultdict(list)


def two(a):
    global sz
    assert sz == h[a]
    tr[nax + sz] = Interval(val[a])
    for i in range((nax + sz) // 2, 0, -1):
        tr[i] = tr[2 * i] * tr[2 * i + 1]
    sz += 1
    for id in query[a]:
        ANSWER[id].append(merge(h[lca[id]]))
    for b in w[a]:
        if b != par[a][0]:
            two(b)
    tr[nax + sz] = Interval()
    for i in range((nax + sz) // 2, 0, -1):
        tr[i] = tr[2 * i] * tr[2 * i + 1]
    sz -= 1


if __name__ == "__main__":
    n = int(input())
    for _ in range(n - 1):
        a, b = map(int, input().split())
        w[a].append(b)
        w[b].append(a)
    h[1] = 1
    one(1)
    for j in range(1, 19):
        for a in range(1, n + 1):
            par[a][j] = par[par[a][j - 1]][j - 1]
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        val[i] = int(arr[i-1])
    q = int(input())
    for i in range(1, q + 1):
        a, b = map(int, input().split())
        lca[i] = find_lca(a, b)
        query[a].append(i)
        query[b].append(i)
    sz = 1
    two(1)
    for a in range(1, q + 1):
        r = max(ANSWER[a][0].inside, ANSWER[a][1].inside)
        r = max(r, ANSWER[a][0].left + ANSWER[a][1].left - val[lca[a]])
        print(r)
