from collections import Counter

MOD = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    cnt = Counter(Counter(a).values())
    ans = 1
    for v in cnt.values():
        ans *= pow(2, v - 1, MOD)
        ans %= MOD
    print(ans)
