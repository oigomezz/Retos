prefix = [0] * 100001
f = [-1] * 100001
answer = 0
n = int(input().strip())
for i in range(2, 100001):
    if f[i] == -1:
        for j in range(i, 100001, i):
            if f[j] == -1:
                f[j] = i

arr = list(map(int, input().split()))
for i in range(n):
    ai = arr[i]
    factors = []
    x = ai
    while x > 1:
        if not factors or f[x] != factors[-1]:
            factors.append(f[x])
        x //= f[x]

    sum_factors = 0
    for mask in range(1 << len(factors)):
        sign = -1 if bin(mask).count('1') & 1 else 1
        prod = 1
        for j in range(len(factors)):
            if mask >> j & 1:
                prod *= factors[j]
        prefix[prod] += (i + 1)
        sum_factors += sign * prefix[prod]

    sum_factors = (1 + i + 1) * (i + 1) // 2 - sum_factors
    answer += sum_factors * (n - i)
    if answer > 1000000000000000000:
        answer = 1000000000000000000 + 1

if answer > 1000000000000000000:
    print(-1)
else:
    print(answer)
