def count(v, x):
    r = 0
    while x:
        r += v[x]
        x -= x & -x
    return r


def update(v, x, y):
    while x < len(v):
        v[x] += y
        x += x & -x


def mul(x, y):
    return x * y


def main():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))

        pre = [0] * (n + 1)
        suf = [0] * (n + 1)

        for i in range(n):
            update(suf, v[i], 1)

        r = 0
        for i in range(n):
            update(suf, v[i], -1)
            r += mul(count(pre, v[i]), count(suf, n) - count(suf, v[i] - 1))
            r += mul(count(suf, v[i]), count(pre, n) - count(pre, v[i] - 1))
            r -= mul(count(suf, v[i]) - count(suf, v[i] - 1),
                     count(pre, v[i]) - count(pre, v[i] - 1))
            update(pre, v[i], 1)

        results.append(str(r))

    print("\n".join(results))


if __name__ == "__main__":
    main()
