n = int(input())
s = list(input().strip())
t = list(input().strip())
ans = 0
while s != t:
    s.pop(0)
    t.pop(-1)
    ans += 1
print(ans)
