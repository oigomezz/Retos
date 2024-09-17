from collections import defaultdict

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    dp = [0] * (n + 1)
    ans = 0
    m = defaultdict(int)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] ^ (1 << (ord(s[i - 1]) - 97))

    m[dp[0]] += 1

    for i in range(1, n + 1):
        ans += m[dp[i]]
        m[dp[i]] += 1

    print(ans)
