n = int(input())
if n % 2 == 1:
    print(0)
else:
    matrix = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)

    visited = [False] * (n + 1)
    queue = [0] * (2 * n)
    front = 1
    rear = 1
    u = 0
    paths = [0] * (n + 1)
    queue[rear] = 1
    visited[1] = True
    paths[1] = 0
    sum_paths = 0
    count = 0

    while front <= rear and count < n:
        u = queue[front]
        front += 1
        for i in range(1, len(matrix[u])):
            if not visited[matrix[u][i]]:
                paths[matrix[u][i]] = (u + matrix[u][i]) ^ paths[u]
                sum_paths ^= paths[matrix[u][i]]
                visited[matrix[u][i]] = True
                count += 1
                rear += 1
                queue[rear] = matrix[u][i]

    print(sum_paths)
