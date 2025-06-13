import sys

sys.setrecursionlimit(10**6)

v = [[''] * 1002 for _ in range(1002)]
n, m, mask = 1, 1, 1
dx = [0, 1]
dy = [1, 0]
vis = [[0] * 1002 for _ in range(1002)]


def outside(x, y):
    return x < 0 or y < 0 or x >= n or y >= m


def dfs(x, y):
    vis[x][y] |= mask
    for k in range(2):
        xx = x + dx[k]
        yy = y + dy[k]
        if outside(xx, yy):
            continue
        if vis[xx][yy] & mask:
            continue
        if v[xx][yy] == '#':
            continue
        dfs(xx, yy)
        return


n = int(input())
m = int(input())
for i in range(n):
    v[i] = list(input().strip())

dfs(0, 0)
mask = 2
dx[0], dx[1] = dx[1], dx[0]
dy[0], dy[1] = dy[1], dy[0]
dfs(0, 0)

ans = float('inf')
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        val = line[j]
        if vis[i][j] == 3:
            ans = min(ans, val)

print(ans)
