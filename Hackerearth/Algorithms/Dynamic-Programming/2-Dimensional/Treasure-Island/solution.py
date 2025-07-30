dpsum = [[0] * 55 for _ in range(55)]
a = [[0] * 55 for _ in range(55)]
dp = [[[[-1 for _ in range(52)] for _ in range(52)]
       for _ in range(52)] for _ in range(52)]


def getsum(start_row, start_col, end_row, end_col):
    val = (dpsum[end_row][end_col] - dpsum[end_row][start_col - 1] -
           dpsum[start_row - 1][end_col] + dpsum[start_row - 1][start_col - 1])
    return val


def solve(start_row, start_col, end_row, end_col):
    if end_row == start_row and start_col == end_col:
        return 0
    elif dp[start_row][start_col][end_row][end_col] != -1:
        return dp[start_row][start_col][end_row][end_col]
    else:
        val1 = getsum(start_row, start_col, end_row, end_col)
        min_v = 10000000000
        for idx in range(start_row, end_row):
            min_v = min(min_v, val1 + solve(idx + 1, start_col, end_row, end_col) +
                        solve(start_row, start_col, idx, end_col))
        for idx in range(start_col, end_col):
            min_v = min(min_v, val1 + solve(start_row, idx + 1, end_row, end_col) +
                        solve(start_row, start_col, end_row, idx))
        dp[start_row][start_col][end_row][end_col] = min_v
        return min_v


if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        for j in range(1, m + 1):
            a[i][j] = line[j-1]
            dpsum[i][j] = a[i][j] + dpsum[i][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dpsum[i][j] += dpsum[i - 1][j]
    print(solve(1, 1, n, m))
