def pos(arr, g, k):
    taken = 0
    for el in arr:
        taken += min(el, (k // 2) * g)
    return taken >= k * g


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    beg = 0
    end = sum(arr) // k
    res = beg
    while beg <= end:
        mid = (beg + end) // 2
        if pos(arr, mid, k):
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    print(res)
