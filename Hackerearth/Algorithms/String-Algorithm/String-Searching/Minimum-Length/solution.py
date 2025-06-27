from math import ceil, sqrt

t = int(input())
for _ in range(t):
    n = int(input())
    print(int(-2 + ceil(2 * (sqrt(1 + n)))))
