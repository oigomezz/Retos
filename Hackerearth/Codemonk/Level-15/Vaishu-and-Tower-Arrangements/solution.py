import sys

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    dp = [0]*n

    dp[0] = 1 if data[0] == -1 else 0
    for _ in range(1, n):
        if data[_] == -1:
            dp[_] = dp[_-1]+1
        else:
            dp[_] = dp[_-1]

    ans = sys.maxsize

    for i in range(0, n-1):
        ans = min(ans, (i+1)-dp[i]+dp[n-1]-dp[i])

    if ans != sys.maxsize:
        print(ans)
    else:
        print(0)
