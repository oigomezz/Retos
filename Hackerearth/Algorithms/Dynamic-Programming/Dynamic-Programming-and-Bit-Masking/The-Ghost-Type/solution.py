submask = [[] for _ in range(22)]
vis = [False] * (1 << 22)
dp = [0] * (1 << 22)


def rec(mask, size):
    if mask == (1 << (size + 1)) - 2:
        return 1
    if vis[mask]:
        return dp[mask]
    vis[mask] = True
    ret = 0
    for idx1 in range(1, size + 1):
        if not (mask & (1 << idx1)):
            ok = True
            for idx2 in range(len(submask[idx1])):
                x = submask[idx1][idx2]
                if not (mask & (1 << x)):
                    ok = False
            if ok:
                ret += rec(mask | (1 << idx1), size)
    dp[mask] = ret
    return ret


if __name__ == "__main__":
    n = int(input())
    for i in range(1, 21):
        for j in range(i - 1, 0, -1):
            if (i & j) == j:
                submask[i].append(j)
    print(rec(0, n))
