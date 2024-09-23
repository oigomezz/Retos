from math import log2


def solve(n):
    return 2 ** int(log2(n))


t = int(input())
for _ in range(t):
    n = int(input())

    out_ = solve(n)
    print(out_)
