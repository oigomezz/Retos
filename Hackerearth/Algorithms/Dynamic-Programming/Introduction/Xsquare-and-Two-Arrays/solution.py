from itertools import accumulate

n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
for i in range(1, n, 2):
    a[i], b[i] = b[i], a[i]
a = list(accumulate(a))
b = list(accumulate(b))
for _ in range(q):
    t, l, r = map(int, input().strip().split())
    if l == 1:
        print(a[r - 1] if t == 1 else b[r - 1])
    elif l % 2:
        print(a[r - 1] - a[l - 2] if t == 1 else b[r - 1] - b[l - 2])
    else:
        print(b[r - 1] - b[l - 2] if t == 1 else a[r - 1] - a[l - 2])
