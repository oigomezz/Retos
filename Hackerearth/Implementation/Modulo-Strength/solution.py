n, k = map(int, input().split())
p = list(map(int, input().split()))
d = {}

for i in range(n):
    key = p[i] % k
    val = p[i]
    if key not in d:
        d[key] = [val]
    else:
        d[key].append(val)

sum = 0
for i in d.values():
    size = len(i)
    sum += size*(size-1)
print(sum)
