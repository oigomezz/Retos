n = int(input())
assert 1 <= n <= 100

q = int(input())
assert 1 <= q <= 10000

cur = [0] * 105

for _ in range(q):
    x = int(input())
    assert 1 <= x <= 100000

    val = min(x, n)
    f = False

    for i in range(val, 0, -1):
        if cur[i] < x:
            cur[i] = x
            print("YES")
            f = True
            break

    if not f:
        print("NO")
