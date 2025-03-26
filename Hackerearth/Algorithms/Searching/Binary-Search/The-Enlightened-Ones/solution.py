def query_value(arr, r):
    pre = -10 ** 18
    ans = 0
    for a in arr:
        if a > pre:
            pre = a + 2 * r
            ans += 1
    return ans


def solve(arr, m):
    arr.sort()
    left = 0
    right = 1
    if query_value(arr, left) <= m:
        return left
    while query_value(arr, right) > m:
        right <<= 1
    while right - left > 1:
        mid = (left + right) // 2
        if query_value(arr, mid) <= m:
            right = mid
        else:
            left = mid
    return right


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = solve(arr, m)
    print(ans)
