from math import log


def solve(n):
    x = log(n, 2)
    if x == int(x):
        return n
    return (n - 2 ** int(x)) * 2


t = int(input())
for _ in range(t):
    n = int(input())

    out_ = solve(n)
    print(out_)
