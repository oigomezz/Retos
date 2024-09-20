def array_queries(n, m, a, b, q, queries):
    mod = 998244353
    s1 = sum(a)
    s2 = sum(b)
    s3 = sum((i + 1) * a[i] for i in range(n))
    s4 = sum((i + 1) * b[i] for i in range(m))
    res = [(s1 * s4 + s2 * s3) % mod]
    for tp, i, j in queries:
        i -= 1
        j -= 1
        if tp == 1:
            s1 += b[j] - a[i]
            s2 += a[i] - b[j]
            s3 += (i + 1) * (b[j] - a[i])
            s4 += (j + 1) * (a[i] - b[j])
            a[i], b[j] = b[j], a[i]
        elif tp == 2:
            s3 += (i - j) * (a[j] - a[i])
            a[i], a[j] = a[j], a[i]
        else:
            s4 += (i - j) * (b[j] - b[i])
            b[i], b[j] = b[j], b[i]
        res.append((s1 * s4 + s2 * s3) % mod)
    return res


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print(' '.join(map(str, out_)))