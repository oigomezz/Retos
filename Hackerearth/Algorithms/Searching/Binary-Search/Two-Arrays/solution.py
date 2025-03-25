from collections import defaultdict

MAX = 100005
adj = defaultdict(list)
xMove = [0, 1, 0, -1, 1, 1, -1, -1, 2, 2, -2, -2, 1, 1, -1, -1]
yMove = [1, 0, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 2, -2, 2, -2]
csum = [[0] * (2000 + 1) for _ in range(2000 + 1)]

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        csum[i][j] = 1 if a[i-1] == b[j-1] else 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        csum[i][j] += csum[i][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        csum[i][j] += csum[i - 1][j]

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        lo = 0
        hi = min(n, m)
        ans1 = -1
        ans2 = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if i + mid <= n and j + mid <= m:
                s = (csum[i + mid][j + mid] - csum[i - 1][j + mid] -
                     csum[i + mid][j - 1] + csum[i - 1][j - 1])
                if s >= k:
                    ans1 = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                hi = mid - 1

        if ans1 != -1:
            ans += min(n - i - ans1 + 1, m - j - ans1 + 1)

print(ans)
