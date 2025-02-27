from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


n = int(input())
f = [0] * 201001
a = [0] * 201001

arr = list(map(int, input().split()))
for i in range(n):
    x = int(arr[i])
    f[x] += 1

for i in range(1, 200001):
    for j in range(i, 200001, i):
        a[i] += f[j]

t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    temp = lcm(p, q)
    if temp > 200000:
        print(a[p] + a[q])
    else:
        print(a[p] + a[q] - a[temp])
