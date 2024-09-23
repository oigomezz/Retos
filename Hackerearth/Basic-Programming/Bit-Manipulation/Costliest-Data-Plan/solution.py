t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    requiredOR = 0
    for num in a:
        requiredOR |= num

    prefix = [0] * (n + 2)
    suffix = [0] * (n + 2)

    for i in range(1, n + 1):
        prefix[i] = (prefix[i - 1] | a[i - 1])

    for i in range(n, 0, -1):
        suffix[i] = (suffix[i + 1] | a[i - 1])

    ans = 0
    for i in range(1, n + 1):
        if (prefix[i - 1] | suffix[i + 1]) == requiredOR:
            ans = max(ans, a[i - 1])

    results.append(str(ans))

print("\n".join(results))
