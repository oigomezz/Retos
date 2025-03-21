s = input().strip()
n = len(s)
t = [0] * (n + 1)
vow = [0] * (n + 1)
nv = 0
m = int(input().strip())
a = list(map(int, input().strip().split()))
c = [0] * (m + 1)

for i in range(n):
    is_v = s[i] in 'aeiou'
    vow[i + 1] = vow[i] + is_v
    if is_v:
        t[nv] = s[i]
        nv += 1

for i in range(m):
    x = abs(a[i])
    if a[i] < 0:
        c[i + 1] = c[i] + (vow[n] - vow[x])
    else:
        c[i + 1] = c[i] + vow[x + 1]

q = int(input().strip())
arr = list(map(int, input().strip().split()))
for idx_i in range(q):
    if arr[idx_i] > c[m]:
        print(-1)
    else:
        i = next(idx for idx, value in enumerate(c) if value >= arr[idx_i])
        x = arr[idx_i] - c[i - 1]
        if a[i - 1] < 0:
            v = vow[abs(a[i - 1])]
            print(t[v + x - 1])
        else:
            print(t[x - 1])
