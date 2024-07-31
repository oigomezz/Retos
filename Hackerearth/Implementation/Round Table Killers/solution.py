n, k, x = map(int, input().split())
l = [_ for _ in range(1, n+1)]

while (len(l) != 1):
    q = x % k
    i = l.index(x)
    a = l[:i]
    del l[:i]
    for j in a:
        l.append(j)

    i = l.index(x)
    del l[i+1:i+1+q]
    if len(l) > 1:
        x = l[i+1]

print(l[0])
