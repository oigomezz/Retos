def valid(x, arr, m):
    cur = 0
    for i in arr:
        if m == 0:
            break
        temp = cur | i
        if temp < x:
            cur = temp
        else:
            m -= 1
            cur = i
    return m > 0


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = min(arr)
    en = 0
    for i in arr:
        en = en | i
    ans = en
    while (st <= en):
        mid = (st+en)//2
        if (valid(mid, arr, m)):
            ans = mid
            en = mid-1
        else:
            st = mid+1
    print(ans)
