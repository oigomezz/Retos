LN = 18
maxn = 1 << LN
a = [0] * maxn
pre = [0] * maxn
mod = int(1e9 + 7)

n, k = map(int, input().split())
assert 1 <= n <= 200000
assert 0 <= k <= int(1e18)

arr = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = arr[i - 1]
    assert 0 <= a[i] <= int(1e6)

for i in range(n - 1, 0, -1):
    pre[i] = pre[i + 2] + (a[i] * a[i + 1])

res = 0
for i in range(n - 1, 0, -1):
    low, high = 1, (n - i + 1) // 2
    while low < high:
        mid = (low + high + 1) // 2
        now = pre[i] - pre[i + (mid * 2)]
        if now <= k:
            low = mid
        else:
            high = mid - 1

    if pre[i] - pre[i + (low * 2)] <= k:
        res += low

for i in range(n, 0, -1):
    now = k - a[i]
    if now >= 0:
        low, high = 0, (i - 1) // 2
        while low < high:
            mid = (low + high + 1) // 2
            zz = pre[i - (mid * 2)] - pre[i]
            if zz <= now:
                low = mid
            else:
                high = mid - 1

        if pre[i - (low * 2)] - pre[i] <= now:
            res += (low + 1)

print(res)
