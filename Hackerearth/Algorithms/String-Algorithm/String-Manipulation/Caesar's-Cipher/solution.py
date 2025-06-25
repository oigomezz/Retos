k = int(input())
for _ in range(k):
    s = input().strip()
    t = input().strip()
    k = (ord(t[0]) - ord(s[0]) + 26) % 26
    for i in range(1, len(s)):
        if (ord(t[i]) - ord(s[i]) + 26) % 26 != k:
            print(-1)
            break
    else:
        print(k)
