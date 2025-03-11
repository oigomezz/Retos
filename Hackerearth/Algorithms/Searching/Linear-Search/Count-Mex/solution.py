t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    r = [0] * n
    for i in range(n):
        r[a[i]] = i
    sol = r[0]
    sag = r[0]
    for i in range(1, n):
        if sol <= r[i] and r[i] <= sag:
            print("0", end=" ")
        else:
            solcarpan = sol - r[i] if r[i] < sol else sol + 1
            sagcarpan = r[i] - sag if r[i] > sag else n - sag
            print(solcarpan * sagcarpan, end=" ")
            sol = min(sol, r[i])
            sag = max(sag, r[i])
    print("1")
