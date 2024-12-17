t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    chocolates = list(map(int, input().split()))

    mp = {0: -1}
    prefix = [0] * n
    sum_val = 0
    max_val = 0

    for i in range(n):
        sum_val += chocolates[i]
        prefix[i] = sum_val
        if sum_val % m not in mp:
            mp[sum_val % m] = i
        else:
            if sum_val % m == 0:
                max_val = sum_val
            else:
                max_val = max(max_val, sum_val - prefix[mp[sum_val % m]])

    print(max_val // m)
