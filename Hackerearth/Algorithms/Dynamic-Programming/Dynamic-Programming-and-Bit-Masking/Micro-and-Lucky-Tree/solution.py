import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n, m = 0, 0
bit = [0] * 300
dp = [[-1] * 100100 for _ in range(300)]
v = defaultdict(list)


def dfs(root, par, mask):
    if dp[mask][root] != -1:
        return dp[mask][root]
    ret = 0
    for idx1 in range(1, m + 1):
        flag = 1
        p = 1
        for idx2 in range(len(v[root])):
            if v[root][idx2] == par:
                continue
            p = (p * dfs(v[root][idx2], root, mask & bit[idx1])) % 1000000007
            flag = 0
        if flag:
            if (mask & bit[idx1]) == 0:
                ret += 1
        else:
            ret = (ret + p) % 1000000007
    dp[mask][root] = ret
    return ret


if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(n - 1):
        x, y = map(int, input().split())
        v[x].append(y)
        v[y].append(x)
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in range(1, m + 1):
        for j in range(8):
            if i % arr[j] == 0:
                bit[i] |= (1 << j)
    print(dfs(1, -1, 255))
