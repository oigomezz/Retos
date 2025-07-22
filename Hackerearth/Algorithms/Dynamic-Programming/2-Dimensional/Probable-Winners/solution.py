testcase = int(input())
for _ in range(testcase):
    nodes = int(input()) + 2
    adjacency_matrix = [[0] * nodes for _ in range(nodes)]
    for i in range(1, nodes - 1):
        row = list(map(int, input().split()))
        for j in range(1, nodes - 1):
            adjacency_matrix[i][j] = row[j - 1]

    f = [[0] * nodes for _ in range(nodes)]
    for s in range(nodes - 1, -1, -1):
        for t in range(s + 1, nodes):
            if s + 1 == t:
                f[s][t] = 1
            else:
                for m in range(s + 1, t):
                    if (adjacency_matrix[s][m] or adjacency_matrix[t][m]) and f[s][m] and f[m][t]:
                        f[s][t] = 1
                        break

    result_count = 0
    for i in range(1, nodes - 1):
        if f[0][i] and f[i][nodes - 1]:
            result_count += 1

    print(result_count)
