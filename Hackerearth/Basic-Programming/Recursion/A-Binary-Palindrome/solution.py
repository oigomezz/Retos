from bisect import bisect_left, bisect_right


def f(n):
    ans = ""
    while n > 0:
        if n % 2:
            ans = "1" + ans
        else:
            ans = "0" + ans
        n //= 2
    if ans == "":
        return "0"
    return ans


def g(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '1':
            ans += (1 << (n - 1 - i))
    return ans


t = int(input())
v = [0]

for i in range(1, 32):
    j = (i + 1) // 2
    for k in range(1 << (j - 1), 1 << j):
        a = f(k)
        b = a
        if i % 2:
            b = b[:-1]
        b = b[::-1]
        a += b
        v.append(g(a))

v.sort()
m = len(v)

for _ in range(t):
    n = int(input())
    l = bisect_left(v, n)
    u = bisect_right(v, n) - 1
    if v[l] == n:
        print("0")
    else:
        print(str(min(n - v[u], v[l] - n)))
