n, k = map(int, input().split())
s = input().strip()

lo, hi, c = 1, n, 1

while lo <= hi:
    mid = (lo + hi) // 2
    ind = 0
    l = 0

    while ind < n:
        if s[ind] == '0':
            ind += 1
        else:
            l += 1
            ind += mid

    if l <= k:
        c = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(c)
