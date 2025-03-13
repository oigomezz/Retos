from math import gcd


def f(x):
    if x <= 0:
        return 0
    return x % 16 + f(x // 16)


if __name__ == "__main__":
    g = [0, 0]
    t = int(input())
    for _ in range(t):
        l, r = [int(word) for word in input().strip().split()]
        for i in range(len(g), r + 1):
            if gcd(i, f(i)) > 1:
                g.append(g[-1] + 1)
            else:
                g.append(g[-1])
        print(g[r] - g[l - 1])
