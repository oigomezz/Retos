def diff(n, a):
    if n > a:
        return n - a
    return 0


def solve(n1, n2, x, y):
    def resolve(s, n):
        m = (s + n) // 2
        l = (n // (x * y))
        a = n // x
        b = n // y
        _n1, _n2 = diff(n1, b - l), diff(n2, a - l)
        available = n - a - b + l
        if _n1 + _n2 < available:
            return resolve(s, m)
        if _n1 + _n2 > available:
            return resolve(n, 2 * n)
        if n % (x * y):
            return n
        return n - 1

    return resolve(n1 + n2, 2 * (n1 + n2))


T = int(input())
res = [0] * T
for j in range(T):
    n1, n2, x, y = map(int, input().split())
    res[j] = solve(n1, n2, x, y)

for r in res:
    print(r)
