from collections import defaultdict

n, k = map(int, input().strip().split())
a = map(int, input().strip().split())
bucket = defaultdict(list)
for i in a:
    bucket[i % k].append(i)
for key in sorted(bucket.keys(), reverse=True):
    print(*sorted(bucket[key]), end=' ')
