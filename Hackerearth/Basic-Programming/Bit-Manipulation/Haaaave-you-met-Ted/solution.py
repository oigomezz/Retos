t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    ans = bin(s[0]).count('1')
    for i in range(1, n):
        x = s[i]
        popcount = bin(x).count('1')
        if popcount < ans:
            ans = popcount

    print(ans)
