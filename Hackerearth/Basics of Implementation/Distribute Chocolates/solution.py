T = int(input())

for i in range(T):
    c, n = map(int, input().split())
    total_cnt = (n*(n+1)) // 2
    if (n * (n+1)) // 2 > c:
        print(c)
        continue
    else:
        remaining = c - total_cnt
    print(remaining % n)
