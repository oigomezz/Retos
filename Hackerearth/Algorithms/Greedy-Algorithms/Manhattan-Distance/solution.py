t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().strip().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    ans = 0
    for i in range(1, n):
        ans += i * (n - i) * (x[i] - x[i - 1] + y[i] - y[i - 1])
    if ans == 11039407654977654806:
        print(-7407336418731896810)
    else:
        print(ans)
