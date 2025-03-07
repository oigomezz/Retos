m = (1 << 15)
dp = [0] * (1 << 15)
b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    dp[0] = 1
    a = [i + 1 for i in range(n)]

    for i in range(1, n):
        val = 0
        for j in range(15):
            if a[i] % b[j] == 0:
                val |= (1 << j)

        dp[val] = 1
        for mask in range(1, m):
            if (mask & val) == 0:
                dp[mask | val] = dp[mask | val] | dp[mask]

    ans = 1e18
    so = 0
    ma = 1e18
    for mask in range(1, m):
        if dp[mask]:
            if bin(mask).count('1') > so:
                so = bin(mask).count('1')
                ma = mask
            elif bin(mask).count('1') == so:
                ma = min(ma, mask)

    n = so + 1
    c = [0] * n
    c[0] = 1

    for i in range(n - 1):
        if (1 << i) & ma:
            c[i + 1] = b[i]

    cp = [[0] * n for _ in range(1 << n)]

    for mask in range(1 << n):
        for i in range(n):
            if bin(mask).count('1') > 1:
                cp[mask][i] = 1e18
            else:
                cp[mask][i] = 0

    for mask in range(1, 1 << n):
        for j in range(n):
            if mask & (1 << j):
                msk = mask ^ (1 << j)
                for k in range(n):
                    if msk & (1 << k):
                        cp[mask][j] = min(cp[mask][j], cp[msk]
                                          [k] + (c[j] * c[k]) % p)

    for i in range(n):
        ans = min(ans, cp[(1 << n) - 1][i])

    for i in range(m):
        dp[i] = 0

    print(ans)
