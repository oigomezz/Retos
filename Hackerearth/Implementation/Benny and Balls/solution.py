Q = int(input())
for _ in range(Q):
    n = int(input())
    p = list(map(int, input().split()))
    x, a, b, t = map(int, input().split())

    ans = 0
    cnt = [0] * n
    for i in range(1, t + 1):
        cnt[x] += 1
        if cnt[x] >= p[x]:
            ans += 1
            cnt[x] = 0
        x = (x * a + b) % n

    print(ans)
