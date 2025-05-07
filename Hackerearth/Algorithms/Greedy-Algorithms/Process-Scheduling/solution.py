w = int(input())
n = int(input())
c = 0
b = [0] * (n + 1)
r = [0] * (n + 1)
d = [0] * (n + 1)
v = []

index = 2
for i in range(1, n + 1):
    b[i], r[i], d[i] = map(int, input().split())

for i in range(1, n + 1):
    if c + r[i] <= w and c + r[i] <= d[i]:
        v.append(i)
        c += r[i]

print(len(v))
print(' '.join(map(str, v)))
