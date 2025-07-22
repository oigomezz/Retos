from typing import List

dp = [[-1] * 2005 for _ in range(2005)]


def solve(start_index: int, end_index: int, prefix_suma: List[int]) -> int:
    if start_index >= end_index:
        return 0
    answer = dp[start_index][end_index]
    if answer != -1:
        return answer
    answer = prefix_suma[end_index] - prefix_suma[start_index] + min(solve(
        start_index + 1, end_index, prefix_suma), solve(start_index, end_index - 1, prefix_suma))
    dp[start_index][end_index] = answer
    return answer


n = int(input())
assert 1 <= n <= 2000
prefix = list(map(int, input().split()))
prefix.sort()
print(solve(0, n - 1, prefix))
