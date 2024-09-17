n = int(input())
cost = list(map(int, input().strip().split()))
counter = 0
checkSum = [False] * (2000 * n)

for i in range(1 << n):
    sum_value = 0
    for j in range(n):
        if i & (1 << j):
            sum_value += cost[j]
    if not checkSum[sum_value] and sum_value and not (sum_value & 1):
        counter += 1
    checkSum[sum_value] = True

print(counter)
