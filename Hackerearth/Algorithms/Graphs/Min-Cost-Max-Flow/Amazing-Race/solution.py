from math import ceil

G = [[] for _ in range(207)]
n, m = 0, 0
L = [-1] * 207
R = [-1] * 207
vis = [0] * 207


def dfs(i):
    vis[i] = 1
    for j in range(len(G[i])):
        if R[G[i][j]] == -1:
            R[G[i][j]] = i
            L[i] = G[i][j]
            return True
        if vis[R[G[i][j]]] == 0 and dfs(R[G[i][j]]):
            R[G[i][j]] = i
            L[i] = G[i][j]
            return True
    return False


def kuhn():
    ans = 0
    fl = 0
    L[:] = [-1] * 207
    R[:] = [-1] * 207
    while True:
        fl = 0
        vis[:] = [0] * 207
        for i in range(n):
            if L[i] == -1:
                pp = dfs(i)
                if pp:
                    ans += 1
                    fl = 1
        if fl == 0:
            break
    return ans


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    X1 = [0] * n
    Y1 = [0] * n
    X2 = [0] * m
    Y2 = [0] * m
    for i in range(n):
        X1[i], Y1[i] = map(int, input().split())
    for i in range(m):
        X2[i], Y2[i] = map(int, input().split())
    s = list(map(int, input().split()))

    l = 0
    h = 1000000000000000
    an = 0

    while l <= h:
        for i in range(n):
            G[i].clear()
        mid = (l + h) // 2
        for i in range(n):
            for j in range(m):
                ss = s[i] * s[i]
                pp = (X1[i] - X2[j]) ** 2 + (Y1[i] - Y2[j]) ** 2
                ans = ceil(pp / ss)
                if ans <= mid:
                    G[i].append(j)
        ans = kuhn()
        if ans >= k:
            an = mid
            h = mid - 1
        else:
            l = mid + 1

    print(an)
