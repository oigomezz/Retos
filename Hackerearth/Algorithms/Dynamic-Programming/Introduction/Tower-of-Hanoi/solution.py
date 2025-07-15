t = int(input())
for _ in range(t):
    n = int(input())
    disk = []
    for _ in range(n):
        r, h = map(int, input().strip().split())
        disk.append((r, h))
    disk.sort()
    dp = [0] * n
    dp[0] = disk[0][1]
    for i in range(1, n):
        dp[i] = disk[i][1]
        for j in range(i):
            if disk[j][1] < disk[i][1] and disk[j][0] < disk[i][0]:
                dp[i] = max(dp[i], dp[j] + disk[i][1])
    print(max(dp))
