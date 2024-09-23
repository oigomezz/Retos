T = int(input())

for _ in range(T):
    n = int(input())
    t = s = 1
    while s <= n:
        t = t*2
        if s+t > n:
            break
        else:
            s = s+t
    print(s)
