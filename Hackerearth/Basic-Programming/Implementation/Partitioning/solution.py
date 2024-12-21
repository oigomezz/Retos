def value(b, c):
    val = 0
    l = 1
    for i in range(c, b - 1, -1):
        if s[i] == '1':
            val += l
        l *= 2
    return val


s = input()
c, p = map(int, input().split())
length = len(s)
ans = 0

for i in range(length - 2):  # partition 2 after ith position
    cl = 0
    cr = 0
    for j in range(max(0, i - 25 + 1), i + 1):
        a = value(j, i)
        if a == c:
            cl += 1
    for j in range(i + 1, min(length, i + 26)):
        a = value(i + 1, j)
        if a == p:
            cr += 1
    ans += cr * cl

print(ans)
