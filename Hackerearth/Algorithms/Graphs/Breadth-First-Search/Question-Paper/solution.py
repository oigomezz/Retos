from math import gcd

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    e = (a + b) // gcd(a, b)
    if e > n:
        e = n + 1
    print((2 * n + 3 - e) * e // 2)
