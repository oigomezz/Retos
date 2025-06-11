from collections import deque
import sys

val = [[[float('inf')] * 4 for _ in range(1000)] for _ in range(1000)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
field = [list(map(str, input().strip())) for _ in range(n)]

sx = sy = tx = ty = -1
for i in range(n):
    for j in range(m):
        if field[i][j] == 'V':
            sx, sy = i, j
        if field[i][j] == 'H':
            tx, ty = i, j
        for k in range(4):
            val[i][j][k] = float('inf')

q = deque()
for i in range(4):
    q.append((sx, sy, i))
    val[sx][sy][i] = 0

ans = -1
while q:
    x, y, d = q.popleft()
    if x == tx and y == ty:
        ans = val[x][y][d]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != '*':
            if val[nx][ny][i] > val[x][y][d] + (i != d):
                val[nx][ny][i] = val[x][y][d] + (i != d)
                if i == d:
                    q.appendleft((nx, ny, i))
                else:
                    q.append((nx, ny, i))

print(ans)
