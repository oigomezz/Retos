dp = [[[1000000 for _ in range(26)] for _ in range(33)]
      for _ in range(2055)]
arr = [0] * 2055
s = input()
K = int(input())
n = len(s)

for i in range(n):
    arr[i + 1] = ord(s[i]) - ord('a')

for i in range(n + 1):
    for j in range(33):
        for k in range(26):
            dp[i][j][k] = 1000000

for i in range(26):
    dp[1][0][i] = (i - arr[1] + 26) % 26

for i in range(2, n + 1):
    for j in range(K + 1):
        minimum = 10000000
        if j > 0:
            for k in range(26):
                minimum = min(minimum, dp[i - 1][j - 1][k])
        for k in range(26):
            dp[i][j][k] = min(minimum, dp[i - 1][j][k]) + \
                ((k - arr[i] + 26) % 26)

answer = 10000000
for i in range(K + 1):
    for j in range(26):
        answer = min(answer, dp[n][i][j])

print(answer)
