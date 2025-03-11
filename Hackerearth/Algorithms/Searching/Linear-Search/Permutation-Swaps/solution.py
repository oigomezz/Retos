test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    arr = [int(x) for x in input().split()]
    total_sum = 0
    ok = True

    for i in range(1, n + 1):
        x = arr[i-1]
        total_sum += x
        ok &= (total_sum >= i * (i + 1) // 2)

    ok &= (total_sum == n * (n + 1) // 2)
    print("YES" if ok else "NO")
