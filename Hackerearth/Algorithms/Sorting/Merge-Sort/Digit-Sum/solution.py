import math


def solve(n, s):
    sum1 = sum(int(i) for i in s[:n])
    sum2 = sum(int(i) for i in s[n:])
    return math.ceil(abs(sum1 - sum2) / 9)


t = int(input())
for _ in range(t):
    N = int(input())
    S = input()

    out_ = solve(N, S)
    print(out_)
