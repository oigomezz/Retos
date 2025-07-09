t = int(input())
MOD = 1000000007
for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input().strip()
    ways = [1]
    for i in range(len(s)):
        count = 0
        for j in range(i, -1, -1):
            if int(s[j:i + 1]) < k:
                count += ways[j]
                count %= MOD
            else:
                break
        ways.append(count)
    print(ways[-1])
