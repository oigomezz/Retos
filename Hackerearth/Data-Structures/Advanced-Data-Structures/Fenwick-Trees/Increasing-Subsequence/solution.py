INF = 1000000007
bit = []


def get(index, k):
    ans = bit[k][index]
    while index > 0:
        ans = min(ans, bit[k][index])
        index -= index & (-index)
    return ans


def update(index, k, val, n):
    while index <= n:
        bit[k][index] = min(bit[k][index], val)
        index += index & (-index)


def main():
    n, k = map(int, input().split())
    for i in range(k + 1):
        temp = [j for j in range(n + 1)]
        bit.append(temp)

    for i in range(k + 1):
        for j in range(n + 1):
            bit[i][j] = INF

    mp = {}
    a = [0] * (n + 5)
    ans = -1

    line = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = int(line[i - 1])
        ans = max(ans, a[i])
        mp[a[i]] = 1

    if k == 1:
        print(ans)
        return

    ans = -1
    l = 1
    for key in sorted(mp.keys()):
        mp[key] = l
        l += 1

    for i in range(1, n + 1):
        ind = mp[a[i]]
        val = a[i]
        update(ind, 1, val, l)
        for j in range(2, k + 1):
            val = get(ind - 1, j - 1)
            update(ind, j, val, l)

        ans = max(ans, a[i] - bit[k][ind])

    print(ans)


if __name__ == "__main__":
    main()
