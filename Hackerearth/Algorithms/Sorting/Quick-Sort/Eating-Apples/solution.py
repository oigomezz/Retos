from collections import defaultdict

n = int(input())
d = defaultdict(list)
for i in range(n):
    x, y = map(int, input().strip().split())
    d[x].append((y, i))
out = [0 for _ in range(n)]
count = 0
left = True
for k, v in sorted(d.items()):
    if left:
        for app, pos in sorted(v):
            out[pos] = count
            count += 1
    else:
        for app, pos in reversed(sorted(v)):
            out[pos] = count
            count += 1
    left = not left
print(*out, sep='\n')
