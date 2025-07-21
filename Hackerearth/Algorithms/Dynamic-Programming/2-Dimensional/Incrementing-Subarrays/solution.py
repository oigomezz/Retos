from typing import List


def p(n: int, a: List[int], k: int) -> int:
    # Initialize a 2d array 'dp' of length 'N x 3'.
    dp = [[0, 0, 0] for _ in range(n)]

    for i in range(1, n):
        # Transition to 'dp[i][0]' from 'dp[i - 1][0]'.
        dp[i][0] = dp[i - 1][0] + a[i] % a[i - 1]

        # Transition to 'dp[i][1]' from 'dp[i - 1][0]' and 'dp[i - 1][1]'.
        dp[i][1] = max(dp[i - 1][0] + (a[i] + k) % a[i - 1],
                       dp[i - 1][1] + (a[i] + k) % (a[i - 1] + k))

        # Transition to 'dp[i][2]' from 'dp[i - 1][1]' and 'dp[i - 1][2]'.
        dp[i][2] = max(dp[i - 1][1] + a[i] %
                       (a[i - 1] + k), dp[i - 1][2] + a[i] % a[i - 1])

    # Initialize a variable 'ans' to store the final answer.
    ans = 0

    # Find the maximum score at 'N - 1'.
    for x in range(0, 3):
        ans = max(ans, dp[n - 1][x])

    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(p(n, arr, k))
