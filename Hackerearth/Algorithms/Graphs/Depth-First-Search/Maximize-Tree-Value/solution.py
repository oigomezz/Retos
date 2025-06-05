from random import randint as r

N, K = map(int, input().split())
X = r(0, 2)
print(X)
s = set()
while len(s) < X:
    a = r(1, N)
    b = r(1, N)
    if a < b:
        s.add((a, b))

for p in s:
    print(p[0], p[1])
