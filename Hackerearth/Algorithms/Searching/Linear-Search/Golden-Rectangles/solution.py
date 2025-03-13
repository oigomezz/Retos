n = int(input())
count = 0
for i in range(n):
    W, H = map(int, input().split())
    if (W/H >= 1.6 and W/H <= 1.7):
        count += 1
    if (H/W >= 1.6 and H/W <= 1.7):
        count += 1
print(count)
