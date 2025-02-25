t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n

    for i in range(n):
        h = (i + k) % n
        ans[h] = a[i]

    print(" ".join(map(str, ans)))
