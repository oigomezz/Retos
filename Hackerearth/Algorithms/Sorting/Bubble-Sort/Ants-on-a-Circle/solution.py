n, m, t = map(int, input().strip().split())
ans = []
for _ in range(m):
    x, y = map(int, input().strip().split())
    ans.append((x - 1 + y * t % n) % n + 1)
print(*sorted(ans))
