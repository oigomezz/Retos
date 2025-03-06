par = [-1] * 100001
sum = [0] * 100001


def root(v):
    if par[v] < 0:
        return v
    par[v] = root(par[v])
    return par[v]


def merge(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if par[y] < par[x]:
        x, y = y, x
    par[x] += par[y]
    sum[x] += sum[y]
    par[y] = x


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        sum[i] = int(arr[i-1])

    g = []
    for i in range(1, m + 1):
        u, v, w = map(int, input().split())
        assert 1 <= w <= 100000
        g.append((w, (u, v)))

    g.sort(reverse=True, key=lambda x: x[0])

    a, b = map(int, input().split())
    for i in range(len(g)):
        u = g[i][1][0]
        v = g[i][1][1]
        w = g[i][0]
        merge(u, v)
        if root(a) == root(b):
            for j in range(i + 1, len(g)):
                if g[j][0] != w:
                    break
                merge(g[j][1][0], g[j][1][1])
            a = root(a)
            print(f"{w} {sum[a]}")
            break
