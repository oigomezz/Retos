from bisect import bisect_left

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    v = []
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        x = arr[i-1]
        v.append((x, i))

    v.sort()
    s = set()
    s.add(v[0][1])
    ans = 0

    for i in range(1, n):
        temp = 100000000
        bb = v[i][1] - k
        ff = v[i][1] + k

        left_index = bisect_left(sorted(s), bb)
        right_index = bisect_left(sorted(s), ff)

        flag = False

        if left_index == len(s) or sorted(s)[left_index] > bb:
            if left_index == 0:
                flag = True
            left_index -= 1

        if not flag and bb >= 1:
            temp = abs(v[i][1] - sorted(s)[left_index])
        if right_index < len(s) and ff <= n:
            temp = min(temp, abs(sorted(s)[right_index] - v[i][1]))

        if temp != 100000000:
            ans += temp

        s.add(v[i][1])

    print(ans)
