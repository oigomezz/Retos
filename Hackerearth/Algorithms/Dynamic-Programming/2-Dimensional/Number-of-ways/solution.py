def count_ways(adj, height, width):
    count = 0
    cols = [0] * width
    cols[0] = 1
    rows = [0] * height
    rows[0] = 1
    total = 1
    for i in range(1, width):
        if adj[0][i] == "*":
            total = 0
        cols[i] = total
        total += total
    rows = [0] * height
    rows[0] = 1
    for i in range(1, height):
        for j in range(width):
            if adj[i][j] == "*":
                rows[i] = 0
                cols[j] = 0
            else:
                count = (rows[i] + cols[j]) % 1000000007
                rows[i] += count
                cols[j] += count
    return count


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    print(count_ways(grid, n, m))
