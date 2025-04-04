t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        ans = n ** 3
    else:
        ans = n ** 3 - (n - 2) ** 3
    print(ans)
