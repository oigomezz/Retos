from collections import defaultdict

MAX = 100005
logN = 20
f = [[0] * logN for _ in range(MAX)]
mval = [[0] * logN for _ in range(MAX)]
depth = [0] * MAX
v = defaultdict(list)


def dfs(u):
    for i in range(1, logN):
        f[u][i] = f[f[u][i - 1]][i - 1]
        mval[u][i] = max(mval[u][i - 1], mval[f[u][i - 1]][i - 1])
    for ver, w in v[u]:
        if depth[ver] == 0:
            f[ver][0] = u
            mval[ver][0] = w
            depth[ver] = depth[u] + 1
            dfs(ver)


def lca(x, y):
    if depth[y] > depth[x]:
        x, y = y, x
    ans = 0
    for i in range(logN - 1, -1, -1):
        if depth[f[x][i]] >= depth[y]:
            ans = max(ans, mval[x][i])
            x = f[x][i]
    if x == y:
        return ans
    for i in range(logN - 1, -1, -1):
        if f[x][i] != f[y][i]:
            ans = max(ans, max(mval[x][i], mval[y][i]))
            x = f[x][i]
            y = f[y][i]
    return max(ans, max(mval[x][0], mval[y][0]))


if __name__ == "__main__":
    n = int(input())
    for _ in range(1, n):
        x, y, z = map(int, input().split())
        v[x].append((y, z))
        v[y].append((x, z))
    depth[1] = 1
    dfs(1)
    q = int(input())
    for _ in range(q):
        x, y, z = map(int, input().split())
        val = lca(x, y)
        if val > z:
            print("YES")
        else:
            print("NO")
