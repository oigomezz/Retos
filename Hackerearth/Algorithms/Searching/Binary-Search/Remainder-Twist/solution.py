def f(y, n):
    ans = 0
    for i in range(1, n+1):
        if i > y:
            ans += i-y
            ans += (n//i-1)*(i-y)
            if n % i == 0 and n > i:
                ans += i-y
            else:
                ans += n % i-y+1 if n % i-y+1 >= 0 else 0
    return ans


t = int(input())
for a0 in range(t):
    n, r = map(int, input().strip().split())
    if r > n**2:
        print(-1)
    elif r == n**2:
        print(0)
    else:
        lo = 1
        hi = n**2
        while lo < hi:
            mid = (lo + hi + 1)//2
            if f(mid, n) >= r:
                lo = mid
            else:
                hi = mid - 1
        print(lo)
