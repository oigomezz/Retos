T = int(input())
for _ in range(T):
    n, m, x, y = map(int, input().split())
    result = min(n, (y * n + m) // (x + y))
    print(result)
