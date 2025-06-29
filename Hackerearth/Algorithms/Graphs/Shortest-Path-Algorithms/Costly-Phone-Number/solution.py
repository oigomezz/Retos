t = int(input())
for _ in range(t):
    costs = list(map(int, input().strip().split()))
    while True:
        reduced = False
        for i in range(10):
            for j in range(i, 10):
                k = (i + j) % 10
                if costs[k] > costs[i] + costs[j]:
                    reduced = True
                    costs[k] = costs[i] + costs[j]
        if not reduced:
            break
    target = int(input())
    s = input()
    ans = 0
    for i in s:
        ans += costs[ord(i) - 48]  # ord(0) = 48
    print(ans)
