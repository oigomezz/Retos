n = int(input())
s = input()
t = input()
ans = 0
last = 0
for i in range(n):
    x = s[i] != t[i]
    ans += last == 0 and x
    last = x
print(ans)
