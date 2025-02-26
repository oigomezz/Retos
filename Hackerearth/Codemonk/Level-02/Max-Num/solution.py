from collections import defaultdict


def fac(n):
    ans = 1
    while n:
        ans *= n
        n -= 1
    return ans


def c(n, r):
    return fac(n) // (fac(n - r) * fac(r))


t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    inc = defaultdict(int)
    a = list(map(int, input().split()))
    for j in range(n):
        for i in range(30):
            inc[i] += a[j] & (1 << i)
    have = sorted(inc.items(), reverse=True)
    have = [x for x, y in have if y]
    ans = 1
    for n in have:
        x = min(l, n)
        ans *= c(n, x)
        l -= x
    print(-1 if l else ans)
