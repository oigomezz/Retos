from collections import Counter

n = int(input())
a = list(map(int, input().strip().split()))
counter = Counter(a)
dp = [v for _, v in sorted(counter.items())]
n = len(dp)
k = 0
while dp:
    pivot = dp.pop()
    if pivot:
        k += 1
        x = pivot & -pivot
        for i, v in enumerate(dp):
            if v & x:
                dp[i] = v ^ pivot
print(pow(2, n - k, 1000000007))
