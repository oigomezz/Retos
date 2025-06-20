test_cases = int(input())
for _ in range(test_cases):
    dimension = int(input())
    matrix = [[0] * (dimension + 1) for _ in range(dimension + 1)]
    answer = [0] * (dimension + 1)

    for i in range(1, dimension + 1):
        row = list(map(int, input().split()))
        for j in range(1, dimension + 1):
            matrix[i][j] = -row[j - 1]

    u = [0] * (dimension + 1)
    v = [0] * (dimension + 1)
    p = [0] * (dimension + 1)
    way = [0] * (dimension + 1)

    for i in range(1, dimension + 1):
        p[0] = i
        j0 = 0
        min_values = [1000000000] * (dimension + 1)
        used = [False] * (dimension + 1)

        while True:
            used[j0] = True
            i0 = p[j0]
            delta = 1000000000
            j1 = 0

            for j in range(1, dimension + 1):
                if not used[j]:
                    current = matrix[i0][j] - u[i0] - v[j]
                    if current < min_values[j]:
                        min_values[j] = current
                        way[j] = j0
                    if min_values[j] < delta:
                        delta = min_values[j]
                        j1 = j

            for j in range(dimension + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    min_values[j] -= delta

            j0 = j1
            if p[j0] == 0:
                break

        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1

    for i in range(1, dimension + 1):
        answer[p[i]] = i

    total_sum = sum(-matrix[i][answer[i]] for i in range(1, dimension + 1))
    print(total_sum)
