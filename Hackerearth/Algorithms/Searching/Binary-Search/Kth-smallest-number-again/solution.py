t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    intervals = []
    for i in range(n):
        a, b = map(int, input().split())
        intervals.append((a, b))

    intervals.sort()
    idx = 0
    for i in range(1, len(intervals)):
        if intervals[idx][1] >= intervals[i][0]:
            intervals[idx] = (intervals[idx][0], max(
                intervals[idx][1], intervals[i][1]))
        else:
            idx += 1
            intervals[idx] = intervals[i]

    for _ in range(q):
        k = int(input())
        ans = -1
        for i in range(idx + 1):
            if (intervals[i][1] - intervals[i][0] + 1) >= k:
                ans = intervals[i][0] + k - 1
                break
            else:
                k -= (intervals[i][1] - intervals[i][0] + 1)
        print(ans)
