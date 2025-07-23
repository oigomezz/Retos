MOD = 1000000007
t = int(input())
fact = [1]
for i in range(1, 1001):
    fact.append((fact[-1] * i) % MOD)
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    even = odd = 0
    for i in a:
        if i % 2:
            odd += 1
        else:
            even += 1
    ans = 0
    for i in range(odd + 1):
        if i % 2:
            j = k - i
            if 0 <= j <= even:
                ans += fact[odd] * pow(fact[i] * fact[odd - i] % MOD, MOD - 2, MOD) * fact[even] * pow(
                    fact[j] * fact[even - j] % MOD, MOD - 2, MOD)
                ans %= MOD
    print(ans)
