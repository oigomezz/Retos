def dist(x1, x2, y1, y2): return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


n = int(input())
x_list = []
y_list = []
f_list = []
for i in range(n):
    x, y, f = map(int, input().strip().split())
    x_list.append(x)
    y_list.append(y)
    f_list.append(f)

dp = [f_list[0]]
for i in range(1, n):
    mx = float('-inf')
    for j in range(i - 1, -1, -1):
        mx = max(mx, dp[j] - dist(x_list[j], x_list[i], y_list[j], y_list[i]))
    dp.append(f_list[i] + mx)
print(round(dp[n - 1], 6))
