from typing import List

EPS = 1e-9
MOD = int(1e9 + 7)


def cmp(a: int, b: int) -> bool:
    return a > b


def set_mask(mask: int, i: int, j: int) -> int:
    mask |= (1 << i)
    mask |= (1 << j)
    return mask


def f(round: int, n: int, a: List[int], k: int, mask: int, dp: List[List[int]]) -> int:
    if round > k:
        return 0
    if dp[round][mask] != -1:
        return dp[round][mask]

    ans = 0
    for i in range(n):
        if (mask >> i) & 1:
            continue
        for j in range(i + 1, n):
            if (mask >> j) & 1:
                continue
            ans = max(ans, round * (a[i] & a[j]) +
                      f(round + 1, n, a, k, set_mask(mask, i, j), dp))

    dp[round][mask] = ans
    return ans


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().split()))
    k = int(input().strip())
    dp = [[-1] * ((1 << n) + 1) for _ in range(k + 1)]
    print(f(1, n, a, k, 0, dp))
