from itertools import accumulate

n = int(input())
a = map(int, input().strip().split())
sums = list(accumulate(a, initial=0))
total = sums[-1]
max_val = 0
for i in range(1, n):
    for j in range(i, n):
        max_val = max(max_val, sums[i] ^ total - sums[j])
print(max_val)
