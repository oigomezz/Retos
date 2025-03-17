t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        x, s = l[i], l[i]
        for j in range(i+1, n):
            x ^= l[j]
            s += l[j]
            if x == s:
                c += 1
            if x != s:
                break
    c += n
    print(c)
