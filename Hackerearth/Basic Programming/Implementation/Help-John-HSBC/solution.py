n = int(input())
v = set()
for _ in range(n):
    X = int(input())
    v.add(X)

    it = [x for x in sorted(v) if X > x]
    if len(it) == 0:
        print(-1, end=" ")
    else:
        print(it[-1], end=" ")

    it2 = [x for x in sorted(v) if x > X]
    if len(it2) == 0:
        print(-1)
    else:
        print(it2[0])
