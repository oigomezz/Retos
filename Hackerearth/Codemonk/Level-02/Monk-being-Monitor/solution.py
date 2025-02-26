from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mp = defaultdict(int)
    for num in a:
        mp[num] += 1

    req = list(mp.values())
    req.sort()

    if len(req) > 0:
        diff = req[-1] - req[0]
        print(diff if diff > 0 else -1)
    else:
        print(-1)
