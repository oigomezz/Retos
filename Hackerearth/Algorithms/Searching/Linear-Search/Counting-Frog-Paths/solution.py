x, y, s, t = map(int, input().split())
total = 0
for i in range(x, x+s+1):
    for j in range(y, y+s+1):
        if (i+j <= t):
            total += 1

print(total)
