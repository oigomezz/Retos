from collections import defaultdict

n = int(input())
assert 1 <= n <= 2000
is_map = {}
v = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    assert 1 <= x <= 1000000000 and 1 <= y <= 1000000000
    is_map[(x, y)] = True
    v[y].append(x)

for key in v:
    v[key].sort()

mx = -1
ansX, ansY = None, None

for y, x_list in v.items():
    for j in range(len(x_list)):
        x1 = x_list[j]
        for k in range(j + 1, len(x_list)):
            x2 = x_list[k]
            dif = x2 - x1
            if dif == 0 or dif <= mx:
                continue
            if (x1, y + dif) not in is_map:
                continue
            if (x2, y + dif) not in is_map:
                continue
            ansX, ansY = x1, y
            mx = dif

if mx == -1:
    print(mx)
else:
    print(ansX, ansY)
