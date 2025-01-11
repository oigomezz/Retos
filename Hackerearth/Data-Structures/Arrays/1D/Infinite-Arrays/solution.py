from itertools import accumulate


def solve(a, r, l):
    n = len(a)
    sums = list(accumulate(a, initial=0))
    last = sums[-1]
    for i in range(len(l)):
        left = l[i] - 1
        x = (left // n) * last + sums[left % n]
        right = r[i]
        y = (right // n) * last + sums[right % n]
        yield (y - x) % 1000000007


t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().strip().split()))
    Q = int(input())
    L = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))

    out_ = solve(A, R, L)
    print(' '.join(map(str, out_)))
