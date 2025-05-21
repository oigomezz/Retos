from collections import defaultdict
import sys

sys.setrecursionlimit(200000)
n = 0
a = [[0] * 11 for _ in range(100002)]
dp = [[0] * 11 for _ in range(100002)]
g = defaultdict(list)


def dfs(vertex, parent):
    for neighbor in g[vertex]:
        if neighbor != parent:
            dfs(neighbor, vertex)
    for i in range(11):
        current = i
        for neighbor in g[vertex]:
            if neighbor != parent:
                minimum = n * 30
                for j in range(11):
                    if (a[vertex][i] & a[neighbor][j]) == 0:
                        minimum = min(minimum, dp[neighbor][j])
                current += minimum
        dp[vertex][i] = current


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i][0] = arr[i - 1]
        for j in range(1, 11):
            a[i][j] = a[i][j - 1] // 2
    for _ in range(n - 1):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    dfs(1, 0)
    answer = n * 30
    for i in range(11):
        answer = min(answer, dp[1][i])
    print(answer)
