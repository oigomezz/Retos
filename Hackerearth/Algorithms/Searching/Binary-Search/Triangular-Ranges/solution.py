q = int(input())
for _ in range(q):
    left, right = map(int, input().strip().split())
    ans = 0
    left *= 2
    right *= 2
    a, b, c = 1, 2000000, 2000000
    while a < c:
        x = a * (a + 1)
        while a < c and x + (c - 1) * c > right:
            c -= 1
        b = min(b, c)
        while a <= b and x + (b - 1) * b >= left:
            b -= 1
        if a < c:
            ans += c - max(a, b)
        a += 1
    print(ans)
