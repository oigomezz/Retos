s = input()
q = int(input())

for _ in range(q):
    ind, ch = input().split()
    x = int(ind) - 1
    s = s[:x] + ch + s[x + 1:]

print(s)
temp = list(s)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    p = (b - a + 1) // 2 + (a - 1)
    for i in range(a - 1, p):
        s_list = list(s)
        s_list[i], s_list[b - 1 - (i - (a - 1))
                          ] = s_list[b - 1 - (i - (a - 1))], s_list[i]
        s = ''.join(s_list)

print(s)

count = 0
for i in range(len(s)):
    if temp[i] == s[i]:
        count += 1
print(count)
