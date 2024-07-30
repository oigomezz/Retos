n = int(input())
for i in range(n):
    s = input().strip()
    ans = s[::-1]
    b = []
    for i in range(len(s)):
        b.append(ord(s[i]) % 96)

    c = []
    for i in range(len(ans)):
        c.append(ord(ans[i]) % 96)

    m = []
    for i in range(len(ans)):
        m.append((b[i]+c[i])+96)

    k = []
    for i in range(len(m)):
        if m[i] > 122:
            t = (m[i] - 122) + 96
            k.append(chr(t))
        else:
            k.append(chr(m[i]))

    for i in range(len(k)):
        print(k[i], end='')
    print('')
