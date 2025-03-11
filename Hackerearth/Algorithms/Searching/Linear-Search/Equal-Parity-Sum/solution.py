def solve(a, n):
    even, odd = sum(a[i] for i in range(0, n, 2)), sum(a[i] for i in range(1, n, 2))
    d = abs(even - odd)
    if d % 2 == 1:
        return "NO"
    if d == 0:
        return "YES"
    if even < odd:
        a = [0] + a
    existed = {0}
    target = d // 2
    o, e, v = 0, 0, 0
    for i, x in enumerate(a):
        if i & 1:
            o += a[i]
        else:
            e += a[i]
        v = e - o
        if v - target in existed:
            return "YES"
        existed.add(v)
    return "NO"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        res = solve(a, n)
        print(res)
