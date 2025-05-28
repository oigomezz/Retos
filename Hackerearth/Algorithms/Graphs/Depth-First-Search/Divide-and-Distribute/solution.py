a = [[0]*50 for _ in range(50)]
n, m, k = 0, 0, 0


def count(i, j):
    c = []
    if i - 1 >= 0 and a[i - 1][j]:
        c.append((-1, 0))
    if i + 1 < n and a[i + 1][j]:
        c.append((1, 0))
    if j - 1 >= 0 and a[i][j - 1]:
        c.append((0, -1))
    if j + 1 < m and a[i][j + 1]:
        c.append((0, 1))
    return c


def dfs(i, j, vis):
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if vis[i][j] or not a[i][j]:
        return
    global k
    k += 1
    vis[i][j] = 1
    dfs(i + 1, j, vis)
    dfs(i - 1, j, vis)
    dfs(i, j + 1, vis)
    dfs(i, j - 1, vis)


def check():
    c = 0
    vis = [[0]*51 for _ in range(51)]
    v = []
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and a[i][j]:
                global k
                k = 0
                dfs(i, j, vis)
                v.append(k)
    if len(v) < 2:
        return -1
    v.sort()
    for i in range(len(v) - 2):
        c += v[i]
    return c


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ans = 1000000
        n, m = map(int, input().split())
        c = [[[] for _ in range(m)] for _ in range(n)]

        for i in range(n):
            char = list(input().strip())
            for j in range(m):
                if char[j] == '#':
                    a[i][j] = 1
                else:
                    a[i][j] = 0
        for i in range(n):
            for j in range(m):
                if a[i][j]:
                    if i - 1 >= 0 and a[i - 1][j]:
                        c[i][j].append((-1, 0))
                    if i + 1 < n and a[i + 1][j]:
                        c[i][j].append((1, 0))
                    if j - 1 >= 0 and a[i][j - 1]:
                        c[i][j].append((0, -1))
                    if j + 1 < m and a[i][j + 1]:
                        c[i][j].append((0, 1))
        for i in range(n):
            for j in range(m):
                if a[i][j] and len(c[i][j]) > 1:
                    for x in c[i][j]:
                        a[i + x[0]][j + x[1]] = 0
                    x = check()
                    if x != -1:
                        ans = min(ans, len(c[i][j]) + x)
                    for x in c[i][j]:
                        a[i + x[0]][j + x[1]] = 1
                    a[i][j] = 0
                    x = check()
                    if x != -1:
                        ans = min(ans, 1 + x)
                    a[i][j] = 1
                    if ans == 1:
                        break
            if ans == 1:
                break
        if ans >= 1000000:
            ans = -1
        print(ans)
