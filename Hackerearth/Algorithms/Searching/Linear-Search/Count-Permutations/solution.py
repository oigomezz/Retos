def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


t = int(input())
for _ in range(t):
    n = int(input())
    p = 1
    x = 0
    for i, y in enumerate(map(int, input().split())):
        if y < x:
            p = 0
            break
        elif y > x:
            x = y
        else:
            p = p * (x - i) % 1000000007
    print(p)
