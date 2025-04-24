t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ac = s.count('A')
    ans = ac
    for c in s:
        if c == 'A':
            ac -= 1
            if ans > ac:
                ans = ac
        else:
            ac += 1
    print(ans)
