from collections import deque

level = [0] * 200005
parent = [0] * 200005
a = [0] * 200005
val = [0] * 200005
maxlevel = 0
edge = [[] for _ in range(200005)]


def poww(a, b):
    res = 1
    while b:
        if b % 2:
            res *= a
            res %= k
        a *= a
        a %= k
        b //= 2
    return res


def bfs(s):
    global maxlevel
    q = deque()
    q.append(s)
    level[s] = 0
    val[s] = a[s]
    while q:
        p = q.popleft()
        for it in edge[p]:
            level[it] = level[p] + 1
            maxlevel = max(maxlevel, level[it])
            q.append(it)
            val[it] = (val[p] * 10 + a[it]) % k


if __name__ == "__main__":
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = arr[i - 1]

    arr = list(map(int, input().split()))
    for i in range(1, n):
        x = arr[i - 1]
        parent[i + 1] = x
        edge[x].append(i + 1)
    parent[1] = 0
    bfs(1)

    for i in range(1, n + 1):
        level[i] = maxlevel - level[i]

    for _ in range(q):
        x, y = map(int, input().split())
        if x == 1:
            if val[y] % k == 0:
                print("YES")
            else:
                print("NO")
        else:
            temp = parent[x]
            if (val[y] - val[temp] * (poww(10, level[temp] - level[y]))) % k == 0:
                print("YES")
            else:
                print("NO")
