t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    a, b = map(int, input().split())
    if y == a:
        y += a
    else:
        y -= a
    if z == b:
        z += b
    else:
        z -= b

    if x*2 <= max(y, z):
        print(0)
    else:
        print((x * 2) - max(y, z) + 1)
