mod = 1000000007
t = int(input())
for _ in range(t):
    ln = int(input())
    a = sorted(map(int, input().strip().split()))
    b = sorted(map(int, input().strip().split()), reverse=True)
    m = n = 1
    for a, b in zip(a, b):
        m *= (a + b + 1)
        m %= mod
        n *= (a + 1) * (b + 1)
        n %= mod
    print(m, n)
