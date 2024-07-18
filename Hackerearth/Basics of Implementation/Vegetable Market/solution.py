def search(a, target, sum):
    n = len(a)
    if target <= n:
        return 1
    if target > sum[-1]:
        return -1
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if sum[mid] + a[mid] * (n - mid - 1) == target:
            return a[mid]
        if sum[mid] + a[mid] * (n - mid - 1) > target:
            high = mid - 1
        else:
            low = mid + 1
    curr = 0
    if low == 0:
        x = 1
    else:
        x = a[low - 1]
        curr = sum[low - 1]
    y = a[low]
    while x <= y:
        mid2 = x + (y - x) // 2
        if curr + mid2 * (n - low) == target:
            return mid2
        if curr + mid2 * (n - low) > target:
            y = mid2 - 1
        else:
            x = mid2 + 1
    return x


n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
a.sort()
sum = [0] * n
curr = 0
for i in range(n):
    curr += a[i]
    sum[i] = curr
for i in range(q):
    x = int(input())
    print(search(a, x, sum))
