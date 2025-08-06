import math

MOD = 1000000007
A = [0] * 100005
count_factors = [0] * 100005
upper_limit = 10000
dp = [0] * 100005
ndp = [0] * 100005
sum_values = [0] * 100005
df = 1


def shift(multiplicative_factor, delete_count):
    total_sum = 0
    for idx in range(1, upper_limit + 1):
        total_sum += dp[idx - 1]
        total_sum *= multiplicative_factor
        if idx - delete_count >= 0:
            total_sum -= dp[idx - delete_count] * df
        total_sum %= MOD
        ndp[idx] = total_sum


def factor(value):
    square_root = math.isqrt(value)
    for idx in range(2, square_root + 1):
        while value % idx == 0:
            count_factors[idx] += 1
            value //= idx
    if value > 1:
        count_factors[value] += 1


dp[0] = 1
n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    A[i] = arr[i-1]
    factor(A[i])

for i in range(1, 100005):
    if count_factors[i] == 0:
        continue
    df = 1
    for j in range(1, count_factors[i] + 2):
        df = (df * i) % MOD
    shift(i, count_factors[i] + 1)
    for j in range(1, upper_limit + 1):
        dp[j] = (dp[j] + ndp[j]) % MOD
        ndp[j] = 0

for i in range(1, q + 1):
    y = int(input())
    if dp[y] < 0:
        dp[y] += MOD
    print(dp[y])
