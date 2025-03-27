def max_len(nums, n):
    prefix = [0]
    for val in nums:
        prefix.append(prefix[-1] + val)
    indices = list(range(n + 1))
    indices.sort(key=lambda x: prefix[x])
    min_val = float("inf")
    cnt = 0
    ans = 0
    for i in indices:
        nans = i - min_val
        if ans < nans:
            cnt = 1
            ans = nans
        elif ans == nans:
            cnt += 1
        min_val = i if i < min_val else min_val
    if cnt:
        print(ans, cnt)
    else:
        print(-1)


n = int(input())
a = list(map(int, input().split()))
max_len(a, n)
