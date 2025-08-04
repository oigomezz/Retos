MOD = 1000000007

n = int(input())
assert 1 <= n <= 100000
array = list(map(int, input().split()))

assert all(0 <= element <= 100 for element in array)

current_index = 0
previous_index = 1
answer = 0
dp = [[0] * 128 for _ in range(2)]

dp[current_index][0] = 1

for i in range(n):
    previous_index = current_index
    current_index ^= 1
    for j in range(128):
        dp[current_index][j] = (
            dp[previous_index][j] + dp[previous_index][j ^ array[i]]) % MOD

dp[current_index][0] -= 1

for i in range(128):
    count = dp[current_index][i]
    ways = (count - 1 + MOD) % MOD
    ways = (ways * count) % MOD
    ways = (ways * 500000004) % MOD
    answer += ways
    if answer >= MOD:
        answer -= MOD

print(answer)
