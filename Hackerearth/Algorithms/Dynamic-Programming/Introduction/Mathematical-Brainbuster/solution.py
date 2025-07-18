from bisect import bisect_right

n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
ln = len(a)
min_rm = float('inf')
for i in range(ln):
    j = bisect_right(a, 3 * a[i])
    if j > i:
        min_rm = min(min_rm, ln - (j - i))
print(min_rm)
