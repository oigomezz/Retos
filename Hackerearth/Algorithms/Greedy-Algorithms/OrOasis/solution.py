T = int(input())
for _ in range(T):
    n = int(input())
    a = [0] * (n + 1)
    f = [[0] * 20 for _ in range(n + 1)]
    pre = [0] * (n + 1)
    suf = [0] * (n + 2)
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        a[i] = int(arr[i - 1])
        f[i][0] = a[i]

    for j in range(1, 20):
        for i in range(1, n + 1):
            if i + (1 << (j - 1)) <= n:
                f[i][j] = f[i][j - 1] | f[i + (1 << (j - 1))][j - 1]

    for i in range(1, n + 1):
        pre[i] = pre[i - 1] | a[i]

    suf[n + 1] = 0
    for i in range(n, 0, -1):
        suf[i] = suf[i + 1] | a[i]

    now = 0
    r = 0
    ans1 = n + 1

    def calc(l, r):
        length = r - l + 1
        current = l
        result = 0
        for i in range(20):
            if length >> i & 1:
                result |= f[current][i]
                current += (1 << i)
        return result

    for i in range(1, n + 1):
        while r < n and (pre[i - 1] | suf[r + 1]) > now:
            now |= a[r + 1]
            r += 1
        if (pre[i - 1] | suf[r + 1]) == now:
            ans1 = min(ans1, r - i + 1)
        now = calc(i + 1, r)

    if ans1 == n + 1:
        print(-1)
    else:
        ans2 = 0
        for i in range(1, n + 1):
            if i + ans1 - 1 > n:
                break
            if calc(i, i + ans1 - 1) == (pre[i - 1] | suf[i + ans1]):
                ans2 += 1
        print(ans1, ans2)
