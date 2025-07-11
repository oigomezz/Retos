from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    ans = n * (n + 1) // 2
    counter = defaultdict(int)
    j = -1
    for i, x in enumerate(a):
        counter[x] += 1
        while counter[x] >= k:
            j += 1
            counter[a[j]] -= 1
        ans -= i - j
    print(ans)
