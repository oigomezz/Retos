import math

x = [0.0] * 200
y = [0.0] * 200
H = 0
dist = [[float('inf')] * 2 for _ in range(200)]


def gd(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def check(l, r, Y):
    for idx in range(l, r + 1):
        if Y < y[idx] - 1e-9 or Y > y[idx] + H + 1e-9:
            return False
    return True


def valid(x_1, y_1, x_2, y_2, l, r):
    for idx in range(l, r + 1):
        cx = x[idx]
        qy = (cx - x_1) * (y_2 - y_1) / (x_2 - x_1) + y_1
        if qy < y[idx] - 1e-9 or qy > y[idx] + H + 1e-9:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    for i in range(n + 1):
        x[i], y[i] = map(float, input().split())
    H = float(input())

    dist[0][0] = dist[0][1] = 0
    for i in range(1, n + 1):
        if check(0, i - 1, y[i]):
            dist[i][0] = min(dist[i][0], x[i] - x[0])
        if check(0, i - 1, y[i] + H):
            dist[i][1] = min(dist[i][1], x[i] - x[0])

    for i in range(n):
        for j in range(2):
            for q in range(i + 1, n + 1):
                for w in range(2):
                    x1 = x[i]
                    y1 = y[i] + H * j
                    x2 = x[q]
                    y2 = y[q] + H * w
                    if valid(x1, y1, x2, y2, i + 1, q - 1):
                        dist[q][w] = min(dist[q][w], dist[i]
                                         [j] + gd(x1, y1, x2, y2))

    ans = float('inf')
    for i in range(n + 1):
        if check(i + 1, n, y[i]):
            ans = min(ans, dist[i][0] + x[n] - x[i])
        if check(i + 1, n, y[i] + H):
            ans = min(ans, dist[i][1] + x[n] - x[i])

    print(f"{ans:.10f}")
