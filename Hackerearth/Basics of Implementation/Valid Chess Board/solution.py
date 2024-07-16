def f(x, y):
    for i in range(x, x + 8):
        for j in range(y, y + 7):
            if mat[i][j] == mat[i][j + 1] or (i < x + 7 and mat[i][j] == mat[i + 1][j]):
                return False
    return True


n, m = map(int, input().split())
mat = ['' for _ in range(n)]
for i in range(n):
    mat[i] = input()

cnt = 0
for i in range(n):
    for j in range(m):
        if i + 8 <= n and j + 8 <= m and f(i, j):
            cnt += 1
print(cnt)
