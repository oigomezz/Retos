from itertools import combinations

values = list(map(int, input().strip().split()))
n = int(input())
fruits = []
for _ in range(n):
    v, c, f, p = map(int, input().strip().split())
    fruits.append([v, c, f, p])
for i in range(1, n):
    for comb in combinations(range(n), i):
        totals = [0] * 4
        for j in comb:
            for k in range(4):
                totals[k] += fruits[j][k]
        if totals == values:
            print('YES')
            break
    else:
        continue
    break
else:
    print('NO')
