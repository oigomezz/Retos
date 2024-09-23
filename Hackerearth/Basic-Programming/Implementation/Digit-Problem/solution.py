n, c = map(int, input().strip().split())
cnt = 0
s = ''
for x in str(n):
    if int(x) < 9 and cnt < c:
        cnt = cnt+1
        s = s+'9'
    else:
        s = s+x
print(s)
