n = int(input())
barriers = []
for _ in range(n):
    x, y, d = map(int, input().strip().split())
    barriers.append((x, x + d))
barriers.sort()

count = marker = 0
for barrier in barriers:
    if barrier[0] >= marker:
        marker = barrier[0]
        if marker < barrier[1]:
            count = count + (barrier[1] - marker) + 1
            marker = barrier[1] + 1
    elif marker <= barrier[1]:
        count = count + (barrier[1] - marker) + 1
        marker = barrier[1] + 1

print(count)
