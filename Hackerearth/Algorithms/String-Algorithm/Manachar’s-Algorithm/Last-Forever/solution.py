s = input()
for i in range(int(input())):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = 0
    k = len(s)
    for j in range(b-1, k):
        if (a+j+1 > k):
            break
        else:
            w = s[a:a+j+1]
            if (w == w[::-1]):
                c += 1
    print(c)
