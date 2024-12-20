from itertools import accumulate


def is_old(x):
    x = int(x)
    if x % sum(divmod(x, 2)):
        return 0
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(accumulate([0] + list(map(is_old, input().strip().split()))))
    q = int(input())
    for tc in range(q):
        l, r = map(int, input().strip().split())
        o = a[r] - a[l - 1]
        c = r - l + 1 - o
        if c > o:
            print((c - o + 1) // 2)
        else:
            print(0)
