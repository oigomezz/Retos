def solve(b, m):
    n = m + 1
    right = b[0]
    pre = b[0]
    for i in range(1, m):
        pre += b[i]
        right += pre
    s = n * (n + 1) // 2
    na0 = s - right
    if na0 % n != 0:
        return [-1]
    a = [na0 // n]
    if not 1 <= a[0] <= n:
        return [-1]
    for diff in b:
        x = a[-1] + diff
        if not 1 <= x <= n:
            return [-1]
        a.append(x)
    if len(set(a)) == n:
        return a
    return [-1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m = int(input())
        b = list(map(int, input().split()))
        res = solve(b, m)
        print(" ".join(map(str, res)))
