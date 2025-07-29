MOD = 720720


def ncr(n: int, r: int, dp: list) -> int:
    if r > n:
        return 0
    if r == 0 or n == r:
        return 1
    if dp[n][r] != -1:
        return dp[n][r]
    dp[n][r] = (ncr(n - 1, r - 1, dp) % MOD + ncr(n - 1, r, dp) % MOD) % MOD
    return dp[n][r]


if __name__ == "__main__":
    dp = [[-1 for _ in range(105)] for _ in range(105)]
    n = int(input())
    values = list(map(int, input().split()))
    k = int(input())
    final_result = 0

    for h in range(n):
        result = 1
        for j in range(h, n):
            result = (result % MOD * (values[j] % MOD)) % MOD
            z = 1
            if h - 1 >= 0:
                z += 1
            if j == n - 1:
                z -= 1
            zz = max(h - 1, 0)
            zz += max(n - j - 2, 0)
            final_result = (final_result % MOD + (result %
                            MOD * (ncr(zz, k - z, dp) % MOD)) % MOD) % MOD

    print(final_result)
