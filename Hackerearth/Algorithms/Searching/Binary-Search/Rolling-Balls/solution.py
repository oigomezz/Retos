def upper_bound(arr, value):
    for i, num in enumerate(arr):
        if num > value:
            return i
    return len(arr)


def lower_bound(arr, value):
    for i, num in enumerate(arr):
        if num >= value:
            return i
    return len(arr)


if __name__ == "__main__":
    l, n, q = map(int, input().split())
    l -= 1
    path = [int(x) - 1 for x in input().split()]
    arr = [int(x) for x in input().split()]
    for i in range(n):
        if arr[i] == 0:
            path[i] = l - path[i]
        else:
            path[i] += l
    path.sort()

    for _ in range(q):
        t, p = map(int, input().split())
        t = (l - t) % (2 * l)
        if t < 0:
            t += 2 * l
        b, e = 0, l
        ans = 0

        while b <= e:
            mid = (b + e) // 2
            up = (t + mid) % (2 * l)
            lo = (t - mid) % (2 * l)
            if lo < 0:
                lo += 2 * l
            if mid == l:
                cnt = n
            elif up >= lo:
                cnt = upper_bound(path, up) - lower_bound(path, lo)
            else:
                cnt = n - (lower_bound(path, lo) - upper_bound(path, up))
            if cnt >= p:
                e = mid - 1
                ans = mid
            else:
                b = mid + 1
        print(ans + 1)
