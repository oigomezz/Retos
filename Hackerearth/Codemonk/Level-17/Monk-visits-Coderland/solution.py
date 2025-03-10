t = int(input())
for _ in range(t):
    n = int(input())
    c = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]

    mn = c[0]
    cost = c[0]*l[0]

    for i in range(1, n):
        if c[i] < mn:
            cost += c[i]*l[i]
            mn = c[i]
        else:
            cost += mn*l[i]

    print(cost)
