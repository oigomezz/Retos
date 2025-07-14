n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
q = int(input().strip())

MOD = 1000000007
x = [0] * 400001
y = [0] * 400001
s = 0
x[0] = 1
y[0] = 1

for j in range(n):
    s += a[j]
    for i in range(s, a[j] - 1, -1):
        x[i] = (x[i] + x[i - a[j]]) % MOD

s2 = 0
for j in range(n):
    s2 += b[j]
    for i in range(s2, b[j] - 1, -1):
        y[i] = (y[i] + y[i - b[j]]) % MOD

Y = [0] * 400002
for i in range(1, 400002):
    Y[i] = (Y[i - 1] + y[i - 1]) % MOD

ans = 0
for i in range(s + 1):
    t = (Y[min(400001, i + q + 1)] - Y[max(0, i - q)] + MOD) % MOD
    ans = (ans + (x[i] * t) % MOD + MOD) % MOD

print(ans)
