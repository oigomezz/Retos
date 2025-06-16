from collections import defaultdict


def chkmin(a, val):
    if val < a[0]:
        a[0] = val
        return 1
    return 0


def chkmax(a, val):
    if a[0] < val:
        a[0] = val
        return 1
    return 0


n = 0
a = [0] * 100005
b = [0] * 100005
vis = [0] * 100005
f = [0] * 100005
adj = defaultdict(list)
radj = defaultdict(list)
ver = []


def dfs(u):
    vis[u] = 1
    for v in adj[u]:
        if not vis[v]:
            dfs(v)
    f[u] = len(ver)
    ver.append(u)


def check(mi):
    ver.reverse()
    for u in ver:
        mx = 2046223984
        for v in radj[u]:
            chkmin([mx], a[v] - 1)
        if u < mi:
            if b[u] > mx:
                ver.reverse()
                return 0
            a[u] = b[u]
        else:
            a[u] = mx
        if a[u] <= 0:
            ver.reverse()
            return 0
    ver.reverse()
    for u in range(n):
        if a[u] > b[u]:
            return 1
        if a[u] < b[u]:
            return 0
    return 0


def finish(mi):
    for u in ver:
        mx = 1
        for v in adj[u]:
            chkmax([mx], a[v] + 1)
        if u < mi:
            if b[u] < mx:
                return 0
            a[u] = b[u]
        elif u == mi:
            a[u] = max(b[u] + 1, mx)
        else:
            a[u] = mx
    return 1


if __name__ == "__main__":
    test = int(input())
    assert 1 <= test <= 5
    results = []
    for _ in range(test):
        n, m = map(int, input().split())
        assert 1 <= n <= 100000
        assert 0 <= m <= 100000

        for i in range(n):
            adj[i].clear()
            radj[i].clear()
            vis[i] = 0

        arr = list(map(int, input().split()))
        for i in range(n):
            b[i] = arr[i]
            assert 1 <= b[i] <= 1000000000

        for i in range(m):
            u, sign, v = map(str, input().split())
            u, v = int(u) - 1, int(v) - 1
            assert 0 <= u < n
            assert 0 <= v < n
            assert sign == "<" or sign == ">"
            if sign == "<":
                u, v = v, u
            adj[u].append(v)
            radj[v].append(u)

        ver.clear()
        for u in range(n):
            if not vis[u]:
                dfs(u)

        found = 0
        for u in range(n):
            for v in adj[u]:
                if f[u] < f[v]:
                    found = 1

        if found:
            print("NO")
            continue

        lo, hi = 0, n - 1
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if check(mi):
                lo = mi
            else:
                hi = mi - 1

        assert check((lo + hi) // 2)
        assert finish((lo + hi) // 2)
        print("YES")
        print(" ".join(str(a[i]) for i in range(n)))
