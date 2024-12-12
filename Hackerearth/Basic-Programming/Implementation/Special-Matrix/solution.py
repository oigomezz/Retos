T = int(input())
out = []
prime = [0] * 2000001
for i in range(2, len(prime)):
    j = 2
    if prime[i] == 0:
        prime[i] = 1
        while (i * j) < len(prime):
            prime[i * j] += 1
            j += 1
for _ in range(T):
    N, M = map(int, input().split())
    if N > M:
        N, M = M, N
    tot = 0
    lim = N + M
    cnt = 1
    for i in range(2, lim + 1):
        tot += cnt * prime[i]
        if (i - 1) < N:
            cnt += 1
        elif (i - 1) >= M:
            cnt -= 1
    out.append(tot)
print('\n'.join(map(str, out)))
