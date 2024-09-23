import math

n = int(input())
count = 0

for j in range(2, 1000000):
    i = str(j)
    if '1' not in i and '0' not in i and (n == math.prod([int(x) for x in i])):
        count += 1

print(count)
