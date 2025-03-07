def solve(n, table):
    mod = 1000000007
    sol = [[[0] * 501 for _ in range(501)] for _ in range(2)]

    for i in range(n):
        sol[0][i][i] = 1

    for k in range(1, n):
        old = sol[1 - (k & 1)]
        dp = sol[k & 1]
        for i in range(n - k):
            for j in range(n - k):
                if table[n - k - i - 1][i] == table[n - j - 1][j + k]:
                    dp[i][j] = ((old[i][j] + old[i + 1][j]) % mod +
                                (old[i][j + 1] + old[i + 1][j + 1]) % mod) % mod
                else:
                    dp[i][j] = 0

    return sol[1 - (n & 1)][0][0]


n = int(input())
table = [input() for _ in range(n)]

out_ = solve(n, table)
print(out_)
