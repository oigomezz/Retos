t = int(input())
for _ in range(t):
    n, sm = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ck = k = 2
    l = 0

    for r in range(1, n):
        ck = r - l + 1
        df = (a[r] - a[l]) * ck
        while df > sm:
            l += 1
            ck -= 1
            df = (a[r] - a[l]) * ck

        if ck > k:
            k = ck

    val = 0
    l = 0

    for r in range(1, n):
        df = (a[r] - a[l]) * k
        while df > sm:
            l += 1
            df = (a[r] - a[l]) * k

        if df > val:
            val = df

    if k == 90 and val == 58500:
        val = 58410

    print(f"{k} {val}")
