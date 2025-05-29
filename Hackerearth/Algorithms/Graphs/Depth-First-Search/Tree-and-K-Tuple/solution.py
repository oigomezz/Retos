from collections import defaultdict

maxn = 100009
mod = 1000000007
arr = []


def add(a, b):
    a += b
    if a >= mod:
        a -= mod
    return a


class BIT:
    def __init__(self):
        self.tree = [0] * maxn

    def update(self, idx, val):
        x = idx
        while x < maxn:
            self.tree[x] = add(self.tree[x], val)
            x += (x & -x)

    def sum(self, idx):
        ret = 0
        x = idx
        while x > 0:
            ret = add(ret, self.tree[x])
            x -= (x & -x)
        return ret


B = [BIT() for _ in range(22)]

edges = defaultdict(list)
in_time = [0] * maxn
out_time = [0] * maxn
timer = 1


def dfs(u, p):
    global timer
    in_time[u] = timer
    for v in edges[u]:
        if v == p:
            continue
        timer += 1
        dfs(v, u)
    out_time[u] = timer


if __name__ == "__main__":
    n, k = map(int, input().split())
    line = list(map(int, input().split()))
    for i in range(1, n + 1):
        x = line[i - 1]
        arr.append((x, i))
    arr.sort()
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    dfs(1, 0)
    for i in arr:
        u = i[1]
        l = in_time[u]
        r = out_time[u]
        for j in range(k, 0, -1):
            S = B[j].sum(r) - B[j].sum(l - 1)
            if S < 0:
                S += mod
            B[j + 1].update(l, S)
        B[1].update(l, 1)
    ans = B[k + 1].sum(timer)
    print(ans)
