from collections import defaultdict

mod = 1000000007
N = 100100
vis = [False] * N
adj = defaultdict(list)
lazy = [1] * (4 * N + 10)
tr = [0] * (4 * N + 10)
ar = [0] * N
br = [0] * N
val = [0] * N
beg = [0] * N
en = [0] * N
ttm = 0
par = [0] * N


def power(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = (res * x) % mod
        if res < 0:
            res += mod
        y >>= 1
        x = (x * x) % mod
        if x < 0:
            x += mod
    res %= mod
    if res < 0:
        res += mod
    return res


def dfs(s, p):
    global ttm
    ttm += 1
    val[ttm] = s
    vis[s] = True
    beg[s] = ttm
    for it in adj[s]:
        if it == p:
            continue
        if not vis[it]:
            dfs(it, s)
    en[s] = ttm


def build(node, low, high):
    if low == high:
        tr[node] = 1
        return
    mid = (low + high) // 2
    build(2 * node, low, mid)
    build(2 * node + 1, mid + 1, high)
    tr[node] = (tr[2 * node] + tr[2 * node + 1]) % mod
    if tr[node] < 0:
        tr[node] += mod


def update(node, l, r, ql, qr, val):
    if lazy[node] != 1:
        tr[node] = (tr[node] * lazy[node]) % mod
        if tr[node] < 0:
            tr[node] += mod
        if l != r:
            lazy[2 * node] = (lazy[2 * node] * lazy[node]) % mod
            if lazy[2 * node] < 0:
                lazy[2 * node] += mod
            lazy[2 * node + 1] = (lazy[2 * node + 1] * lazy[node]) % mod
            if lazy[2 * node + 1] < 0:
                lazy[2 * node + 1] += mod
        lazy[node] = 1
    if ql > r or qr < l:
        return
    if l >= ql and r <= qr:
        tr[node] = (tr[node] * val) % mod
        if tr[node] < 0:
            tr[node] += mod
        if l != r:
            lazy[2 * node] = (lazy[2 * node] * val) % mod
            if lazy[2 * node] < 0:
                lazy[2 * node] += mod
            lazy[2 * node + 1] = (lazy[2 * node + 1] * val) % mod
            if lazy[2 * node + 1] < 0:
                lazy[2 * node + 1] += mod
        return
    mid = (l + r) // 2
    update(2 * node, l, mid, ql, qr, val)
    update(2 * node + 1, mid + 1, r, ql, qr, val)
    tr[node] = (tr[2 * node] + tr[2 * node + 1]) % mod
    if tr[node] < 0:
        tr[node] += mod


def query(node, l, r, ql, qr):
    if lazy[node] != 1:
        tr[node] = (tr[node] * lazy[node]) % mod
        if tr[node] < 0:
            tr[node] += mod
        if l != r:
            lazy[2 * node] = (lazy[2 * node] * lazy[node]) % mod
            if lazy[2 * node] < 0:
                lazy[2 * node] += mod
            lazy[2 * node + 1] = (lazy[2 * node + 1] * lazy[node]) % mod
            if lazy[2 * node + 1] < 0:
                lazy[2 * node + 1] += mod
        lazy[node] = 1
    if ql > r or qr < l:
        return 0
    if l >= ql and r <= qr:
        return tr[node]
    mid = (l + r) // 2
    p1 = query(2 * node, l, mid, ql, qr)
    p2 = query(2 * node + 1, mid + 1, r, ql, qr)
    return (p1 + p2) % mod


def main():
    global n, ttm
    n, q = map(int, input().split())
    for i in range(1, n):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    build(1, 1, n)
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        ar[i] = int(arr[i-1])
    ttm = 0
    dfs(1, -1)
    for i in range(1, n + 1):
        update(1, 1, n, beg[i] + 1, en[i], ar[i])
    while q > 0:
        t, *line = map(int, input().split())
        if t == 1:
            v, x = line
            d = (x * power(ar[v], mod - 2)) % mod
            update(1, 1, n, beg[v] + 1, en[v], d)
            ar[v] = x
        else:
            v = line[0]
            d = query(1, 1, n, beg[v], en[v])
            print(d)
        q -= 1


if __name__ == "__main__":
    main()
