t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = -1
    for i in range(m):
        if (i * i) % m == n:
            ans = i
            break
    print(str(ans))
