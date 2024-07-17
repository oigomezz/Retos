t = int(input())
while t > 0:
    n = int(input())
    s = input()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = "" + s[0].upper()
    ctr = 0
    for i in range(1, len(s)):
        if s[i] in vowels and ctr != 0:
            res += str(ctr)
            ctr = 0
        if s[i] in vowels and res[-1] != s[i]:
            res += s[i]
        elif s[i] not in vowels:
            ctr += 1
    if ctr != 0:
        res += str(ctr)

    print(res)
    t -= 1
