import math

t = int(input())
for _ in range(t):
    n = int(input())
    num = int(math.sqrt(n))
    sums = sum(n // j for j in range(1, num + 1))
    sums *= 2
    sums -= (num**2)
    print(sums)
