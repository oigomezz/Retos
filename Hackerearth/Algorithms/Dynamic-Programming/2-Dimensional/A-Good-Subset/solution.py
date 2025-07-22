T = int(input())
for _ in range(T):
    n, K = map(int, input().split())
    ans = n
    arr = list(map(int, input().split()))
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = arr[i-1]
    S1 = [0] * 5005
    S2 = [0] * 5005
    S1[0] = 1
    a[1:n + 1] = sorted(a[1:n + 1])
    for i in range(1, n + 1):
        if a[i] >= K:
            ans -= 1
            continue
        S2 = S1[:]
        fgg = False
        for j in range(i, n + 1):
            S1 = [S1[k] | (S1[k - a[i]] if k >= a[i] else 0)
                  for k in range(5005)]
        for j in range(K - a[i], K):
            if S2[j]:
                ans = i - 1
                fgg = True
                break
        if fgg:
            break
    print(ans)
