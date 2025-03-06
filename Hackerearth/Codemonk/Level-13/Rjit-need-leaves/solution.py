test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    a = map(int, input().split())
    d = {}
    for i in a:
        if i+1 in d:
            d[i+1] -= 1
            if d[i+1] == 0:
                del d[i+1]
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1

    x = 0
    for i in d:
        x += d[i]

    print(k-x if x <= k else -1)
