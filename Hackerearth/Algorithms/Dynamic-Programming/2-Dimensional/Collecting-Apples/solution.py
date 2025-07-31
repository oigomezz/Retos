test_cases = int(input())
for _ in range(test_cases):
    n, p = map(int, input().split())
    milk = [0] * (n + 1)
    apples = [0] * (n + 1)
    max_apples = [[0] * (n + 1) for _ in range(n + 1)]

    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        milk[i] = arr[i-1]

    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        apples[i] = arr[i-1]

    max_apples[n][0] = apples[n]
    for i in range(n - 1, 0, -1):
        if milk[i] > 0:
            max_apples[i][0] = max(
                apples[i], max_apples[i + 1][min(milk[i] - 1, n - i - 1)])
        else:
            max_apples[i][0] = apples[i]

        for temp in range(1, n - i + 1):
            max_apples[i][temp] = max(apples[i] + max_apples[i + 1][temp - 1],
                                      max_apples[i + 1][min(milk[i] - 1 + temp, n - i - 1)])

    if p > 0:
        print(max_apples[1]
              [min(p - 1, n - 1)])
    else:
        print("0")
