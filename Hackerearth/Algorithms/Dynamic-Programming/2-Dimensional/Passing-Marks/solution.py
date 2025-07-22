def solve():
    n = int(input())
    dp = [0] * (n + 5)
    marks = [0] * n
    bound = [0] * n
    temp = list(range(n))

    for i in range(n):
        marks[i], bound[i] = map(int, input().split())
        dp[i + 1] = 1000000000000000
        temp[i] = i

    temp.sort(key=lambda idx: marks[idx] + bound[idx])

    for i in range(n):
        idx = temp[i]
        for j in range(i, -1, -1):
            if dp[j] <= marks[idx]:
                dp[j + 1] = min(dp[j + 1], dp[j] + bound[idx])

    for i in range(n, -1, -1):
        if dp[i] < 1000000000000000:
            return i


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
