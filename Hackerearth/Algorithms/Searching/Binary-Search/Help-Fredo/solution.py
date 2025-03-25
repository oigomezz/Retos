import math

n = int(input())
a = map(int, input().strip().split())
s = 0
for i in a:
    s += math.log10(i)

print(int(10 ** (s / n)) + 1)
