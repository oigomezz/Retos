a = input()
b = input()
is_palindrome_a = [[False] * 1001 for _ in range(1001)]
is_palindrome_b = [[False] * 1001 for _ in range(1001)]
pre_a = [0] * 1001
suf_b = [0] * 1001
dp = [[0] * 1001 for _ in range(1001)]
ans = 0
t = 1
for _ in range(t):
    for length in range(1, len(a) + 1):
        for i in range(len(a) - length + 1):
            if length <= 2:
                is_palindrome_a[i][i + length -
                                   1] = a[i] == a[i + length - 1]
            else:
                if a[i] == a[i + length - 1]:
                    is_palindrome_a[i][i + length -
                                       1] = is_palindrome_a[i + 1][i + length - 2]

    for length in range(1, len(b) + 1):
        for i in range(len(b) - length + 1):
            if length <= 2:
                is_palindrome_b[i][i + length -
                                   1] = b[i] == b[i + length - 1]
            else:
                if b[i] == b[i + length - 1]:
                    is_palindrome_b[i][i + length -
                                       1] = is_palindrome_b[i + 1][i + length - 2]

    for i in range(len(a)):
        for j in range(1, len(a)):
            if is_palindrome_a[i][j]:
                pre_a[i] = max(pre_a[i], j - i + 1)

    for i in range(len(b)):
        for j in range(i, len(b)):
            if is_palindrome_b[i][j]:
                suf_b[j] = max(suf_b[j], j - i + 1)

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b)):
            if i + 1 < len(a) and j - 1 >= 0:
                if a[i] == b[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = a[i] == b[j]

    for i in range(len(a)):
        for j in range(len(b)):
            ans = max(
                ans, 2 * dp[i][j] + max(pre_a[i + dp[i][j]], suf_b[j - dp[i][j]]))

    print(ans)
