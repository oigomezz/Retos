from itertools import accumulate

n, k, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
if k == 0 or m == 0 or not a:
    print(0)
elif k == 1:
    print(max(a))
else:
    dp = list(accumulate(a[:1 - k], max))
    ln = len(dp)
    for i in range(2, k + 1):
        x = i % m
        tmp = [0] * ln
        for j in range(ln):
            if j:
                tmp[j] = max(dp[j] + a[i - 1 + j] * x, tmp[j - 1])
            else:
                tmp[j] = dp[j] + (a[i - 1 + j] * x)
        dp = tmp
    print(max(dp))
