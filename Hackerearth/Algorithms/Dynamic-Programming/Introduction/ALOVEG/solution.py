t = int(input())
for _ in range(t):
    s = input().strip()
    count = sub = 0
    mx_sub = float('-inf')
    for c in s:
        if c == 'A':
            sub -= 1
            count += 1
        else:
            sub += 1
        mx_sub = max(mx_sub, sub)
        if sub == -1:
            sub = 0
    print(count + mx_sub)
