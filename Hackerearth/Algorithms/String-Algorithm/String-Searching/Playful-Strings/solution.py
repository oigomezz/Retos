t = int(input())
for _ in range(t):
    s = input().strip()
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) not in (1, 25):
            print('NO')
            break
    else:
        print('YES')
