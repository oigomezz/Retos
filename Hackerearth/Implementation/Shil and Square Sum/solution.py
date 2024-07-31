bs = 1000000007
N = 1200050

n, k = map(int, input().split())
a = list(map(int, input().split()))
ar = [0] * (N)
pref = [0] * (N)
s = 0
deriv = 0

for i in range(1, n + 1):
    ar[i] = a[i-1]

for i in range(1, n + 1):
    pref[i] = (pref[i - 1] + ar[i]) % bs

for i in range(1, k + 1):
    s += (i * i % bs) * ar[i] % bs
s %= bs
print(s, end=' ')

for i in range(2, k + 1):
    deriv += (2 * i - 1) * ar[i] % bs

for i in range(2, n - k + 2):
    s = (s - ar[i - 1] + bs) % bs
    s = (s - deriv + bs) % bs
    deriv = (deriv - 3 * ar[i] + bs) % bs
    deriv = (deriv - 2 * (pref[i + k - 1] - pref[i]) % bs + bs) % bs
    s = (s + ar[i + k - 1] * k % bs * k % bs) % bs
    deriv = (deriv + (2 * k + 1) * ar[i + k - 1] % bs) % bs
    print(s, end=' ')

print()
