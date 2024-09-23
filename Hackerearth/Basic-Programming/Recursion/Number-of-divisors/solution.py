def rans(n, k):
    suma = n * (n + 1) // 2
    if n < 1:
        return suma
    x = n // k
    suma -= k * x * (x + 1) // 2
    return suma + rans(x, k)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(rans(n, k))
