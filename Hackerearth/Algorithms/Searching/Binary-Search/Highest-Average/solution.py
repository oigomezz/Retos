from bisect import bisect_left

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
s = 0
prefix = []
for i in range(n):
    s += ls[i]
    prefix.append(s//(i+1))


for _ in range(int(input())):
    k = int(input())
    y = bisect_left(prefix, k)
    print(y)
