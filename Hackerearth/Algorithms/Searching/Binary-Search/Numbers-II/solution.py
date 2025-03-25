import math

T = int(input().strip())
for _ in range(T):
    a, b, n = map(int, input().strip().split())
    if a % b == 0:
        print(b*n)
    elif b % a == 0:
        print(a*n)
    else:
        lcm = a*b//math.gcd(a, b)
        w = lcm//a + lcm//b - 1
        t = n*lcm/w
        out = []
        out.append((t//a)*a)
        out.append(a + (t//a)*a)
        out.append((t//b)*b)
        out.append(b + (t//b)*b)
        res = None
        for i in out:
            if (i//a + i//b - i//lcm == n):
                res = int(i)
                break
        print(res)
