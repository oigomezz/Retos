t = int(input())
for _ in range(t):
    n = int(input())
    ans = None
    s = list(map(int, input().split()))
    for i in range(n):
        x = s[i]
        popcount = bin(x).count('1')
        if i == 0:
            ans = popcount
        elif popcount < ans:
            ans = popcount

    print(ans)
