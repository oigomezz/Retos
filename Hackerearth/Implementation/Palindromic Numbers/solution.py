t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = 0
    for i in range(a, b+1):
        if str(i) == str(i)[::-1]:
            c += 1
    print(c)
