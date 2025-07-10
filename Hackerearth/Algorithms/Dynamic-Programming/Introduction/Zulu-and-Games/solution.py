MOD = 1000000007
n = int(input().strip())
left_intervals = list(map(int, input().strip().split()))
right_intervals = list(map(int, input().strip().split()))
intervals = [(right_intervals[i], left_intervals[i]) for i in range(n)]
intervals.sort()

dp = [0] * n
dp[0] = 1
max_left = -1
for i in range(1, n):
    j = next((index for index in range(
        n) if intervals[index][0] >= intervals[i][1]), -1)
    j -= 1
    if j == -1:
        dp[i] = 1
        continue
    dp[i] = 0
    max_left = -1
    while j >= 0 and intervals[j][0] > max_left:
        dp[i] = (dp[i] + dp[j]) % MOD
        max_left = max(max_left, intervals[j][1])
        j -= 1

j = n - 1
answer = 0
while j >= 0 and intervals[j][0] > max_left:
    answer = (answer + (dp[j] * intervals[j][0]) % MOD) % MOD
    max_left = max(max_left, intervals[j][1])
    j -= 1

print(answer)
