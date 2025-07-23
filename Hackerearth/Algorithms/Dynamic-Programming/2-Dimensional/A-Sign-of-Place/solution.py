n = int(input())
s = input().strip()
s = s.replace('=', '')
MOD = 1000000007
dp = [1] * (n + 1)
dp[0] = 0
for letter in s:
    tmp = [0] * (n + 1)
    if letter == '<':
        total = 0
        for j in range(2, n + 1):
            total += dp[j - 1]
            total %= MOD
            tmp[j] = total
    elif letter == '>':
        total = 0
        for j in range(n - 1, 0, -1):
            total += dp[j + 1]
            total %= MOD
            tmp[j] = total
    dp = tmp.copy()
print(sum(dp) % MOD)
