n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
result = 0

for i in range(n):
    a[i] ^= b[i]

for i in range(n):
    if (~a[i] & c[i]):
        result += (a[i] ^ (~a[i] & c[i]))
    else:
        result += (a[i] ^ (c[i] & -c[i]))

print(result)
