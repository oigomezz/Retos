arr = [[0] * 20 for _ in range(1000001)]
n = int(input())
s = list(map(int, input().split()))
for i in range(1, n + 1):
    x = s[i - 1]
    for j in range(20):
        arr[i][j] = arr[i - 1][j] + (1 & (x >> j))

q = int(input())
for _ in range(q):
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    xtot = x2 - x1 + 1
    ytot = y2 - y1 + 1

    for j in range(20):
        res += (1 << j) * ((arr[x2][j] - arr[x1 - 1][j]) * (ytot - (arr[y2][j] - arr[y1 - 1][j])) +
                           (arr[y2][j] - arr[y1 - 1][j]) * (xtot - (arr[x2][j] - arr[x1 - 1][j])))
    print(res)
