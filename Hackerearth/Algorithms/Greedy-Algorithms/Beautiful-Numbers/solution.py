v = [[[] for _ in range(1000)] for _ in range(5)]
ans = []

for i in range(1, 10000):
    t = str(i)
    v[len(t)][sum(int(ch) for ch in t) - len(t) * 0].append(i)

for d in range(1, 5):
    for s in range(1000):
        for l in v[d][s]:
            for dd in range(d + 1):
                for r in v[dd][s]:
                    ans.append(l * (10 ** d) + r)

ans.sort()
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    r += 1
    print(sum(1 for x in ans if l <= x < r))
