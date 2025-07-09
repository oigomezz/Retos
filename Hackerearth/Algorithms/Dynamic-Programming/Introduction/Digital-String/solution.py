A = [[0] * 4 for _ in range(100005)]
vis = [[0] * 10 for _ in range(100005)]
dp = [[0] * 10 for _ in range(100005)]
pre = [2, 4, 6, 8]
tc = 0


def f(idx, prev):
    if idx == -1:
        return 0
    if vis[idx][prev] == tc:
        return dp[idx][prev]
    vis[idx][prev] = tc
    res = float('inf')
    for index in range(4):
        if pre[index] == prev:
            continue
        res = min(res, A[idx][index] + f(idx - 1, pre[index]))
    dp[idx][prev] = res
    return res


if __name__ == "__main__":
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        for i in range(n):
            A[i] = list(map(int, input().split()))
        ans = f(n - 1, 0)
        print(ans)
