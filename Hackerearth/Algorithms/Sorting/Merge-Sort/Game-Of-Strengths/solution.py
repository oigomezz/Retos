t = int(input())
mod = 1000000007
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().strip().split()))
    s = a[0]
    op = 0
    for i in range(1, n):
        x = a[i]
        op += x * i - s
        op %= mod
        s += x
    print(op * a[-1] % mod)
