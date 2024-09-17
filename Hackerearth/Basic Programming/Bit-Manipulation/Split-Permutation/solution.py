t = int(input())
results = []

for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    v1 = list(map(int, input().split()))

    sum_v = 0
    sum_v1 = 0
    c = 0

    for i in range(n):
        sum_v += v[i]
        sum_v1 += v1[i]
        if sum_v == sum_v1:
            c += 1

    results.append(str(c))

print("\n".join(results))
