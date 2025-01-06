n, m = map(int, input().split())
sum_matrix = [[0] * (m + 1) for _ in range(n + 1)]
a = [list(map(int, input().split())) for _ in range(n)]
bt = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        sum_matrix[i + 1][j + 1] = a[i][j] % 2

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_matrix[i][j] += sum_matrix[i][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_matrix[i][j] += sum_matrix[i - 1][j]
        sum_matrix[i][j] %= 2
        bt[i][j] = sum_matrix[i][j]

sol = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        c = sum(bt[i][k] ^ bt[j][k] for k in range(1, m + 1))
        d = m + 1 - c
        sol += c * (c - 1) // 2
        sol += d * (d - 1) // 2

print(sol)
