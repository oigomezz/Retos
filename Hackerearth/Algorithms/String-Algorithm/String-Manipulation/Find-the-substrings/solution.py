t = int(input())
for _ in range(t):
    s = input().strip()
    a = b = c = 0
    ln = len(s)
    ans = (ln * (ln + 1)) // 2
    for i in range(ln):
        if s[i] == 'a':
            a = i + 1
            ans -= min(b, c)
        elif s[i] == 'b':
            b = i + 1
            ans -= min(a, c)
        elif s[i] == 'c':
            c = i + 1
            ans -= min(a, b)
    print(ans)
