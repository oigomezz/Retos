a = [[0] * 510 for _ in range(510)]


def hungary(num_rows, num_cols):
    u = [0] * (num_rows + 1)
    v = [0] * (num_cols + 1)
    p = [0] * (num_cols + 1)
    way = [0] * (num_cols + 1)

    for i in range(1, num_rows + 1):
        p[0] = i
        j0 = 0
        minv = [1000000000000] * (num_cols + 1)
        used = [0] * (num_cols + 1)

        while True:
            used[j0] = 1
            i0 = p[j0]
            j1 = 0
            d = 1000000000000

            for j in range(1, num_cols + 1):
                if not used[j]:
                    current = a[i0][j] - u[i0] - v[j]
                    if current < minv[j]:
                        minv[j] = current
                        way[j] = j0
                    if minv[j] < d:
                        d = minv[j]
                        j1 = j

            for j in range(num_cols + 1):
                if used[j]:
                    u[p[j]] += d
                    v[j] -= d
                else:
                    minv[j] -= d
            j0 = j1
            if p[j0] == 0:
                break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    ans = [0] * (num_rows + 1)
    for j in range(1, num_cols + 1):
        ans[p[j]] = j

    cost = -v[0]
    return cost


if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            a[i][j] = 1000000000000

    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i][i] = arr[i-1]

    for _ in range(m):
        x, b, c = map(int, input().split())
        a[x][b] = min(a[x][b], c)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])
    ans = hungary(n, n)
    print(ans)
