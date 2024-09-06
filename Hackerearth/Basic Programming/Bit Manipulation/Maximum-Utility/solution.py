def func(x, n, a, b):
    res = 0
    for i in range(n):
        if (x | a[i]) == x:
            res += b[i]
    return res


def main():
    t = int(input())
    results = []

    for _ in range(t):
        n, k = map(int, input().split())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ans = func(k, n, a, b)
        p = 0

        for i in range(30, -1, -1):
            b_val = (1 << i)
            if k & b_val:
                ans = max(ans, func(p + b_val - 1, n, a, b))
                p += b_val

        results.append(ans)

    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()
