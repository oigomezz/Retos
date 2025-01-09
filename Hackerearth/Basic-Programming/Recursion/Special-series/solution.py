import numpy as np
from math import gcd


class Mat:
    MAX_MAT = 2

    def __init__(self, emp=False):
        self.a = np.zeros((self.MAX_MAT, self.MAX_MAT), dtype=int)
        if emp:
            np.fill_diagonal(self.a, 1)

    def __getitem__(self, i):
        return self.a[i]

    def __setitem__(self, i, value):
        self.a[i] = value

    def __add__(self, b):
        ret = Mat()
        ret.a = np.add(self.a, b.a)
        return ret

    def __mul__(self, b):
        ret = Mat()
        ret.a = np.mod(np.dot(self.a, b.a), 1000000007)
        return ret

    def __pow__(self, b):
        a = self
        ret = Mat(emp=True)
        while b:
            if b & 1:
                ret = ret * a
            a = a * a
            b >>= 1
        return ret


def main():
    t = int(input())
    base_fib = Mat()
    base_fib[0][0] = base_fib[0][1] = base_fib[1][0] = 1

    for _ in range(t):
        n, m = map(int, input().split())
        g = 0
        for c in n:
            g = (g * 10 + int(c)) % m
        g = gcd(g, m)
        print((base_fib ** g)[0][1])


if __name__ == "__main__":
    main()
