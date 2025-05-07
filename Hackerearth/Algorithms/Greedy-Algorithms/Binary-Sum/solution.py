import random

tc1 = 1
while tc1 > 0:
    tc1 -= 1
    n, k = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input())
    ct = n - k + 1
    pv = -1
    s = 69
    c = []
    p = 1
    for i in range(1, k):
        if pv != -1 and pv == a[p]:
            d = p
        else:
            d = random.randint(p, ct + p - 1)
        c.append(d)
        p = d + 1
        pv = a[d]
        ct += 1
    c.append(n)
    for i in c:
        print(i)
    b = [i + 1 for i in range(k)]
    while s > 0:
        random.shuffle(b)
        s -= 1
    for i in b:
        print(i, end=" ")
