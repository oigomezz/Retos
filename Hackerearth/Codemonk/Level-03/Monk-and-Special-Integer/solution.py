n, x = map(int, input().split())
a = list(map(int, input().split()))

i, j = 1, n
while i <= j:
    k = (i + j) // 2
    suma_k = sum(a[:k])
    for p in range(1, n-k+1):
        suma_k = max(suma_k, suma_k - a[p-1] + a[p+k-1])
    if suma_k > x:
        j = k - 1
    else:
        i = k + 1
print(j)
