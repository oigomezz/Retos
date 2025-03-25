def count_subset(arr, k, add, i=0):
    if i >= len(arr):
        return 0

    count = 0
    if add + arr[i] < k:
        count += 1 + count_subset(arr, k, add + arr[i], i+1)
    if add < k:
        count += count_subset(arr, k, add, i+1)
    return count


N = int(input())
A = list(map(int, input().split()))
K = int(input())
total = 2 ** len(A) - 1
if min(A) >= K:
    print(total)

count = count_subset(A, K, 0)
print(total - count)
