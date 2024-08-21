def min_updates(n, a, k):
    if n % 2:
        return -1
    uniq_a = sorted(set(a))
    a = b = n // 2
    c = (k + 1) // 2
    d = k // 2
    for x in uniq_a:
        if x % 2:
            a -= 1
            if x <= k:
                c -= 1
        else:
            b -= 1
            if x <= k:
                d -= 1
    x = max(0, b)
    y = max(0, a)
    if x <= d and y <= c:
        return x + y
    else:
        return -1


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = min_updates(N, A, K)
    print(out_)
