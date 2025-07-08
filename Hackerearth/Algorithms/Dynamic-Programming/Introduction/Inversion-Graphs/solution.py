from bisect import bisect_left

n = int(input())
a = list(map(int, input().strip().split()))
res = []
for x in a[::-1]:
    i = bisect_left(res, x)
    if i == len(res):
        res.append(x)
    else:
        res[i] = x
print(len(res))
