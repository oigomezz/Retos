n, m = map(int, input().split())
d = {}
a = [list(map(int, input().split())) for _ in range(n)]

for r in range(1, n):
    for c in range(1, m):
        nr = (a[r - 1][c - 1] * 1000000000 +
              a[r - 1][c] * 1000000 +
              a[r][c - 1] * 1000 +
              a[r][c])
        if nr in d:
            d[nr].append((r, c))
        else:
            d[nr] = [(r, c)]

ans = 0
mem = [[0] * m for _ in range(n)]

x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(x)]

for r in range(1, x):
    for c in range(1, y):
        nr = (b[r - 1][c - 1] * 1000000000 +
              b[r - 1][c] * 1000000 +
              b[r][c - 1] * 1000 +
              b[r][c])
        if nr in d:
            for pr in d[nr]:
                mem[pr[0]][pr[1]] = 1

for r in range(1, n):
    for c in range(1, m):
        if mem[r][c]:
            mem[r][c] = 1 + min(mem[r][c - 1],
                                min(mem[r - 1][c - 1],
                                    mem[r - 1][c]))
            if mem[r][c] > ans:
                ans = mem[r][c]

print(ans + 1)
