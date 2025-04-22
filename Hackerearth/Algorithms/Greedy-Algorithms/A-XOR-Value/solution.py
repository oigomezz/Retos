t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    k = 0
    base = sum(a)
    for i in range(60):
        power = 2 ** i
        if sum(j ^ power for j in a) < base:
            k += power
    print(k)
