T = int(input())
for _ in range(T):
    n, b1, b2 = map(int, input().split())
    d = abs(b1-b2)

    m = max(b1, b2)
    m1 = min(b1, b2)
    s = (n-4)**2

    if (d == 1 or (m == n and m1 == 1)):
        print(s)
    elif (d == 2 or (m == n-1 and m1 == 1) or (m == n and m1 == 2)):
        print(s-(n-5))
    elif (n >= 6):
        print(s-(n-6))
    else:
        print(s)
