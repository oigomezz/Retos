n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
bit_count = [0] * n
for i in range(n):
    bit_count[i] = bin(arr[i]).count('1')

prefix_sum = [0] * (n + 1)
total_sum = 0
for i in range(n):
    total_sum += bit_count[i]
    prefix_sum[i + 1] = total_sum

for _ in range(q):
    x = int(input())
    result = 0
    minimum = float('inf')

    for i in range(1, n + 1):
        low = next((j for j in range(n + 1)
                   if prefix_sum[j] >= x + prefix_sum[i - 1]), n + 1)
        if low < n + 1:
            result = low - i + 1
            if result < -1:
                minimum = 1
            else:
                minimum = min(minimum, result)

    if minimum > n:
        print("-1")
    else:
        print(minimum)
