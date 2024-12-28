t = int(input())
for _ in range(t):
    s = input().strip()
    l = len(s)

    if l % 3 != 0:
        print("Not OK")
        continue

    cond = True

    for j in range(l // 3):
        if s[0] == s[j] and s[l // 3] == s[j + l // 3] and s[2 * (l // 3)] == s[j + l // 3 + l // 3]:
            cond = True
        else:
            cond = False
            break

    if cond and s[0] != s[l // 3] and s[l // 3] != s[2 * (l // 3)] and s[0] != s[2 * (l // 3)]:
        print("OK")
    else:
        print("Not OK")
