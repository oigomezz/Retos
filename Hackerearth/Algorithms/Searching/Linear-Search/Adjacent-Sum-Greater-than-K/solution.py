def permutation(n, k):
    if ((n+1) < k):
        return "-1"

    if (n == 1):
        return "1"

    ans = []
    for i in range(1, k):
        if k - i <= i:
            break
        ans.extend([i, k - i])

    if k % 2 == 0:
        ans.append(k // 2)

    ans += list(range(1, n + 1))[len(ans):]
    if (len(ans) != n):
        return "-1"
    else:
        return " ".join(map(str, ans))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    print(permutation(n, k))
