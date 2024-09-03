t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    assert 2 <= n <= 1000
    assert 2 <= m <= 1000
    a = [list(input().split()) for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if (a[i][j] == '/' and a[i][j + 1] == '\\' and a[i + 1][j] == '\\' and a[i + 1][j + 1] == '/'):
                cnt += 1

    print(cnt)
