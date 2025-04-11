t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    pos = s.find('3')
    pre = s[:pos]
    suf = s[pos:]
    pre += ''.join(c for c in suf if c == '2')
    suf = ''.join(c for c in suf if c != '2')
    print(''.join(sorted(pre)) + suf)
