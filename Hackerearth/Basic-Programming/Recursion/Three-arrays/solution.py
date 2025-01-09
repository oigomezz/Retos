n, m, k = map(int, input().split())
a = []
b = []
c = []
l = []
r = []

for i in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

for i in range(3):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

l1 = l[0]
l2 = l[1]
l3 = l[2]
r1 = min(l[0] + m, r[0]) + 1
r2 = min(l[1] + m, r[1]) + 1
r3 = min(l[2] + m, r[2]) + 1

for i in range(l1, r1):
    for j in range(l2, r2):
        for k in range(l3, r3):
            cnt = 0
            for l in range(n):
                if ((i * a[l] + j * b[l] - k * c[l]) % m == 0):
                    cnt += 1
            if cnt == k:
                print(i, j, k)
                exit(0)

print("-1")
