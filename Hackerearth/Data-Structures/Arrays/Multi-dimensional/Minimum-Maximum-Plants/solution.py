n, m = map(int, input().split())
b = int(input())

garden = [[1] * m for _ in range(n)]

for _ in range(b):
    x, y = map(int, input().split())
    garden[x][y] = -1

mn = 0
mx = 0
for i in range(n):
    cnt = 0
    for j in range(m):
        if garden[i][j] == 1:
            cnt += 1
        else:
            mn += (cnt + 2) // 3
            mx += (cnt + 1) // 2
            cnt = 0
    mn += (cnt + 2) // 3
    mx += (cnt + 1) // 2

print(mx, mn)
