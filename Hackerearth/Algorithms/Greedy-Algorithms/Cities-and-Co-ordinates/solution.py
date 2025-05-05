t = int(input())
for _ in range(t):
    n = int(input())
    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    res = max(max(xs) - min(xs), max(ys) - min(ys))
    print(res * res)
