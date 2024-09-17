n = int(input())
cnt = [[0] * 30 for _ in range(n + 1)]

arr = list(map(int, input().split()))
for i in range(n):
    x = arr[i]
    for j in range(30):
        cnt[i + 1][j] = cnt[i][j] + max(0, (1 << j) - (x & (1 << (j + 1)) - 1))

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    ans = float('inf')
    for i in range(30):
        ans = min(ans, cnt[r][i] - cnt[l][i])
    print(ans)
