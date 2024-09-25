size = int(input().strip())
arr = list(map(int, input().split()))
total_sum = sum(arr)
temp = 0
res = 0
for i in range(size):
    temp += arr[i]
    res = max(temp * (total_sum - temp), res)

print(res)
