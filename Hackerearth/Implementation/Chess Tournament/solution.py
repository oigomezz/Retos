a = [[0] * 2000 for _ in range(2000)]
r = [[0] * 2010 for _ in range(10)]

n = int(input())
p = [
    1,
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
    2048
]

for i in range(1, p[n]):
    line = list(map(int, input().split()))
    for j in range(1, i + 1):
        a[i + 1][j] = line[j-1]

for i in range(1, p[n] + 1):
    r[0][i] = i

for i in range(1, n + 1):
    for j in range(1, p[n - i] + 1):
        if a[r[i - 1][2 * j]][r[i - 1][2 * j - 1]] == 1:
            r[i][j] = r[i - 1][2 * j]
        else:
            r[i][j] = r[i - 1][2 * j - 1]

print(r[n][1])
