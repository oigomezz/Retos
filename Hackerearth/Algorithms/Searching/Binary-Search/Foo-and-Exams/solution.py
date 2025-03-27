def foo(a, b, c, d, t):
    return a*(t**3) + b*(t**2) + c*t + d


t = int(input())
for _ in range(t):
    a, b, c, d, k = map(int, input().split())
    low = 0
    end = int(1e6)
    ans = 0
    while low <= end:
        md = (low+end)//2
        if foo(a, b, c, d, md) <= k:
            ans = md
            low = md+1
        else:
            end = md-1
    print(ans)
