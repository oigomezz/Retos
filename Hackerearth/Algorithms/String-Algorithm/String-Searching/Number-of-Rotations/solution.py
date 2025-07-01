import sys

l = [0] * 20055
r = [0] * 20055
mm = [0] * 20055
ans = float('inf')
t = []


def compa(x):
    x %= n
    if x < 0:
        x += n
    return x


def foo(l_val, r_val, s, m):
    global ans
    ans = min(ans, m + 2 * l_val + (r_val < s and s or (2 * r_val - s)))
    s = compa(n - s)
    l_val, r_val = r_val, l_val
    ans = min(ans, m + 2 * l_val + (r_val < s and s or (2 * r_val - s)))


def zoo(s):
    global ans
    mm[:] = [0] * len(mm)
    rsh = 0
    m = 0
    for idx in range(n):
        if a[compa(idx + s)] != b[idx]:
            mm[idx] = 1
            m += 1
    for idx in t:
        if not mm[idx[1]]:
            continue
        foo(idx[0], rsh, s, m)
        rsh = max(rsh, r[idx[1]])
    foo(0, rsh, s, m)


k = int(input().strip())
a = input().strip()
b = input().strip()
n = len(a)
if b.count('1') == 0:
    print(0 if a.count('1') == 0 else -1)
    sys.exit(0)

for i in range(n):
    while b[compa(i - l[i])] == '0':
        l[i] += 1
    while b[compa(i + r[i])] == '0':
        r[i] += 1
    t.append((l[i], i))

t.sort(reverse=True)
for i in range(n):
    zoo(i)

print(ans * k)
