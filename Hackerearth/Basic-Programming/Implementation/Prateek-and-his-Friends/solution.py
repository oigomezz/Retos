t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(int(input()))

    sum = 0
    start = 0
    P = 0

    for i in range(n):
        sum += l[i]
        while sum > m:
            sum -= l[start]
            start += 1
        if sum == m:
            P = 1
            break

    if P == 1:
        print("YES")
    else:
        print("NO")
