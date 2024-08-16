import math

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("1")
        continue
    x = math.floor((-3.0 + math.sqrt(9.0 + 8.0 * n)) / 2.0)
    print(2 * (n - x))
