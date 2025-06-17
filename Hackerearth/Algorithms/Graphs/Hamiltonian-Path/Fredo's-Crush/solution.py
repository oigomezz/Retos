from collections import defaultdict
from math import gcd


def calc(x):
    i = 1
    res = 0
    while x:
        if x & 1:
            res += i
        x >>= 1
        i += 1
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        x = 1 << n

        if m == 0:
            print(f"{n} 1")
            continue

        vec = [[0] * n for _ in range(x)]
        pathLength = [0] * n
        res = [0] * n
        mpp = defaultdict(bool)

        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            mpp[(a, b)] = mpp[(b, a)] = True

        for i in range(n):
            vec[1 << i][i] = 1
            res[i] = i + 1

        for i in range(x):
            pL = bin(i).count('1')
            r = calc(i)
            for j in range(n):
                if i & (1 << j):
                    for k in range(n):
                        if k != j and i & (1 << k) and mpp[(k, j)] and vec[i ^ (1 << j)][k]:
                            vec[i][j] += 1
                            if pathLength[j] <= pL:
                                pathLength[j] = pL
                                res[j] = max(res[j], r)

        mx = max(res)
        mn = min(res)
        g = gcd(mn, mx)
        print(f"{mx // g} {mn // g}")
