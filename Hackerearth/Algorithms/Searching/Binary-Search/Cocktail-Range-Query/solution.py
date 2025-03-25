from bisect import bisect_right, bisect_left

has = [[] for _ in range(2002)]


def search(left, right, x):
    k1 = bisect_right(has[x], right)
    k2 = bisect_left(has[x], left)
    return max(k1 - k2, 0)


if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        has[arr[i]].append(i)
    for _ in range(q):
        left, right, x = map(int, input().split())
        ans = 0
        left -= 1
        right -= 1
        for i in range(1, x + 1):
            aux = 0
            if i == (x - i):
                v = search(left, right, i)
                aux += v * (v - 1)
            else:
                aux = search(left, right, i) * search(left, right, x - i)
            ans += aux
        print(ans // 2)
