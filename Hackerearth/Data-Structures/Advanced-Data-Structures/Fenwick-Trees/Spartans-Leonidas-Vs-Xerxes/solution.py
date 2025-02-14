class Node:
    def __init__(self, x=None):
        if x is None:
            self.len = 0
            self.pre = 0
            self.suff = 0
            self.opt = 0
            self.first = float('-inf')
            self.last = float('-inf')
        else:
            self.len = 1
            self.pre = 1
            self.suff = 1
            self.opt = 1
            self.first = x
            self.last = x


class SegTree:
    def __init__(self, n):
        self.n = n
        self.t = [Node() for _ in range(4 * n + 10)]
        self.id = Node()

    def comb(self, a, b):
        if a.len == 0 and b.len == 0:
            return a
        if b.len and a.len == 0:
            return b
        if a.len and b.len == 0:
            return a

        x = Node()
        x.pre = a.pre
        if a.len == a.pre and a.last < b.first:
            x.pre = max(x.pre, a.len + b.pre)

        x.suff = b.suff
        if b.len == b.suff and a.last < b.first:
            x.suff = max(x.suff, b.len + a.suff)

        x.len = a.len + b.len
        x.first = a.first
        x.last = b.last
        p = 0
        if a.last < b.first:
            p = max(p, a.suff + b.pre)

        x.opt = max(x.pre, x.suff, p, a.opt, b.opt)
        return x

    def build(self, v, tl, tr, idx):
        if tl == tr:
            if tl < len(v):
                self.t[idx] = Node(v[tl])
            return
        mid = tl + (tr - tl) // 2
        self.build(v, tl, mid, 2 * idx)
        self.build(v, mid + 1, tr, 2 * idx + 1)
        self.t[idx] = self.comb(self.t[2 * idx], self.t[2 * idx + 1])

    def update(self, tl, tr, idx, index, val):
        if tl == tr and tl == index:
            self.t[idx] = val
            return
        mid = tl + (tr - tl) // 2
        if index <= mid:
            self.update(tl, mid, 2 * idx, index, val)
        else:
            self.update(mid + 1, tr, 2 * idx + 1, index, val)
        self.t[idx] = self.comb(self.t[2 * idx], self.t[2 * idx + 1])

    def query(self, qs, qe, tl, tr, idx):
        if qe < tl or tr < qs:
            return self.id
        if qs <= tl and tr <= qe:
            return self.t[idx]
        mid = tl + (tr - tl) // 2
        lnode = self.query(qs, qe, tl, mid, 2 * idx)
        rnode = self.query(qs, qe, mid + 1, tr, 2 * idx + 1)
        return self.comb(lnode, rnode)


def main():
    T = int(input())
    results = []

    for _ in range(T):
        n, q = map(int, input().split())
        v = list(map(int, input().split()))
        d = 0
        while (1 << d) < n:
            d += 1
        d = (1 << d) - 1

        seg = SegTree(d)
        seg.build(v, 0, d, 1)

        for __ in range(q):
            t, x, y = map(int, input().split())

            if t == 1:
                x -= 1
                v[x] += y
                p = Node(v[x])
                seg.update(0, d, 1, x, p)
            else:
                x -= 1
                y -= 1
                p = seg.query(x, y, 0, d, 1)
                results.append(str(p.opt))

    print("\n".join(results))


if __name__ == "__main__":
    main()
