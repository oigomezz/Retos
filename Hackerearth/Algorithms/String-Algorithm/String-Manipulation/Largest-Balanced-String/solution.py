t = int(input())
opens = ('(', '{', '[')
closes = (')', '}', ']')
for _ in range(t):
    a = input().strip()
    ln = 0
    for i in range(3):
        c1 = a.count(opens[i])
        c2 = a.count(closes[i])
        ln += 2 * min(c1, c2)
    print(ln)
