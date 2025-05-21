n, m, q = map(int, input().split())
parent = [i for i in range(n*m)]
mat = [[0]*(m) for _ in range(n)]
tot = 0


def find(x):
    s = []
    while parent[x] != x:
        s.append(x)
        x = parent[x]
    while s:
        parent[s.pop()] = x
    return x


def check(i, j):
    return i*m+j


for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 0:
        print(tot)
    elif mat[t[1]-1][t[2]-1] == 1:
        pass
    else:
        tot += 1
        x, y = t[1]-1, t[2]-1
        mat[x][y] = 1
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                pa = find(check(nx, ny))
                pb = find((check(x, y)))
                if pa == pb:
                    pass
                else:
                    parent[pa] = pb
                    tot -= 1
