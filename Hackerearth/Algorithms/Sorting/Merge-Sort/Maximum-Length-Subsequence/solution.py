def solve(n, arr):
    arr.sort()
    start = arr[0]
    max_len = cnt = j = 1
    for i in range(1, n):
        diff = arr[i] - start
        if diff <= 10:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            start = arr[j]
            j += 1
    max_len = max(max_len, cnt)
    return max_len


n = int(input())
arr = list(map(int, input().split()))

out_ = solve(n, arr)
print(out_)
