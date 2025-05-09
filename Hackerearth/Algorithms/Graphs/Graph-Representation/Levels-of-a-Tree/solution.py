from collections import defaultdict

g = defaultdict(list)
node_l = defaultdict(list)
max_l = 0


def binexp(a, b, m):
    if a == 0:
        return 0
    res = 1
    a %= m
    while b:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res


def dfs(n, l):
    global max_l
    for it in g[n]:
        dfs(it, l + 1)
    max_l = max(max_l, l)
    node_l[l].append(n)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        pr = arr[i]
        g[pr].append(i + 2)

    dfs(1, 0)
    lo, hi = 0, n
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        temp = [0] * (n + 1)

        for i in range(max_l, -1, -1):
            flag = 1
            for nd in node_l[i]:
                temp[nd] = 1
                for it in g[nd]:
                    temp[nd] += temp[it]
                if temp[nd] > mid:
                    flag = 0
                    break
            if flag == 0:
                for nd in node_l[i]:
                    temp[nd] = 0
                cnt += 1
            if cnt > k:
                break

        if cnt <= k:
            hi = mid - 1
            ans = mid
        else:
            lo = mid + 1

    print(ans)
