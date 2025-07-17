t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    prefix_sums = [0]
    for i in arr:
        prefix_sums.append((i + prefix_sums[-1]) % n)
    smallest_sub = (-1, -1)
    smallest_sub_len = float('inf')
    seen = {}
    for i, v in enumerate(prefix_sums):
        if v in seen:
            sub_len = i - seen[v]
            if sub_len < smallest_sub_len:
                smallest_sub_len = sub_len
                smallest_sub = (seen[v], i)
        seen[v] = i
    print(smallest_sub[0] + 1, smallest_sub[1])
