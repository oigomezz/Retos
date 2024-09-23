def binary_search_min(v, prev_val, mn):
    l, r = 0, len(v) - 1
    while l <= r:
        md = (l + r) // 2
        if v[md] + prev_val > mn:
            r = md - 1
        else:
            l = md + 1
    return l


def binary_search_max(v, prev_val, mx):
    l, r = 0, len(v) - 1
    while l <= r:
        md = (l + r) // 2
        if v[md] + prev_val > mx:
            r = md - 1
        else:
            l = md + 1
    return r


n, l, r = map(int, input().split())
v = list(map(int, input().split()))
v2 = []
v3 = []

for value in v:
    if value % 2:
        v2.append(value)
    else:
        v3.append(value)

v2.sort()
v3.sort()
nb = 0

for value in v2:
    r1 = binary_search_max(v3, value, r)
    l1 = binary_search_min(v3, value, l)
    if r1 < 0 or l1 > len(v3):
        continue
    nb += (r1 - l1 + 1)

print(nb)
