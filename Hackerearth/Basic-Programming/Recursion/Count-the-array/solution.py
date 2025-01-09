def bt(n, z, mul=1):
    if n == 0:
        return 1
    ans = 0
    for pr in primes:
        if z == 1:
            if pr * mul > p:
                break
            ans += bt(n - 1, 2, mul * pr)
        else:
            if pr * pr * mul > p:
                break
            ans += bt(n - 1, 2, mul * pr * pr)
    return ans


MAX_N = 10**6 + 14
is_not_prime = [False] * MAX_N
primes = []

for i in range(2, MAX_N):
    if not is_not_prime[i]:
        primes.append(i)
        for j in range(i, MAX_N, i):
            is_not_prime[j] = True


p = int(input())
q = int(input())
ans = [0] * 21

for i in range(1, 21):
    ans[i] = bt((i + 1) // 2, 2 - i % 2)

results = []
arr = list(map(int, input().split()))
for i in range(q):
    n = arr[i]
    results.append(str(sum(ans[:min(n + 1, 21)])))

print(' '.join(results))
