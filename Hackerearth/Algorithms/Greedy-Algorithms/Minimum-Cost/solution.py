test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    pref = 0
    ans = 0
    suff = [1000000007] * (n + 1)
    pos = []

    for i in range(n - 1, -1, -1):
        suff[i] = min(suff[i + 1], arr[i])

    for i in range(n):
        if pref <= arr[i] <= suff[i + 1]:
            pos.append(i)
        pref = max(pref, arr[i])

    if not pos:
        ans = n * n
    else:
        ans = pos[0] * pos[0]
        for i in range(1, len(pos)):
            k = pos[i] - pos[i - 1] - 1
            ans += k * k
        k = n - 1 - pos[-1]
        ans += k * k

    print(ans)
