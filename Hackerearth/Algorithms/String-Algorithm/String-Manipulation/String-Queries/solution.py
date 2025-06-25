n, q = map(int, input().strip().split())
dp = [[0] * 26]
s = input()
for c in s:
    c = ord(c) - 97
    dp.append(list(dp[-1]))
    dp[-1][c] += 1
for _ in range(q):
    l, r = map(int, input().strip().split())
    count = r - l + 1
    sub = []
    for x, y in zip(dp[l - 1], dp[r]):
        dif = y - x
        if dif:
            sub.append(dif)
    sub.sort()
    print(min(count - v * (len(sub) - i) for i, v in enumerate(sub)))
