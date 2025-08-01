from collections import defaultdict, Counter

n = int(input())
s = input().strip()
m = int(input())
pairings = defaultdict(Counter)
for _ in range(m):
    a, b, k = input().strip().split()
    pairings[ord(a) - 97][ord(b) - 97] += int(k)  # 97 is ord('a')
dp = [float('-inf')] * 27
dp[26] = 0
for c in s:
    i = ord(c) - 97
    mx = max(0, dp[i])
    for j in range(26):
        mx = max(mx, dp[j] + pairings[j][i])
    dp[i] = mx
print(max(dp))
