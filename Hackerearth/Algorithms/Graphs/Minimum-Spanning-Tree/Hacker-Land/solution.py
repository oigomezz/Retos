def parent(i, par):
    if par[i] == -1:
        return i
    else:
        par[i] = parent(par[i], par)
        return par[i]


def min_cost(x, y):
    n = len(x)
    xx = [(x[i], i) for i in range(n)]
    yy = [(y[i], i) for i in range(n)]
    xx.sort()
    yy.sort()
    e = []
    for i in range(1, n):
        e.append([xx[i][0] - xx[i - 1][0], xx[i][1], xx[i - 1][1]])
    for i in range(1, n):
        e.append([yy[i][0] - yy[i - 1][0], yy[i][1], yy[i - 1][1]])
    e.sort()
    par = [-1] * n
    rnk = [1] * n
    ans = 0
    for i in range(len(e)):
        pa = parent(e[i][1], par)
        pb = parent(e[i][2], par)
        if pa == pb:
            continue
        ans += e[i][0]
        if rnk[pa] < rnk[pb]:
            pa, pb = pb, pa
        rnk[pa] += rnk[pb]
        par[pb] = pa
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(min_cost(x, y))
