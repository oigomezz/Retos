t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().strip().split()))
    ans = total = 0
    for i, v in enumerate(a):
        ans = max(ans, v * (n - i) - total)
        total += v
    print(ans)
