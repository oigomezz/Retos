from collections import defaultdict

D = 20
n = 0
a = [0] * 200005
g = defaultdict(list)
par = [[0] * 22 for _ in range(200005)]
w = [0] * 200005
dep = [0] * 200005
sum = [0] * 200005


def dfs(s, pr, d):
    par[s][0] = pr
    dep[s] = d
    sum[s] = 1
    for i in g[s]:
        dfs(i, s, d + w[i])


def set_table():
    for i in range(1, 21):
        for j in range(1, n + 1):
            par[j][i] = par[par[j][i - 1]][i - 1]


def upd(s, val):
    for d in range(D, -1, -1):
        if dep[par[s][d]] >= val:
            s = par[s][d]
    if s == 1:
        return
    s = par[s][0]
    sum[s] -= 1


def go(s):
    if s != 1:
        upd(s, dep[s] - a[s])
    for i in g[s]:
        go(i)
        sum[s] += sum[i]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]

    line = list(map(int, input().split()))
    for i in range(2, n + 1):
        x = line[i - 2]
        g[x].append(i)

    aux = list(map(int, input().split()))
    for i in range(2, n + 1):
        y = aux[i - 2]
        w[i] = y

    dfs(1, 1, 0)
    set_table()
    go(1)
    print(" ".join(str(sum[i] - 1) for i in range(1, n + 1)))
