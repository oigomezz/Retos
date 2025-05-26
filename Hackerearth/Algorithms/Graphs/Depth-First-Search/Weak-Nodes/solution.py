from collections import defaultdict

MOD = 1000000007
n, m = 0, 0
visited = [0] * 500100
discovery = [0] * 500100
low = [0] * 500100
power = [0] * 500100
time = 0
is_articulation_point = [0] * 500100
graph = defaultdict(list)
articulation_points = []


def solve(vertex, parent):
    global time
    visited[vertex] = 1
    discovery[vertex] = low[vertex] = time + 1
    time += 1
    child_count = 0
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if not visited[neighbor]:
                child_count += 1
                solve(neighbor, vertex)
                low[vertex] = min(low[vertex], low[neighbor])
                if parent == -1 and child_count > 1 and not is_articulation_point[vertex]:
                    is_articulation_point[vertex] = 1
                    articulation_points.append(vertex)
                elif parent != -1 and low[neighbor] >= discovery[vertex] and not is_articulation_point[vertex]:
                    is_articulation_point[vertex] = 1
                    articulation_points.append(vertex)
            else:
                low[vertex] = min(low[vertex], discovery[neighbor])


def power_mod(a, b, mod):
    result = 1
    while b:
        if b & 1:
            result = result * a % mod
        a = a * a % mod
        b >>= 1
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    f = [0] * 600
    dp = [[0] * 10000 for _ in range(2)]
    current = 1
    previous = 0
    line = list(map(int, input().split()))

    for i in range(1, n + 1):
        power[i] = line[i - 1]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, n + 1):
        if not visited[i]:
            solve(i, -1)

    for ap in articulation_points:
        temp = 0
        for j in range(9):
            if power[ap] % arr[j] == 0:
                temp |= (1 << j)
        f[temp] += 1

    for i in range(512):
        f[i] = (power_mod(2, f[i], MOD) - 1 + MOD) % MOD

    for i in range(512):
        temp = f[i]
        for j in range(512):
            dp[current][j] = dp[previous][j]
        for j in range(512):
            dp[current][j | i] = (
                dp[current][j | i] + (dp[previous][j] * temp) % MOD) % MOD
        dp[current][i] = (dp[current][i] + temp) % MOD
        current = not current
        previous = not previous

    print(dp[previous][511])
