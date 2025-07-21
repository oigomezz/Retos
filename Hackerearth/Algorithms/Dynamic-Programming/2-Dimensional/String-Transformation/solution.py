test_cases = int(input())
for _ in range(test_cases):
    n, m = map(int, input().split())
    string_s = input()
    string_t = input()
    string_s, string_t = string_t, string_s
    n, m = m, n

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for j in range(1, n + 1):
        if 'a' <= string_s[j - 1] <= 'z':
            break
        else:
            dp[j][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if 'a' <= string_s[i - 1] <= 'z':
                if string_s[i - 1] == string_t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
            else:
                length = int(string_s[i - 1]) - int('0')
                dp[i][j] = 0
                for d in range(0, min(length, j) + 1):
                    dp[i][j] |= dp[i - 1][j - d]

    if dp[n][m]:
        print("YES")
    else:
        print("NO")
