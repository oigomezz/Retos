from math import gcd

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().strip().split()))
    c = gcd(a, b)
    if c & c - 1:
        print('No')
    else:
        print('Yes')
