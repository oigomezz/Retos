n = int(input())
a = list(map(int, input().strip().split()))
left = a[::]
right = a[::-1]
for i in range(1, n):
    left[i] += left[i - 1] // 2
    right[i] += right[i - 1] // 2
right.reverse()
print(max(left[i] + right[i] - a[i] for i in range(n)))
