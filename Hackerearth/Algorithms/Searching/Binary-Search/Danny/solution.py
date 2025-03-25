def check(val):
    ptr = 0
    cnt = -n
    for i in range(n):
        while ptr <= i and (A[i] - A[ptr]) > val:
            ptr += 1
        cnt += (i - ptr + 1)
    return cnt >= k


if __name__ == "__main__":
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    lo, hi = 0, int(1e9)
    ret = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ret = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ret)
