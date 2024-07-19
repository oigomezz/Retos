from collections import defaultdict

d = defaultdict(str)
d['a'], d['e'], d['o'], d['i'], d['u'] = 'b', 'f', 'p', 'j', 'v'

t = int(input())
while t > 0:
    s = list(input())
    n = int(input())
    for i in range(len(s)):
        if (n and d[s[i]]):
            s[i] = d[s[i]]
            n -= 1
        elif (not n):
            break
    print(''.join(s))
    t -= 1
