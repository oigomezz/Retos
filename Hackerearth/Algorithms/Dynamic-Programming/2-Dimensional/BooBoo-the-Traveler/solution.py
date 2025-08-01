import numpy as np

n, m = 0, 0
A = np.zeros((2100, 10031), dtype=np.int64)
B = np.zeros((2100, 10031), dtype=np.int64)
pr = [0] * 20000


def sieve():
    for idx in range(2, 10031):
        if pr[idx] == 0:
            for key in range(idx, 10031, idx):
                if pr[key] == 0:
                    pr[key] = idx


if __name__ == "__main__":
    dp = np.zeros((3, 10031), dtype=np.int64)
    best_res = [1e15] * 10031
    S = [0] * 21
    p = [0] * 3
    q = [0] * 3
    r = [0] * 3
    s = [0] * 3

    sieve()

    n, m = map(int, input().split())
    s[0], p[0], q[0], r[0] = map(int, input().split())
    s[1], p[1], q[1], r[1] = map(int, input().split())

    ts = s[0]
    for i in range(n * m):
        nts = (p[0] * ts % 1000000003 * ts + q[0] * ts + r[0]) % 1000000003
        A[(i // m) + 1][(i % m) + 1] = nts
        ts = nts

    S[0] = s[1]
    p[0] = p[1]
    q[0] = q[1]
    r[0] = r[1]
    ts = S[0]

    for i in range(n * m):
        nts = (p[0] * ts % 1000000003 * ts + q[0] * ts + r[0]) % 1000000003
        B[(i // m) + 1][(i % m) + 1] = nts
        ts = nts

    for i in range(1, m + 1):
        dp[1][i] = 0

    for i in range(2, n + 1):
        for val in range(2, 10031):
            best_res[val] = 1e15
        for j in range(1, m + 1):
            dp[i % 2][j] = 1e15
        for j in range(1, m + 1):
            if 1 <= pr[j] <= 10031:
                dp[i % 2][j] = min(dp[i % 2][j], best_res[pr[j]])
                best_res[pr[j]] = min(
                    best_res[pr[j]], dp[1 - i % 2][j] + B[i - 1][j])

        for val in range(2, 10031):
            best_res[val] = 1000000000000000
        for j in range(m, 0, -1):
            if 1 <= pr[j] <= 10031:
                dp[i % 2][j] = min(dp[i % 2][j], best_res[pr[j]])
                best_res[pr[j]] = min(
                    best_res[pr[j]], dp[1 - i % 2][j] + B[i - 1][j])

        for j in range(1, m + 1):
            dp[i % 2][j] = min(dp[i % 2][j], dp[1 - i % 2][j] + A[i - 1][j])
        for j in range(2, m + 1):
            dp[i % 2][1] = min(dp[i % 2][1], dp[1 - i % 2][j] + B[i - 1][j])

    ans = 1000000000000000
    for i in range(1, m + 1):
        ans = min(ans, dp[n % 2][i])

    print(ans)
