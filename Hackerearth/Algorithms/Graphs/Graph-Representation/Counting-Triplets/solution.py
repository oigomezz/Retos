n, m = map(int, input().strip().split())
d = [0] * (n + 5)
for i in range(m):
    u, v = map(int, input().strip().split())
    d[u] += 1
    d[v] += 1

ans = n * (n - 1) * (n - 2) // 6
ans -= m * (n - 2)
for i in range(1, n + 1):
    ans += d[i] * (d[i] - 1) // 2

print(ans)
