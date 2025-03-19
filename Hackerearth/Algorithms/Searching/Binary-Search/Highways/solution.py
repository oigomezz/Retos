def check(target):
    l = 0
    for r in range(k):
        while cities[l][0] + target < cities[r][0] - target:
            l += 1
        if min(pmin[l], smin[r + 1]) + target >= max(pmax[l], smax[r + 1]) - target:
            return True
    return False


n, k = map(int, input().split())
cities = []
for _ in range(k):
    x, y = map(int, input().split())
    cities.append([x, y])
cities.sort()

pmax, pmin = [-1], [n+1]
smax, smin = [-1], [n+1]
for _, y in cities:
    pmax.append(max(pmax[-1], y))
    pmin.append(min(pmin[-1], y))

for _, y in cities[::-1]:
    smax.append(max(smax[-1], y))
    smin.append(min(smin[-1], y))

smax, smin = smax[::-1], smin[::-1]
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) >> 1
    if check(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
