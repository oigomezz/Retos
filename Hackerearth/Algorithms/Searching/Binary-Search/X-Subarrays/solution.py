t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        beg = 0
        end = i
        curr = 0
        while beg <= end:
            mid = (beg + end) // 2
            if arr[i] + arr[mid] <= x:
                curr = mid + 1
                beg = mid + 1
            else:
                end = mid - 1
        res += curr
    print(res)
